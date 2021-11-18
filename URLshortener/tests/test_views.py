from django.test import Client, TestCase

from URLshortener.models import Shortener


# Set of tests for checking 'create_short_URL' function
class CreateShortURLViewTest(TestCase):

    # Check creating with correct input information
    def test_successful_creating_short_URL(self):
        client = Client()
        context = {
            'url': 'https://ravkavonline.co.il/he/'
        }
        response = client.post('/create', context)

        self.assertEqual(response.status_code, 201)

    # Check creating with wrong input information
    def test_wrong_creating_short_URL(self):
        client = Client()
        context = {
            'url': 'It_is_not_URL'
        }
        response = client.post('/create', context)

        self.assertEqual(response.status_code, 400)


# Set of tests for checking 'redirect_from_short_to_long_URL' function
class RedirectFromShortToLongURLViewTest(TestCase):

    def setUp(self):
        self.test_shortener = Shortener.objects.create(url='https://www.youtube.com/')

    # Check redirecting with correct request
    def test_successful_redirecting_from_short_to_long_URL(self):
        client = Client()
        response = client.get('/s/{0}'.format(self.test_shortener.short_url))

        self.assertEqual(response.get('location'), 'https://www.youtube.com/')
        self.assertEqual(response.status_code, 302)

    # Check redirecting with wrong request
    def test_wrong_redirecting_from_short_to_long_URL(self):
        client = Client()
        response = client.get('/s/1{0}'.format(self.test_shortener.short_url))

        self.assertNotEqual(response.get('location'), 'https://www.youtube.com/')
        self.assertEqual(response.status_code, 404)
