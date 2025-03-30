from django.test import TestCase
from .models import Event

class EventModelTest(TestCase):

    def setUp(self):
        self.event = Event.objects.create(
            title="Sample Event",
            description="This is a sample event.",
            date="2023-10-01",
            location="Sample Location"
        )

    def test_event_creation(self):
        self.assertEqual(self.event.title, "Sample Event")
        self.assertEqual(self.event.description, "This is a sample event.")
        self.assertEqual(str(self.event), "Sample Event")

    def test_event_date(self):
        self.assertEqual(self.event.date, "2023-10-01")

    def test_event_location(self):
        self.assertEqual(self.event.location, "Sample Location")