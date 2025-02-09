from django.db import models
from django.contrib.auth.models import User

class User_details(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number=models.IntegerField()
    address=models.TextField()
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.user_id

class Hall(models.Model):
    name=models.CharField(max_length=100)
    location=models.TextField()
    capacity=models.IntegerField()
    price_per_day=models.DecimalField(max_digits=10,decimal_places=2)
    photo_url=models.FileField()
    description=models.TextField()
    def __str__(self):
        return self.name


class Food(models.Model):
    food_image=models.FileField()
    food_name=models.CharField(max_length=100)
    food_price=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.food_name

class Decoration(models.Model):
    decoration_image=models.FileField()
    decoration_name=models.CharField(max_length=200,null=True,blank=True)
    decoration_price=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.decoration_name

class Booking(models.Model):
    hall_id=models.ForeignKey(Hall,on_delete=models.CASCADE)
    customer_id=models.ForeignKey(User,on_delete=models.CASCADE)
    booking_date=models.DateField(auto_now_add=True)
    payment_status=models.CharField(max_length=20,default='pending',null=True,blank=True)
    include_photography=models.BooleanField(null=True,blank=True)
    include_food=models.BooleanField(null=True,blank=True)
    food=models.ForeignKey(Food,on_delete=models.CASCADE,null=True,blank=True)
    include_decoration=models.BooleanField(null=True,blank=True)
    decoration_model=models.ForeignKey(Decoration,on_delete=models.CASCADE,null=True,blank=True)
    photography_cost=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,default=1000)
    suggestion=models.CharField(max_length=250,null=True,blank=True)
    total_cost=models.DecimalField(max_digits=10,decimal_places=2)
    event_date=models.DateField(null=True,blank=True)
    status=models.CharField(max_length=20,default='pending',null=True,blank=True)
    number=models.IntegerField(null=True,blank=True)

   


    


