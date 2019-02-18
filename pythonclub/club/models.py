from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# meeting, meetingmin, resource, event

class Meeting(models.Model):
    meetingtitle = models.CharField(max_length=255)
    date = models.DateField()
    time = models.SmallIntegerField()
    location = models.CharField(max_length=255)
    agenda = models.TextField()

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table = 'Meeting'

class MeetingMin(models.Model):
    meetingid = models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    minutes = models.TextField()

    def __str__(self):
        return self.meetingid

    class Meta:
        db_table='MeetingMin'

class Resource(models.Model):
    resname = models.CharField(max_length=255)
    restype = models.CharField(max_length=255)
    resurl = models.URLField(null=True, blank=True)
    dateentry = models.DateField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField()

    def __str__(self):
        return self.resname
    
    class Meta:
        db_table='Resource'

class Event(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.SmallIntegerField()
    description = models.TextField()
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.title

    class Meta:
        db_table='Event'

