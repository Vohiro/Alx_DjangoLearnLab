import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings.py")
from django.core.asgi import get_asgi_application

app = get_asgi_application()
