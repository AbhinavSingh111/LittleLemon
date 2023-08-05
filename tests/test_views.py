from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from reservation.models import Menu,Booking
from reservation.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Create a few test instances of the Menu model
        self.menu1 = Menu.objects.create(id="1",title="IceCream", price=80, inventory=100)
        self.menu2 = Menu.objects.create(id="2",title="Choclate", price=40, inventory=10)
        self.menu3 = Menu.objects.create(id="3",title="Cake", price=80, inventory=10)

    def test_getall(self):
        # Retrieve all the Menu objects in the database
        expected_data = MenuSerializer([self.menu1, self.menu2, self.menu3], many=True).data
    

        # Initialize the Django REST framework APIClient
        client = APIClient()

        # Define the URL for the Menu list view
        url = reverse('menu-list')

        # Send a GET request to the view
        response = client.get(url)

        

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the serialized data in the response equals the expected serialized data
        self.assertEqual(response.data, expected_data)
        