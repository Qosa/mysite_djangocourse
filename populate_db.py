import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

import django
django.setup()

import random
from userdb.models import Users
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        fake_name = fakegen.name()
        fake_email = fakegen.email()

        user_data = Users.objects.get_or_create(name=fake_name,email=fake_email)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")

