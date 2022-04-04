from django.db import models

class TimeStampModel(models.Model):    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # managed = True
        abstract = True

class Seed(TimeStampModel):
    seed_name = models.CharField(max_length=255)
    seed_description = models.TextField(null=True,blank=True)
    server_ip = models.GenericIPAddressField()
    class Meta:
        ordering = ['-id',]

class Product(TimeStampModel):
    prod_name = models.CharField(max_length=255)
    prod_description = models.TextField(null=True,blank=True)
    prod_ip = models.GenericIPAddressField()

    class meta:
        ordering = ['-id',]

    def __str__(self):
        return self.prod_name

class Image(TimeStampModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    large_img = models.ImageField(upload_to="media/img/large", default='1',null=True, blank=True)
    thumb_img = models.ImageField(upload_to="media/img/thumb", default='1',null=True, blank=True)      
    small_img = models.ImageField(upload_to="media/img/small", default='1',null=True, blank=True)

    class meta:
        ordering = ['-id',]