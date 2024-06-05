from django.db import models

# Create your models here.






class Owner(models.Model):
    name=models.CharField(max_length=300,blank=True,null=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name=models.CharField(max_length=300)

    def __str__(self):
        return self.name


# car=Car.objects.filter(id=1)
# car.owner
# owner=Owner.objects.filter(id=1)
# owner.car_set.model
# owner.cars.model



class Car(models.Model):
    owner=models.OneToOneField(Owner,on_delete=models.CASCADE,related_name='cars')
    brand=models.CharField(max_length=300)
    model=models.CharField(max_length=300)
    gallery=models.ForeignKey(Gallery,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.brand}-------{self.model}"


    


    







