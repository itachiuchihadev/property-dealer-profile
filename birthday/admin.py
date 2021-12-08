from django.contrib import admin
from .models import Birthday

class BirthdayAdmin(admin.ModelAdmin):
    birthday_display=('name', 'is_published')
    list_per_page = 25


admin.site.register(Birthday, BirthdayAdmin)