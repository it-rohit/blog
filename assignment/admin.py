from django.contrib import admin
from django.http.request import HttpRequest
from .models import About_1,Social_link

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count= About_1.objects.all().count()
        if count == 0:
            return True
        return False


admin.site.register(About_1,AboutAdmin)
admin.site.register(Social_link)