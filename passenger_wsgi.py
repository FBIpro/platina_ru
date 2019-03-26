# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0683760/data/platina_ru/')
sys.path.insert(1, '/var/www/u0683760/data/platina_ru/platina/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'platina.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
