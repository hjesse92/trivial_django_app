from django.test import TestCase, Client
from .models import Question

# Create your tests here.

class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        q1 = Question.objects.create(question_text="test question")

    def test_create_question(self):
        self.assertEqual(Question.objects.count(), 1)
        response = self.client.post('/api/questions/create/', {'question_text': "What is Saad's favorite ramen?"})
        self.assertEqual(Question.objects.count(), 2)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['message'], 'Question created successfully!')

        testquestion = Question.objects.get(pk=2)
        self.assertEqual(testquestion.question_text, "What is Saad's favorite ramen?")

    def test_get_question(self):
        response = self.client.get('/api/questions/')
        self.assertEqual(response.status_code, 200)
