from django.shortcuts import render
from .models import user_collection
from django.http import HttpResponse

def index(request):
    return HttpResponse("<H1>App is running..</h1>")

def add_user(request):
    records = {
        "first_name" : "Joao",
        "last_name" : "Nogueira"
    }
    user_collection.insert_one(records)
    return HttpResponse("New user is added")

def get_all_users(request):
    users =  user_collection.find()
    return HttpResponse(users)