from django.test import TestCase
from .models import Meeting, MeetingMin, Resource, Event

# Create your tests here.
class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='New Member Orientation')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

class MeetingMinTest(TestCase):
    def test_stringOutput(self):
        meetingmin=MeetingMin(meetingid='1')
        self.assertEqual(str(MeetingMin), MeetingMin.meetingid)

    def test_tablename(self):
        self.assertEqual(str(MeetingMin._meta.db_table), 'Meeting Minutes')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resname='GitHub')
        self.assertEqual(str(resource), resource.resname)

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'Resource')

class EventTest(TestCase):
    def test_stringOutput(self):
        event=Event(title='Test')
        self.assertEqual(str(event), event.title)

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'Event')
