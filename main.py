import webbrowser
import myconfig
from descriptionAnalyser import DescriptionAnalyser
from imageSearch import ImageSearch
from paletteSearch import PaletteSearch
from colorExtractor import ColorExtractor
from outputGenerator import OutputGenerator

# captura a descricao
description = raw_input('Descricao:\n')

# extrai palavras-chave
analysis = DescriptionAnalyser(description)
analysis.calculate_terms_frequency()
terms = set(analysis.terms())
keywords = analysis.most_frequent_terms(myconfig.most_frequent_terms)

print 'Encontrados os termos-chave...'
print terms
print '-' * 20, '\n'
print 'Termos mais frequentes...'
print keywords
print '-' * 20, '\n'

if myconfig.search_images_per_keyword:
    # download de imagens individuais
    files = []
    for keyword in keywords:
        files += ImageSearch.search(keyword, myconfig.images_dir, myconfig.total_images_per_keyword)
else:        
    files = ImageSearch.search(' '.join(keywords), myconfig.images_dir, myconfig.total_images)

print 'Imagens capturadas. Total de %d imagens...' % len(files)
print files
print '-' * 20, '\n'
    
# analise das cores
clusters = []
for file in files:    
    colorExtractor = ColorExtractor(file, myconfig.total_colors_per_image)
    clusters += colorExtractor.extract_colors()
colors = map(str, clusters)
    
print 'Imagens analisadas. Cores coletadas...'
print colors
print '-' * 20, '\n'

# paletas
palettes = PaletteSearch.search([color[1:] for color in colors], myconfig.total_palettes_per_color)
    
print 'Corea analisadas. Paletas coletadas...'
print palettes
print '-' * 20, '\n'
    
# geracao da saida    
og = OutputGenerator(description, keywords, colors, palettes, files, template='template.tpl', output='output.html')
og.save_output()

# browser para abrir arquivo
webbrowser.open_new('output.html')