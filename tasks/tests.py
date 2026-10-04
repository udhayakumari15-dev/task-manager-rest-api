from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class TaskAPITests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', password='pass12345')
        self.user2 = User.objects.create_user('user2', password='pass12345')

    def test_register(self):
        r = self.client.post('/api/register/', {'username': 'new', 'password': 'pass12345'})
        self.assertEqual(r.status_code, 201)

    def test_login_returns_token(self):
        r = self.client.post('/api/login/', {'username': 'user1', 'password': 'pass12345'})
        self.assertIn('token', r.data)

    def test_tasks_need_login(self):
        r = self.client.get('/api/tasks/')
        self.assertEqual(r.status_code, 401)

    def test_create_update_delete(self):
        self.client.force_authenticate(self.user1)
        r = self.client.post('/api/tasks/', {'title': 'A'})
        self.assertEqual(r.status_code, 201)
        task_id = r.data['id']
        r = self.client.patch(f'/api/tasks/{task_id}/', {'completed': True})
        self.assertTrue(r.data['completed'])
        r = self.client.delete(f'/api/tasks/{task_id}/')
        self.assertEqual(r.status_code, 204)

    def test_user_cannot_see_others_tasks(self):
        self.client.force_authenticate(self.user1)
        self.client.post('/api/tasks/', {'title': 'Private'})
        self.client.force_authenticate(self.user2)
        r = self.client.get('/api/tasks/')
        self.assertEqual(len(r.data), 0)
