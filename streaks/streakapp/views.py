from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import datetime 
from .models import Question, User, SolvedData
# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

def generate_problems():
    pass

def get_todays_problems(request):
    questions = Question.objects.filter(date__date=datetime.date.today())
    if len(questions) == 0:
        generate_problems()