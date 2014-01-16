from django.contrib import admin

from .models import Blog, Category, BlogImage, BlogSearch



class BlogAdmin(admin.ModelAdmin):
    #exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    class Meta:
        model = Blog
        
admin.site.register(Blog, BlogAdmin)




class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)



class BlogSearchAdmin(admin.ModelAdmin):
  
    class Meta:
        model = BlogSearch

admin.site.register(BlogSearch, BlogSearchAdmin)


