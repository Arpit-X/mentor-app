import os
import django
os.environ['DJANGO_SETTINGS_MODULE']='summerMRND.settings'
django.setup()
from onlineapp.models import *

manager =College.objects
querySets =College.objects.all()
print(querySets)
for itr in querySets:
    print(itr)