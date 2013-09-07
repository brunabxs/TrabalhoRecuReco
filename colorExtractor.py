import random   
import math
from PIL import Image

class Point:
    
    @staticmethod
    def convert_to_hexa(color):
        '''
        Converte uma lista de inteiros numa cor em hexa
        @param list possui tres elementos que correspondem aos canais R, G, B
        @return str corno formato '#______'
        '''
        rgb = map(int, color)
        return '#%s' % ''.join(('%02x' % channel for channel in rgb))

    def __init__(self, color, count):
        '''
        Construtor
        @param list possui tres elementos que correspondem aos canais R, G, B
        @param int total de pixels com a cor
        '''
        self.color = color
        self.count = count
        
    def calculate_distance(self, point):
        '''
        Dado um ponto, retorna a distancia euclidiana
        @param Point ponto para o qual se quer calcular distancia
        @return float distancia entre os pontos
        '''
        return math.sqrt(sum([((self.color[channel] - point.color[channel]) ** 2) for channel in xrange(3)]))
        
    def find_cluster(self, clusters):
        '''
        Calcula o cluster ao qual pertence o ponto.
        A proximidade eh calculada com distancia entre o centro do cluster e o ponto em questao.
        @param list<Cluster> clusters
        @return Cluster cluster mais proximo do ponto
        '''
        nearest_cluster, smallest_distance = None, float('Inf')
        for cluster in clusters:
            distance = self.calculate_distance(cluster.center)
            if distance < smallest_distance:
                nearest_cluster, smallest_distance = cluster, distance
        return nearest_cluster

    def __str__(self):
        return Point.convert_to_hexa(self.color)
        
    def __repr__(self):
        return str(self)
        
class Cluster:
    def __init__(self, start_point):
        '''
        Construtor
        @param Point ponto inicial do cluster
        '''
        self.points = [start_point]
        self.new_points = []
        self.center = start_point
        
    def add(self, point):
        '''
        Adiciona um ponto na lista de pontos do cluster
        @param Point ponto a ser adicionado no cluster
        '''
        self.new_points.append(point)
        
    def update(self):
        '''
        Atualiza a lista de pontos do cluster e seu centro
        @return float distancia entre os centros
        '''
        self.points, self.new_points = self.new_points, []
        return self.__calculate_center()
        
    def __calculate_center(self):
        '''
        Calcula o novo centro do cluster
        @return float distancia entre os centros (atual e anterior)
        '''
        values = [0.0 for channel in xrange(3)]
        
        total_points = 0
        for point in self.points:
            total_points += point.count
            for channel in xrange(3):
                values[channel] += point.color[channel] * point.count
                
        # calcula o centro do cluster
        center = Point([(value / total_points) for value in values], 1)
        
        # calcula a variacao dos centros
        difference = self.center.calculate_distance(center)
        self.center = center
        
        return difference
        
    def __str__(self):
        return str(self.center)
        
    def __repr__(self):
        return str(self)

class ColorExtractor:
    def __init__(self, image_filename, total_clusters=3, min_difference=0.001):
        '''
        Construtor
        @param str nome do arquivo da imagem
        @param int (opcional) total de clusters
        @param float (opcional) erro minimo para se encerrar a procura de clusters
        '''
        self.image = Image.open(image_filename)
        self.image.thumbnail((200, 200))
        self.total_clusters = total_clusters
        self.min_difference = min_difference
        
    def __get_points(self):
        '''
        Recupera o conjunto de cores da imagem e o total de pixels na imagem com a cor
        @param Image imagem a ser analisada
        @return list<Point> lista de pontos extraidos da imagem
        '''
        points = []
        width, height = self.image.size

        for count, color in self.image.getcolors(width * height):
            points.append(Point(color, count))
        
        return points
    
    def __kmeans(self, points, total_clusters, min_difference):
        '''
        Separa os pontos em grupos (clusters)
        @param list<Point> lista de pontos para agrupamento
        @param int total de clusters
        @param float erro minimo para encerrar o algoritmo
        '''
        # recupera um conjunto de amostras aleatorias de pontos e cria os clusters
        clusters = [Cluster(point) for point in random.sample(points, total_clusters)]

        while True:
            # insere um ponto na lista de pontos do cluster correspondente
            for point in points:
                cluster = point.find_cluster(clusters)
                cluster.add(point)

            # atualiza os pontos do cluster
            # recalcula o centro
            # verifica a variacao dos centros
            max_difference = 0
            for cluster in clusters:
                difference = cluster.update()
                max_difference = max(max_difference, difference)
                
            if max_difference < min_difference:
                break

        return clusters
        
    def extract_colors(self):
        '''
        Extrai os clusters de cores da imagem
        @return list<Cluster> clusters encontrados
        '''
        points = self.__get_points()
        clusters = self.__kmeans(points, self.total_clusters, self.min_difference)
        return clusters