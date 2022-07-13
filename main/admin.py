from django.contrib import admin
from main.models import QNA
class qnaAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']

# Register your models here.
admin.site.register(QNA,qnaAdmin)