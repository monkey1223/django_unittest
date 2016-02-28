import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_test.settings'

import django
django.setup()

from verify_pack.test_verify import *