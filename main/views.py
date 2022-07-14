from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from main.models import QNA


# Create your views here.
def index(request):
    return render(request,"bot.html")


