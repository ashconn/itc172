from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting

# Create views here.
def index (request):
    return render(request, 'club/index.html')

def resource (request):
    type_list=Resource.objects.all()
    return render(request, 'club/resource.html', {'type_list': type_list})

def meeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meeting.html', {'meeting_list': meeting_list})

def meetingdetail(request, id):
    detail=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetail.html', {'detail': detail})

