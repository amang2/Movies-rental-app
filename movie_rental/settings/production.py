# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration
from django.conf import settings

# import simple
from .base import *

# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================

# CSRF_COOKIE_SECURE = True
#CSRF_COOKIE_HTTPONLY = True

#SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_SSL_REDIRECT = True
#SECURE_BROWSER_XSS_FILTER = True
#SECURE_CONTENT_TYPE_NOSNIFF = True
#SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# SESSION_COOKIE_SECURE = True


# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================

# sentry_sdk.init(
#     dsn=config("SENTRY_DSN", default=""),
#     environment=SIMPLE_ENVIRONMENT,
#     release="simple@%s" % simple.__version__,
#     integrations=[DjangoIntegration()],
# )

# MIDDLEWARE.insert(-1, "helper.custom_middleware.ErrorEmailMiddleware")

# settings.REST_FRAMEWORK.update({'DEFAULT_RENDERER_CLASSES':(
#             'rest_framework.renderers.JSONRenderer',
#         ),
# })

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': timedelta(hours=24),
# }

# EMAIL_BACKEND = config('EMAIL_BACKEND', default='')
# # # EMAIL_USE_TLS = True # TLS setting will be disabled for private mail service
# EMAIL_USE_SSL = config('EMAIL_USE_SSL', default=True, cast=bool)
# EMAIL_HOST = config('EMAIL_HOST', default='')
# EMAIL_PORT = config('EMAIL_PORT', default=465)  
# EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='email@mail.com')  
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')  
