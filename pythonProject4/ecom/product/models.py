from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
# Create your models here.
class Category(MPTTModel):
    STATUS =(
        ('True','Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=255)
    descriptionT = models.DateTimeField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS)

    slug=models.SlugField(blank=True,max_length=255)
    parent=TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    create_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by =['title']

    def __str__(self):  #içi içe kategori oluşturmak için yapıldı. görünüm olarak iç içe gözükmesi için
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '>>'.join(full_path[::-1])




class Product(models.Model):
    STATUS =(
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)#ilişkisel kategori tablosu
    title = models.CharField(max_length=255)#marka
    keyword = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    puan=  models.FloatField()
    amount = RichTextUploadingField()
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




   # def image_tag(self):
       # return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    #image_tag.short_description = 'Image'

class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


