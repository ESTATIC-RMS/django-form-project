from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class PrifileAdmin(admin.ModelAdmin):
    fields = (
        'name', 'dob', 'gender', 'locality', 'city', 'pin',
        'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file'
    )

    