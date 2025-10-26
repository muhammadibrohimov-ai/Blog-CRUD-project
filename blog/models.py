from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    slug = models.SlugField(max_length=220, unique=True)
    main_image = models.FileField(upload_to='post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False, editable=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            
            slug = base_slug
            num = 1
            
            while Post.objects.filter(slug = slug).exists():
                slug = f'{base_slug}-{num}'
                num += 1
                
            self.slug = slug                
                
        return super().save(*args, **kwargs)
    
    
    def delete(self, *args, **kwargs):
        
        self.is_delete = True
        
        self.save()
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-updated_at',)
        
        
class Images(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ('-created_at',)