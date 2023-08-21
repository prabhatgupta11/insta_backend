from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class PostTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_post(self):
        url = reverse('post-list')
        data = {'username': 'user1', 'caption': 'My first post'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'user1')
        self.assertEqual(response.data['caption'], 'My first post')

    def test_view_posts(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # No posts initially

    def test_delete_existing_post(self):
        # Create a post
        url = reverse('post-list')
        data = {'username': 'user1', 'caption': 'My post'}
        response = self.client.post(url, data, format='json')
        post_id = response.data['id']

        # Delete the post
        delete_url = reverse('post-detail', args=[post_id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_nonexistent_post(self):
        delete_url = reverse('post-detail', args=[999])  # Nonexistent post ID
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
