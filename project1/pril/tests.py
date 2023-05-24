from django.test import *
from django.urls import reverse, resolve
from .views import *

from . import factories
from .models import *
from .factories import *


class TeamTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_list(self):
        respounse = self.client.get(reverse('team'))
        self.assertEqual(respounse.status_code, 200)

    def test_team_add(self):
        url = reverse('addteam')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


