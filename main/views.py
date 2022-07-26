import random
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from feedback.models import feedback
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        feedbacks = request.POST['feedback']
        feedback.objects.create(name=name,email=email,feedback=feedbacks)
        messages.add_message(request, messages.SUCCESS, 'Thank You for Your Response')
    return render(request,"bot.html")


def handler500(request, *args, **argv):
    msgrsp = ("Did't Get That","Could you please re-phrase that?")
    obj = {"message":random.choice(msgrsp)}
    return JsonResponse(obj)