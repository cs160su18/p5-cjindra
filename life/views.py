from django.shortcuts import render
from django.core import serializers
from life.models import *

def index(request):
    all_posts = Post.objects.all()
    all_answers = Answer.objects.all()
    return render(request, 'life/index.html', {"posts": all_posts, "answers": all_answers})