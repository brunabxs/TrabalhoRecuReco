#https://developers.google.com/image-search/v1/jsondevguide#json_snippets_python
#http://www.craigquiter.com/post/23892979248/download-images-from-google-image-search-python

import urllib2
import simplejson
import os

class ImageSearch:
    
    BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&userip=177.98.68.247&q=' 

    INDEX = 0
    
    @staticmethod
    def google_search(keyword):
        '''
        Utiliza a API do Google para encontrar a url de uma imagem
        @param str
        @return dict
        '''
        request = urllib2.Request(ImageSearch.BASE_URL + keyword, None, {'Referer': ''})
        response = urllib2.urlopen(request)
        results = simplejson.load(response)
        return results

    @staticmethod
    def download_image(image_url):
        '''
        Faz o download da imagem de uma dada url
        @param str
        '''
        try:
            image_name, image_extention = os.path.splitext(image_url)
            image_name = 'image' + ImageSearch.get_image_index()
            image_file = open(image_name + image_extention, "wb")
            
            image = urllib2.urlopen(image_url)
            image_file.write(image.read())
        except:
            raise ValueError('Download image error')
    
    @staticmethod
    def search(keyword):
        '''
        Faz a busca de uma imagem utilizando a API do Google e salva em disco
        @param str
        '''
        results = ImageSearch.google_search(keyword)
        results_data = results['responseData']['results']
        results_count = int(results['responseData']['cursor']['estimatedResultCount'])

        if results_count == 0:
            raise ValueError('No image found')
            
        image_url = results_data[0]['unescapedUrl']
        ImageSearch.download_image(image_url)
        
    @staticmethod
    def get_image_index():
        '''
        Retorna um indice e atualiza
        @return srt
        '''
        ImageSearch.INDEX += 1
        return str(ImageSearch.INDEX)