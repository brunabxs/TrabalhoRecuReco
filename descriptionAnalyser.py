import string
from stemming.porter2 import stem

class DescriptionAnalyser:

    STOPWORDS = set(['a', 'about', 'above', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also','although','always','am','among', 'amongst', 'amoungst', 'amount',  'an', 'and', 'another', 'any','anyhow','anyone','anything','anyway', 'anywhere', 'are', 'around', 'as',  'at', 'back','be','became', 'because','become','becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 'bottom','but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'do', 'done', 'down', 'due', 'during', 'each', 'eg', 'eight', 'either', 'eleven','else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 'fifteen', 'fify', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'ie', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'it', 'its', 'itself', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own','part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'she', 'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the', 'their', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', 'thickv', 'thin', 'third', 'this', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves', 'the'])
    
    @staticmethod
    def remove_punctuation(text):
        '''
        Remove do documento caracteres de pontuacao
        @param str
        @return str
        '''
        return text.translate(string.maketrans("",""), string.punctuation)

    @staticmethod
    def remove_stopwords(terms):
        '''
        Filtra a lista de palavras, removendo as 'stop words' (adverbios, artigos, preposicoes etc)
        @param list<str>
        @return list<str>
        '''
        # recupera apenas as palavras que nao sao stopwords
        return filter(lambda x: x not in DescriptionAnalyser.STOPWORDS, terms)
        
    @staticmethod
    def stemming(terms):
        '''
        Retorna o radical da(s) palavra(s)
        @param str/list<str>
        @return str/list<str>
        '''
        if type(terms) == str:
            return stem(terms)
            
        if type(terms) == list:
            new_terms = list()
            for term in terms:
                new_terms.append(DescriptionAnalyser.stemming(term))
            return new_terms

    @staticmethod
    def prepare(text):
        '''
        Trata o texto, retornando os termos do mesmo
            - Converte os caracteres para minusculo
            - Remove caracteres de pontuacao
            - Separa os termos por ' '
            - Remove stop words
            - Reduz as palavras ao seu radical
        @param str
        @return list<str>
        '''
        # remove whitespaces
        # converte para caracteres minusculos
        terms = text.strip().lower()
        
        # remove caracteres de pontuacao
        terms = DescriptionAnalyser.remove_punctuation(terms)
        
        # separa as palavras por ' '
        terms = terms.split(' ')
        
        # remove '' da lista de palavras
        terms = filter(lambda word : len(word) > 0, terms)
        
        # remove stop words
        terms = DescriptionAnalyser.remove_stopwords(terms)
        
        # stemming
        terms = DescriptionAnalyser.stemming(terms)
        
        return terms
        
    def __init__(self, text):
        self.text = text.strip()
        self.__terms = DescriptionAnalyser.prepare(self.text)
        
    def terms(self):
        '''
        Termos do documento
        @return list<str>
        '''
        return self.__terms
        
    def calculate_terms_frequency(self):
        '''
        Calcula a frequencia de cada termo 
        A frequencia de um termo eh dada por:
            total_de_ocorrencias_do_termo_na_sentenca / total_de_termos_na_sentenca
        '''
        self.__terms_frequency = dict.fromkeys(self.terms(), 0.0)
        
        # ocorrencia do termo na descricao
        for term in self.terms():
            self.__terms_frequency[term] += 1
        
        # frequencia do termo na descricao
        total_terms = len(self.terms())
        for term in self.terms():
            self.__terms_frequency[term] /= total_terms
            
    def terms_frequency(self, term=None):
        '''
        Frequencia de cada termo na sentenca ou a frequencia do termo informado
        @param str (optional)
        @return dict<str, float>/float
        '''
        if term == None:
            return self.__terms_frequency
        if self.__terms_frequency.has_key(term):
            return self.__terms_frequency[term]
        else:
            return 0.0