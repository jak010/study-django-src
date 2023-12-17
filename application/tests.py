import random
import string

from django.test import TestCase

from application.models import Person


# Create your tests here.


class PersonCreateTest(TestCase):

    def test_create_person(self):
        for _ in range(10):
            random_name = ''.join(random.choices(string.ascii_lowercase, k=5))
            person = Person.objects.create(name=random_name)

        assert person.name == "jako"
