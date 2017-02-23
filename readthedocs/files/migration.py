import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'readthedocs.settings.dev')
sys.path.append(os.getcwd())

from django.contrib.auth.models import User

admin = User.objects.create_user('admin', '', 'admin')
admin.is_superuser = True
admin.is_staff = True
admin.save()
test = User.objects.create_user('test', '', 'test')
test.is_staff = True
test.save()
