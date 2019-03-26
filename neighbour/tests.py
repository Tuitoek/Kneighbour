from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

# Create your tests here.
class NeighhbourhoodTestClass(TestCase):
    def setUp(self):
        self.new_name = Neighbourhood(name='Rongai')
        self.new_location=Neighbourhood(location='Kajiado')
        self.member = User.objects.create(member='Sarah')
        self.new_occupants = Neighbourhood(occupants='3')
        self.neighbourhood=Neighbourhood(name='Test',location=self.new_location,occupants=self.mew_occupants,member=self.user)
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbour,Neighbourhood))

    def test_save_neighbourhood(self):
        self.neighbour.save_neighbourhood()
        neighbourhoods=Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods)>0)

    def test_delete_neighbourhood(self):
        self.neighbour.save_neighbourhood()
        self.neighbour.delete_neighbourhood()
        neighbourhoods=Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods)==0)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='test',password="testpassword")
        self.new_neighbour=Neighbourhood.objects.create("Test")
        self.new_business=Business(name="test",email='s@gmail.com',img="black.jpg",neighbour=new_neighbour)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))

    def test_save_business(self):
        self.new_business.save_biz()
        business=Business.objects.all()
        self.assertTrue(len(business)>0)

    def test_delete_business(self):
        self.new_business.save_biz()

        self.new_business.delete_business()
        business=Business.objects.all()
        self.assertTrue(len(buisness)==0)

class ProfileTestCase(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='testpassword')
        self.new_neighbourhood = Neighbourhood.objects,create_neighbourhood(neighbourhood="Rongai")
        self.new_profile = Profile(user=self.new_user,profile='black.jpeg',email='user@gmail.com',neighbourhood=new_neighbourhood)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_profile(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)
