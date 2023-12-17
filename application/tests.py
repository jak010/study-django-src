# from django.test import TestCase

from application.models import Person
from django.test.client import Client

from unittest import TestCase


# Create your tests here.


class PersonCreateTest(TestCase):

    def test_person_create_view(self):
        client = Client()
        resp = client.post(path="/api/v1/person")
        assert resp.status_code == 200
