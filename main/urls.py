from django.urls import path
from main import views
from simple_chatbot.views import SimpleChatbot


urlpatterns = [
    path("", SimpleChatbot.as_view()),
    path('addxl',views.addxl),
]
