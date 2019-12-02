from django.urls import reverse, resolve

class TestUrls:

    def test_list_url(self):
        path = reverse('cancion_list', {})
        assert resilve(path).view_name == 'cancion_list'
