from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from main.models import QNA


# Create your views here.
def index(request):
    if request.method == "GET":
        inData = request.GET.get("data")
        outData = get_object_or_404(QNA,question__icontains = inData)
        obj = {"message":outData.answer}

        return JsonResponse(obj)
    else:
        obj = {"message":"Not Defined"}
        return JsonResponse(obj)
def addxl(request):
    if request.method == "GET":
        question = request.GET.get("q")
        answer = request.GET.get("a")
        QNA.objects.create(question=question,answer=answer)
        return HttpResponse("success")

