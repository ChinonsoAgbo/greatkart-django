from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=100, unique=True) # slug is url for category and is unique
    description = models.TextField(max_length=255, blank=True) # description of the category is optional
    cat_image = models.ImageField(upload_to='category_images', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

#=================== This fun will  be profied the url for a particular slug ===============
    
    def get_url(self): # self--> creating a fun in side category
        return reverse('products_by_category', args=[self.slug]) # taking the self variable slup 



    def __str__(self):
        return self.category_name
