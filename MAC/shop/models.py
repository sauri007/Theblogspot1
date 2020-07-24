from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=20)
    categary = models.CharField(max_length=50,default="")
    sub_categary = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="shop/static/shop/1.jpg")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70, default="")
    phone = models.IntegerField(default=+91)
    desc = models.CharField(max_length=500,default="")

    def __str__(self):
         return self.name
class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    items_JSON = models.CharField(max_length=5000)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70, default="")
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=500, default="")
    state = models.CharField(max_length=500, default="")
    phone = models.IntegerField(default=+91)
    amount = models.IntegerField(default=0)
    zip_code = models.CharField(max_length=500,default="")

    def __str__(self):
         return self.name