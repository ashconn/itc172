from django.shortcuts import render, get_object_or_404
from .models import GameType, Game, Review
from .forms import GameForm, GameTypeForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'reviewapp/index.html')

def gametype(request):
    type_list = GameType.objects.all()
    return render (request, 'reviewapp/types.html', {'type_list': type_list})

def game(request):
    game_list = Game.objects.all()
    return render (request, 'reviewapp/games.html', {'game_list': game_list})

def review(request):
    review_list = Review.objects.all()
    return render (request, 'reviewapp/reviews.html', {'review_list': review_list})

# Form views

@login_required
def newgame(request):
    form=GameForm
    if request.method=='POST':
        form.GameForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=GameForm()
    else:
        form=GameForm()
    return render(request, 'reviewapp/newgame.html', {'form': form})

@login_required
def newreview(request):
    form=ReviewForm
    if request.method=='POST':
        form.ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
    else:
        form=ReviewForm()
    return render(request, 'reviewapp/newreview.html', {'form': form})

def loginmessage(request):
    return render(request, 'reviewapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'reviewapp/logoutmessage.html')