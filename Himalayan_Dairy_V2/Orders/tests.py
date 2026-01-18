from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from authentication.models import CustomUser
from Orders.models import MilkOrder


class OrderAPITests(APITestCase):
    def setUp(self):
        # Create a regular user
        self.user = CustomUser.objects.create_user(
            email='user@example.com',
            password='password123',
            first_name='Test',
            last_name='User',
            phone='9800000000',
        )

        # Create a staff user
        self.staff_user = CustomUser.objects.create_user(
            email='staff@example.com',
            password='password123',
            first_name='Staff',
            last_name='User',
            phone='9800000001',
            is_staff_user=True,
        )

        # Create an order for the regular user
        self.order = MilkOrder.objects.create(
            user=self.user,
            milk_type='cow',
            quantity=1.5,
        )

    def test_create_order_as_regular_user(self):
        # Get token
        url = reverse('token_obtain_pair')
        data = {'email': 'user@example.com', 'password': 'password123'}
        response = self.client.post(url, data)
        token = response.data['access']

        # Create order
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('api_orders')
        data = {'milk_type': 'buffalo', 'quantity': 2.0}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MilkOrder.objects.count(), 2)

    def test_create_order_as_staff_user(self):
        # Get token
        url = reverse('token_obtain_pair')
        data = {'email': 'staff@example.com', 'password': 'password123'}
        response = self.client.post(url, data)
        token = response.data['access']

        # Create order
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('api_orders')
        data = {'milk_type': 'cow', 'quantity': 1.0}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_orders_as_regular_user(self):
        # Get token
        url = reverse('token_obtain_pair')
        data = {'email': 'user@example.com', 'password': 'password123'}
        response = self.client.post(url, data)
        token = response.data['access']

        # Get orders
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('api_orders')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_order_status_as_staff_user(self):
        # Get token
        url = reverse('token_obtain_pair')
        data = {'email': 'staff@example.com', 'password': 'password123'}
        response = self.client.post(url, data)
        token = response.data['access']

        # Update order status
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('api_order_status_update', kwargs={'pk': self.order.pk})
        data = {'status': 'delivered'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'delivered')

    def test_update_order_status_as_regular_user(self):
        # Get token
        url = reverse('token_obtain_pair')
        data = {'email': 'user@example.com', 'password': 'password123'}
        response = self.client.post(url, data)
        token = response.data['access']

        # Update order status
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('api_order_status_update', kwargs={'pk': self.order.pk})
        data = {'status': 'delivered'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_access(self):
        url = reverse('api_orders')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)