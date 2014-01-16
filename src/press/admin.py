from django.contrib import admin

from .models import News, NewsImage

class NewsAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('headline',)}
    class Meta:
        model = News
        
        
admin.site.register(News, NewsAdmin)



class NewsImageAdmin(admin.ModelAdmin):
    class Meta:
        model = NewsImage
        
admin.site.register(NewsImage, NewsImageAdmin)