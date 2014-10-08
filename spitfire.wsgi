#!/usr/bin/env python
import os, sys

#sanity check
if not os.path.exists('/var/www2/palabras/live/repo/palabras'):
        raise Exception("Palabras dir not found")
if not os.path.exists('/var/www2/palabras/live/repo/palabras/settings.py'):
        raise Exception("settings not found")

if not '/var/www2/palabras/live/repo' in sys.path:
    sys.path.append('/var/www2/palabras/live/repo')
if not '/var/www2/palabras/live/repo/palabras' in sys.path:
    sys.path.append('/var/www2/palabras/live/repo/palabras')

os.environ['DJANGO_SETTINGS_MODULE'] = 'palabras.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


