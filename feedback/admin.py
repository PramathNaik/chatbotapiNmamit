from django.contrib import admin
from feedback.models import feedback
# Register your models here.
class respAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_date','feedback')

admin.site.register(feedback,respAdmin)