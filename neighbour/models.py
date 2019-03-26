from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Neighbourhood(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=20)
    occupants=models.CharField(max_length=30)
    member = models.ForeignKey(User)

    def __str__(self):
        return self.name

    @classmethod
    def create_neighborhood(self):
        self.create()

    @classmethod
    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neigborhood(self):
        self.remove()

    @classmethod
    def update_neighbourhood(self):
        self.update()

    @classmethod
    def update_occupants(self,occupants):
        self.update()

    @classmethod
    def search_by_name(cls,search_term):
        neighborhood=cls.objects.filter(name__icontains=search_term)
        return neighborhood    

class Profile(models.Model):
    user = models.OneToOneField(User)
    name=models.CharField(max_length=30)
    neighbourhood=models.ForeignKey(Neighbourhood)
    profile = models.ImageField(upload_to='images')
    email=models.EmailField()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.save()

class Business(models.Model):
    name = models.CharField(max_length=1000)
    user = models.ForeignKey(User)
    img = models.ImageField(upload_to='business')
    neighbour = models.ForeignKey(Neighbourhood)
    email = models.EmailField()

    @classmethod
    def create_business(self):
        self.save()

    @classmethod
    def delete_business(self):
        self.remove()

    @classmethod
    def find_business(business_id):
        db.session.filter(business_id)

    @classmethod
    def update_business(self):
        self.update()


class Events(models.Model):
    eventname=models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    image=models.ImageField(upload_to = 'events')
    date=models.DateField()

    @classmethod
    def create_event(self):
        self.save()

    @classmethod
    def delete_event(self):
        self.remove()

    @classmethod
    def find_event(business_id):
        db.session.filter(business_id)

    @classmethod
    def update_event(self):
        self.update()

class Contacts(models.Model):
    medical=models.CharField(max_length=20)
    location = models.ForeignKey(Neighbourhood)
    police = models.CharField(max_length=30)
