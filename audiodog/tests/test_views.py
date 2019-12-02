from django.test import TestCase,Client

# Create your tests here.
import datetime
from django.utils import timezone
from django.urls import reverse
from audiodog.models import Cancion


class TestViews(TestCase):

    def setUp(self):
        self.cancion = Cancion()
        self.list_url = reverse('cancion_list')
