from django.db import models
from user.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    post_description = models.TextField(max_length=140, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    main_image = models.ImageField(upload_to='post_pics')
    is_recipe = models.BooleanField()
    ingredients = models.TextField(blank=True, null=True)
    recipe_description = models.TextField(blank=True, null=True)
    cooking_time = models.CharField(max_length=20, blank=True, null=True)
    likes = models.ManyToManyField(User,related_name='post_likes')
    loves = models.ManyToManyField(User,related_name='post_loves')
    drooling_faces = models.ManyToManyField(User,related_name='post_drooling_faces')

    def clean(self, *args, **kwargs):
        if (self.is_recipe and self.ingredients == None) or (self.is_recipe and self.ingredients == None) or (self.is_recipe and self.recipe_description == None) or (self.is_recipe and self.cooking_time == None):
            raise ValidationError('You need to complete the recipe fields!')
        if not self.slug:
            slug_title = slugify(self.title)
            slug_date = slugify(self.date_created)
            self.slug = f"{slug_title}-{slug_date}"
        super().clean(*args, **kwargs)
    
    class Meta:
        ordering = ('-date_created',)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug':self.slug})

    def like_count(self):
        return self.likes.count()

    def love_count(self):
        return self.loves.count()

    def droolingface_count(self):
        return self.drooling_faces.count()
    