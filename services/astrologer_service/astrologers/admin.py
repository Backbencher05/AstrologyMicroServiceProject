from django.contrib import admin
from .models import Astrologer
# Register your models here.


class AstrologerAdmin(admin.ModelAdmin):
    list_display = ['name', 'expertise', 'experience_years', 'rating']



admin.site.register(Astrologer, AstrologerAdmin)