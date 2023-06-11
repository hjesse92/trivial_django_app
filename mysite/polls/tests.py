from django.test import TestCase, Client
from .models import Question

# Create your tests here.

class Tests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello_world(self):
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 200)

    def test_create_question(self):
        self.assertEqual(Question.objects.count(), 0)
        response = self.client.post('/api/questions/create/', {'question_text': "What is Saad's favorite ramen?"})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['message'], 'Question created successfully!')

        testquestion = Question.objects.get(pk=1)
        self.assertEqual(testquestion.question_text, "What is Saad's favorite ramen?")

    def test_get_question(self):
        response = self.client.get('/api/questions/')
        self.assertEqual(response.status_code, 200)