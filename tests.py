from django.test import SimpleTestCase


class Simpletests(SimpleTestCase):
    def test_home_page(self):
        responce = self.client.get('/')
        self.assertEqual(responce.status_code, 200)

    def test_about_page(self):
        responce = self.client.get('/about/')
        self.assertEqual(responce.status_code, 200)