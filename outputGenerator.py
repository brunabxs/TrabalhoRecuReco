from string import Template

class OutputGenerator:
    @staticmethod
    def load_template(filename):
        '''
        Carrega um arquivo de template
        @return Template conteudo do arquivo
        '''
        template = open(filename, 'r')
        data = ''.join(template.readlines())
        template.close()
        return Template(data)
        
    def __init__(self, description, keywords, colors, images, template='template.tpl', output='home.html'):
        '''
        Construtor
        @param str descricao
        @param list palavras-chave
        @param list cores
        @param list imagens
        @param str (opcional) nome do arquivo de template
        @param str (opcional) nome do arquivo de saida
        '''
        self.description = description
        self.keywords = keywords
        self.colors = colors
        self.images = images
        self.output = OutputGenerator.load_template(template)
        self.output_file = output
        
    def save_output(self):
        '''
        Salva num arquivo os dados de palavras-chave, imagens e cores
        '''
        # constroi dicionario com valores
        keywords = ['<li>%s</li>' % keyword for keyword in self.keywords]
        colors = ['<li style="background-color: %s"></li>' % color for color in self.colors]
        images = ['<li><img src="%s" /></li>' % image for image in self.images]
        
        # carrega valores na estrutura
        self.output = self.output.safe_substitute({'description': self.description, 'keywords' : ''.join(keywords), 'colors' : ''.join(colors), 'images' : ''.join(images)})
        
        # salva arquivo
        output = open(self.output_file, 'w')
        output.write(self.output)
        output.close()
        
        