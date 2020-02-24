from .base import *
try:
    from .production import *
    from .local import *
except:
    print("setting import error")
