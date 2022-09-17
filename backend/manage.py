from core.factory import create_app
from core import celery_exc
app = create_app(celery=celery_exc)

if __name__ == "__main__":
    app.run()