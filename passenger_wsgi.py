# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0000006/data/platina/')
sys.path.insert(1, '/var/www/u0000006/data/platina/platina/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'platina.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
