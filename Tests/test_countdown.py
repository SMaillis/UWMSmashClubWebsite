from django.test import TestCase, Client
from datetime import datetime

class TestCountdown(TestCase):
    def setUp(self):
        self.donkey = Client()
        self.scheduled = datetime(2025, 9, 5, 4, 30, 0) #year, month, day, hour, minute, second

    def test_bracket_in_an_hour(self):
        pass

