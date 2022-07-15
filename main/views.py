import random
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from feedback.models import feedback


# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        feedbacks = request.POST['feedback']
        feedback.objects.create(name=name,email=email,feedback=feedbacks)
    return render(request,"bot.html")


def handler500(request, *args, **argv):
    msgrsp = ("Did't Get That","Could you please re-phrase that?","What does that mean?")
    obj = {"message":random.choice(msgrsp)}
    return JsonResponse(obj)