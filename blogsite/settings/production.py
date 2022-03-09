from .base import *

DEBUG = False

CSRF_TRUSTED_ORIGINS = ['https://blog.petal2collect.art','https://*.127.0.0.1']

try:
    from .local import *
except ImportError:
    pass
