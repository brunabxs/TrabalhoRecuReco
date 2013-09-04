from descriptionAnalyser import DescriptionAnalyser
from imageSearch import ImageSearch

# captura a descricao
description = raw_input('Descricao:\n')

# extrai palavras-chave
analysis = DescriptionAnalyser(description)
analysis.calculate_terms_frequency()

# download de imagens individuais
for term in analysis.terms():
    ImageSearch.search(term)


