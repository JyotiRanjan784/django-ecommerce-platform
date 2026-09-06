from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
   # product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='')
    subcategory = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    desc = models.TextField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images/', default="")


    def __str__(self):
        return self.product_name


class Contact(models.Model):
        msg_id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        email = models.EmailField(max_length=70, blank=True)
        phone = models.CharField(max_length=15, blank=True)
        desc = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.TextField()
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=15, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)

    razorpay_order_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    razorpay_payment_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    razorpay_signature = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    payment_status = models.CharField(
        max_length=20,
        default='Pending'
    )

    paid = models.BooleanField(default=False)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    update_desc = models.CharField(max_length=5000, default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[:7] + "..." if self.update_desc else "No Update"