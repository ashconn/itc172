from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required

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

# Form view
@login_required
def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})

@login_required
def newResource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')