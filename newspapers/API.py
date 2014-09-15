__author__ = 'newscred'
import requests
import settings

class NewscredApi():
    url = 'http://api.newscred.com/'
    options = {}

    def __init__(self, endpoint=None, options=None):
        self.url = '%s%s' % (self.url, endpoint)
        self.options = options
        self.options['access_key'] = settings.NEWSCRED_API_ACCESS_KEY
        self.options['format'] = 'json'

    def response(self):
        response = requests.get(self.url, params=self.options)
        return response.json()

class FlickerApi():
    url = 'https://api.flickr.com/services/rest/'
    options = {}
    def __init__( self ,options = None ):
        self.options = options
        self.options['api_key'] = settings.FLICKER_API_ACCESS_KEY
        self.options['method'] = 'flickr.photos.search'
        self.options['format'] = 'json'
        self.options['extras'] = 'url_s'
        self.options['nojsoncallback'] = True
    def response(self):
        response = requests.get(self.url,params = self.options)
        return response.json()