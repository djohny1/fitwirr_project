from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


LEVEL_CHOICES = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
    
)

HOMEGYM_CHOICES = (
    ('home', 'Home'),
    ('gym', 'Gym'),
    ('Gym or Home', 'Gym or Home'),
    
)

class ActiveExerciseManager(models.Manager):
    def get_query_set(self):
        return super(ActiveExerciseManager, self).get_query_set().filter(active=True)



class Exercise(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=120, null=False, blank=True)
    description = models.CharField(max_length=500)
    meta_keywords = models.CharField('Meta keywords', max_length=255, null=True, blank=True,
                                     help_text='Comma-delimited set SEO keywords for meta tag')
    meta_description = models.CharField('Meta Description', max_length=255, null=True, blank=True,
                                    help_text='Content for Description  meta tag')
    muscle = models.CharField(max_length=200, null=True, blank=True)
    equipments = models.CharField(max_length=15, null=True, blank=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    home_gym = models.CharField(max_length=20, choices=HOMEGYM_CHOICES)
    weight = models.CharField(max_length=15, null=True, blank=True)
    reps = models.CharField(max_length=20, null=True, blank=True)
    sets = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField()
    order = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    
    objects = models.Manager()
    active_objects = ActiveExerciseManager()
    tags = TaggableManager()
    
    def __unicode__(self,):
        return str(self.title)
    class Meta:
        ordering = ['-order']
        
    @models.permalink
    def get_absolute_url(self):
        return ('exerciselibrary_exercise', (), { 'slug' : self.slug })     
        
   
class ExerciseImageManager(models.Manager):
    """
    manager class for ExerciseImageManager
    """ 

    def like_or_dislike_exercise_image(self, user, exercise_image):
        if UserLikeExerciseImage.objects.filter(user=user, exercise_image=exercise_image).count() > 0:
            try:
                exercise_images = UserLikeExerciseImage.objects.filter(user=user, exercise_image=exercise_image)
                count = exercise_images.count()
                exercise_images.delete()
                
                if count > 0:
                    exercise_image.like_count = exercise_image.like_count - count
                    exercise_image.save(update_fields=["like_count"])
                
                return ("like", exercise_image.like_count)
            except Exception, e:
                print e
                raise e
        else:
            user_like = UserLikeExerciseImage()
            user_like.user = user
            user_like.exercise_image = exercise_image
            user_like.save()
            
            # Increase the total like count
            exercise_image.like_count = exercise_image.like_count + 1
            exercise_image.save(update_fields=["like_count"])
            
            return ("dislike", exercise_image.like_count)
    
    
class ExerciseImage(models.Model):
    exercise = models.ForeignKey(Exercise)
    image = models.ImageField(upload_to='exercises/image/')
    title = models.CharField(max_length=120, null=True, blank=True)
    featured_image = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    objects = ExerciseImageManager()
    
    def __unicode__(self,):
        return str(self.title)
    
    

class UserLikeExerciseImage(models.Model):
    exercise_image = models.ForeignKey(ExerciseImage)
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)   
    
    
    
    
    
class Tag(models.Model):
    exercise = models.ForeignKey(Exercise)
    tag = models.CharField(max_length=25)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self,):
        return str(self.tag)
    
class ActiveCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set().filter(active=True)

class Category(models.Model):
    exercises = models.ManyToManyField(Exercise)
    title = models.CharField(max_length=120)
    meta_keywords = models.CharField('Meta keywords', max_length=255, null=True, blank=True,
                                     help_text='Comma-delimited set SEO keywords for meta tag')
    meta_description = models.CharField('Meta Description', max_length=255, null=True, blank=True,
                                    help_text='Content for Description  meta tag')
    description = models.CharField(max_length=500)
    slug = models.SlugField()
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = models.Manager()
    active_objects = ActiveCategoryManager()

    
    def __unicode__(self,):
        return str(self.title)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    @models.permalink
    def get_absolute_url(self):
        return ('exerciselibrary_category', (), { 'slug' : self.slug })
    
class CategoryImage(models.Model):
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='exercises/image/')
    title = models.CharField(max_length=120, null=True, blank=True)
    featured_image = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self,):
        return str(self.title)
    
        class Meta:
            verbose_name = "Category Image"
            verbose_name_plural = "Categories Images"
    

class ExerciseSearch(models.Model):
    q = models.CharField(max_length=50)
    exercise = models.ForeignKey(Exercise)
    search_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.IPAddressField()
    user = models.ForeignKey(User, null=True)
    
    def __unicode__(self,):
        return str(self.q)   