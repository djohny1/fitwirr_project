from django.contrib import admin

from .models import Exercise, Category, ExerciseImage, Tag, CategoryImage


class CategoryImageInline(admin.TabularInline):
    model = CategoryImage



class TagInline(admin.TabularInline):
    prepopulated_fields = {"slug" : ('tag',)}
    extra = 1
    model = Tag

class ExerciseImageInline(admin.TabularInline):
    model = ExerciseImage



class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('description','muscle', 'level',  'categories', 'live_link',)
    inlines = [TagInline, ExerciseImageInline]
    search_fields = ['title', 'description', 'muscle', 'level', 'home_gym', 'category__title', 'category__description']
    list_filter = ['order','timestamp','updated']
    prepopulated_fields = {"slug" : ('title',)}
    
    readonly_fields = ['categories','live_link','timestamp', 'updated',]
    
    class Meta:
        model = Exercise
        
    def categories(self, obj):
        cat = []
        for i in obj.category_set.all():
            link = "<a href='/admin/exerciselibrary/category/"+ str(i.id) +"/'> " + i.title + "</a>"
            cat.append(link)
        return ", ".join(cat)
        
    categories.allow_tags = True
    
    def live_link(self, obj):
  
        link = "<a href='/exerciselibrary//"+ str(obj.slug) +"/'> " + obj.title + "</a>"
            
        return link
        
    live_link.allow_tags = True
    
admin.site.register(Exercise, ExerciseAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ('title',)}
    inlines = [CategoryImageInline]
    class Meta:
        model = Category
        
admin.site.register(Category, CategoryAdmin)