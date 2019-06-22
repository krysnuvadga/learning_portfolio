from django.test import TestCase
from .models import Link
from django.urls import reverse


class UrlShortener(TestCase):

    def test_shortens(self):

        '''Test that length of urls get shorten. The legth of the new url must be smaller than that of the original url.'''

        url = 'https://docs.google.com'
        l = Link(url=url)
        short_url = Link.shorten(l)
        self.assertLess(len(short_url), len(url))



    def test_recover_link(self):

        '''Test that the shorten url, when expanded is thesame as the original url'''

        url = 'https://docs.google.com'
        l = Link(url=url)
        short_url = Link.shorten(l)
        l.save()
        exp_url = Link.expand(short_url)
        self.assertEqual(url, exp_url)


    def test_homepage(self):

        '''Test that a home page exits and it contains a form'''

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_shorten_form(self):

        '''Test that submitting the forms returns a Link object'''

        url = 'https://docs.google.com/'
        response = self.client.post(reverse('home'), {'url': url}, follow=True)
        self.assertIn("Link", response.context)
        l = response.cotext['Link']
        short_url = Link.shorten(l)
        self.assertEqual(u)
        self.assertIn(short_url, response.content)
