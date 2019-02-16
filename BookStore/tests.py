from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Genre

# Create your tests here.

class GenreTesting(APITestCase):
    def test_genre(self):
        data = {'name':'Comedy', 'desc':'Funny'}
        url = reverse('genre-all')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        data = {'name': 'Emotional', 'desc': 'Sad'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Genre.objects.count(), 2)

        url = reverse('genre-single', args=['Emotional'])
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Genre.objects.get(name='Emotional').name, 'Emotionaly')
