#http://www.colourlovers.com/api

import urllib2
import simplejson
import os

class PaletteSearch:
    
    BASE_URL = 'http://www.colourlovers.com/api/palettes?format=json&hex=' 

    @staticmethod
    def colourlover_search(color, total_palettes):
        '''
        Utiliza a API do COLOURLover para encontrar paletas de cores
        @param lits<str> cores
        @param int total paletas
        @return dict resultado da consulta no colourlover (ver referencias)
        '''
        request = urllib2.Request(PaletteSearch.BASE_URL + color + '&numResults=' + str(total_palettes))
        request.add_header('User-Agent', 'Mozilla/5.0')
        response = urllib2.urlopen(request)
        results = simplejson.load(response)
        return results

    @staticmethod
    def search(colors, total_palettes=1):
        '''
        @param list<str> cores no formato hexadecimal
        @param int (opcional) total de paletas por cor
        @return list<dict>>
        '''
        print colors
        palettes = list()
        for color in colors:
            results = PaletteSearch.colourlover_search(color, total_palettes)
            for result in results:
                palettes.append({'color': '#'+color, 'palette_colors': ['#' + c for c in result['colors']], 'palette_name': result['title']})
        return palettes