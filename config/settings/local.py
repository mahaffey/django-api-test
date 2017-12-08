from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SERCET_KEY', default='ue&au@d$ho+&)kou_#*9^q3ywc2%xowoxuvjqoc2%a7cdiwugm')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
