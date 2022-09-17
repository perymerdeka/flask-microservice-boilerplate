import os
from typing import Any
from celery import Celery
from flask import Flask
from celery.schedules import crontab 

def init_celery(celery: Any, app: Flask):
    """Adding Flask to Celery Support

    Args:
        app (Flask): Flask Object

    Returns:
        Celery: Celery Object
    """

    if os.environ.get("FLASK_ENV") == "development":
        app.config.update({
            'broker_url': os.environ.get("CELERY_BROKER_URL_DEV"),
            "result_backend": os.environ.get("CELERY_RESULT_BACKEND_DEV")
        })
    else:
         app.config.update({
            'broker_url': os.environ.get("CELERY_BROKER_URL"),
            "result_backend": os.environ.get("CELERY_RESULT_BACKEND")
        })
    

    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args: Any, **kwargs: Any) -> Any:
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery