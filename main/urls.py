from django.urls import path
from main import views
from simple_chatbot.views import SimpleChatbot


urlpatterns = [
    path("bot", SimpleChatbot.as_view()),
    path("",views.index),
]
