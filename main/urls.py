from django.urls import path
from main import views
from simple_chatbot.views import SimpleChatbot
from django.contrib import admin

urlpatterns = [
    path("bot", SimpleChatbot.as_view()),
    path("",views.index),
]
admin.site.site_header = 'NMAMIT BOT ADMINISTRATION'
