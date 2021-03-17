from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField( max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    category=models.CharField(max_length=20,default="")
    subCategory=models.CharField(max_length=20,default="")
    Price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="shop/imgaes",default="")
    
    def __str__(self) -> str:
        return self.product_name


class Contact(models.Model):
    personId=models.AutoField(primary_key=True)
    Name=models.CharField( max_length=50,default="")
    Email=models.CharField(max_length=20,default="")
    Phone=models.IntegerField(default="")
    Message=models.CharField(max_length=50,default=123)

    def __str__(self) -> str:
        return self.Name


class Order(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField( max_length=50,default="")
    Email=models.CharField(max_length=20,default="")
    Phone=models.CharField(max_length=21, default="")
    Address=models.CharField(max_length=300,default="")
    State=models.CharField(max_length=50,default="")
    City=models.CharField(max_length=20)
    Pincode=models.IntegerField(default=0000)


    def __str__(self) -> str:
        return self.Name

class OrderUpdate(models.Model):
    Order_id=models.IntegerField(default=0)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    Order_update=models.CharField(max_length=500,default="")
    Cart_item=models.CharField(max_length=500,default="")
    Email=models.CharField(max_length=100,default="")

    def __str__(self) -> str:
        return self.Email
