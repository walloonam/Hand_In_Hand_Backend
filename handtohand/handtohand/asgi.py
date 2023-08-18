import os

import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from chatting.routing import websocket_urlpatterns

from handtohand import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "handtohand.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":
        AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
    ,
})