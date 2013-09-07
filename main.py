import webbrowser
from descriptionAnalyser import DescriptionAnalyser
from imageSearch import ImageSearch
from colorExtractor import ColorExtractor
from outputGenerator import OutputGenerator

# captura a descricao
description = raw_input('Descricao:\n')

# extrai palavras-chave
analysis = DescriptionAnalyser(description)
analysis.calculate_terms_frequency()
keywords = analysis.terms()

print 'Encontrados os termos-chave...'
print keywords
print '-' * 20, '\n'

# download de imagens individuais
files = []
for keyword in keywords:
    files += ImageSearch.search(keyword)
    
print 'Imagens capturadas. Total de %d imagens...' % len(files)
print files
print '-' * 20, '\n'
    
# analise das cores
clusters = []
for file in files:    
    colorExtractor = ColorExtractor(file, 5)
    clusters += colorExtractor.extract_colors()
colors = map(str, clusters)
    
print 'Imagens analisadas. Cores coletadas...'
print colors
print '-' * 20, '\n'
    
# geracao da saida    
og = OutputGenerator(description, keywords, colors, files, template='template.tpl', output='output.html')
og.save_output()

# browser para abrir arquivo
webbrowser.open_new('output.html')