from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete = models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True,blank=True) 

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    brand = models.CharField(max_length=100,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    price = models.FloatField(null=True,blank=False)
    product_type = models.BooleanField(default=False,null=True,blank=True)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images',null=True)

    def __str__(self):
        return self.brand
    def get_image(self):
        try:
            return self.image.url
        except:
            return ""
        

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete = models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=12,null=True,blank=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.id) 

    @property
    def get_cart_total_items(self):
        customerorder = self.customerorder_set.all()   
        # print(customerorder)  --> it will get what we have return in CustomerOrder
        total_items = sum([item.quantity for item in customerorder])
        return total_items
        
    @property
    def get_cart_total_price(self):
        customerorder = self.customerorder_set.all()   
        total_price = sum([item.product.price for item in customerorder])
        return total_price
    
    @property
    def shipping(self):
        shipping=False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.product_type == False:
                shipping = True
        return shipping

class CustomerOrder(models.Model):
    order = models.ForeignKey(Order,null=True,on_delete=models.SET_NULL,blank=True)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.brand

    # Total of price * quantity 
    @property
    def get_total(self):
        return self.product.price * self.quantity

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL,blank=True)
    order = models.ForeignKey(Order,null=True,on_delete=models.SET_NULL,blank=True)
    address= models.CharField(max_length=200,null=False)
    city= models.CharField(max_length=200,null=False)
    state= models.CharField(max_length=200,null=False)
    zipcode= models.CharField(max_length=200,null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address




