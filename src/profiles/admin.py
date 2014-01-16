from django.contrib import admin

from .models import Profile, UserPicture

class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile
        
admin.site.register(Profile, ProfileAdmin)


class UserPictureAdmin(admin.ModelAdmin):
    class Meta:
        model = UserPicture
        
admin.site.register(UserPicture, UserPictureAdmin)