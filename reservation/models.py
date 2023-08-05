from django.db import models

class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10,decimal_places=2) 
   inventory = models.IntegerField() 
   def __str__(self):
       return f'{self.title} : {str(self.price)}'
   
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(null=False)
    reservation_date = models.DateTimeField()
    def __str__(self): 
        return self.name
