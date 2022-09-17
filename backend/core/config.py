import os
from pathlib import Path
from dotenv import dotenv_values

dotenv_path = os.path.join(Path(__file__).resolve().parent.parent.parent, '.env')

dotenv_values(dotenv_path)
class BaseConfig:
    BASE_DIR = Path(__file__).resolve().parent.parent
    SECRET_KEY = "TheSecretKey"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOAD_FOLDER  = os.path.join(BASE_DIR, 'media')

    # Celery task
    CELERY_BEAT_SCHEDULE = {}
    TIMEZONE = "Asia/Jakarta"
    CELERY_ENABLE_UTC = False

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI_DEV")
    broker_url = os.environ.get("CELERY_BROKER_URL_DEV")
    RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND_DEV")

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_ENV= os.environ.get("FLASK_ENV")
    
    broker_url = os.environ.get("CELERY_BROKER_URL")
    RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")


