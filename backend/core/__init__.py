import os
from celery import Celery

def celery_app(app_name=__name__) -> Celery:
    """create celery object to make a module of celery task

    Args:
        app (None): _description_

    Returns:
        Celery: _description_
    """
    if os.environ.get("FLASK_ENV") == "development":
        print("Broker development")
        redis_broker = os.environ.get("CELERY_BROKER_URL_DEV")
        redis_backend = os.environ.get("CELERY_RESULT_BACKEND_DEV")
        return Celery(app_name, backend=redis_backend, redis_broker=redis_broker)
    else:
        print("Broker Production")
        redis_broker = os.environ.get("CELERY_BROKER_URL")
        redis_backend = os.environ.get("CELERY_RESULT_BACKEND")
        return Celery(app_name, backend=redis_backend, redis_broker=redis_broker)

celery_exc = celery_app()