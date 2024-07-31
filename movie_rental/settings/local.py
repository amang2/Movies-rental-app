from .base import *

if DEBUG:
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

INSTALLED_APPS += ["debug_toolbar"]


# # if DEBUG:
# #     MIDDLEWARE.insert(-1, "helper.custom_middleware.ErrorEmailMiddleware")

# # mailhog settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = '127.0.0.1'
# EMAIL_PORT = 1025
# EMAIL_HOST_USER = "nikhil@mail.com"
# EMAIL_HOST_PASSWORD = "qweqweqwe"