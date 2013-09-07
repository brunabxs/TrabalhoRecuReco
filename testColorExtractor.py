from colorExtractor import *
import unittest

class TestColorExtractorMethods(unittest.TestCase):

    def test_cluster_init(self):
        point = Point([255, 255, 255], 5)
        cluster = Cluster(point)
        
        self.assertEqual(len(cluster.points), 1)
        self.assertEqual(cluster.points[0], point)
        self.assertEqual(len(cluster.new_points), 0)
        self.assertEqual(cluster.center, point)
        
    def test_cluster_add(self):
        points = [Point([255, 255, 255], 5), Point([0, 0, 0], 2)]
        cluster = Cluster(points[0])
        cluster.add(points[1])
        
        self.assertEqual(len(cluster.points), 1)
        self.assertEqual(cluster.points[0], points[0])
        self.assertEqual(len(cluster.new_points), 1)
        self.assertEqual(cluster.new_points[0], points[1])
        self.assertEqual(cluster.center, points[0])
        
    def test_cluster_update(self):
        points = [Point([255, 255, 255], 2), Point([0, 0, 0], 2), Point([128, 128, 128], 1)]
        cluster = Cluster(points[0])
        cluster.add(points[1])
        cluster.add(points[2])
        diff = cluster.update();
        
        self.assertEqual(len(cluster.points), 2)
        self.assertEqual(cluster.points[0], points[1])
        self.assertEqual(cluster.points[1], points[2])
        self.assertEqual(len(cluster.new_points), 0)
        self.assertAlmostEqual(cluster.center.color[0], 42.6666666, delta=0.000001)
        self.assertAlmostEqual(cluster.center.color[1], 42.6666666, delta=0.000001)
        self.assertAlmostEqual(cluster.center.color[2], 42.6666666, delta=0.000001)
        self.assertEqual(cluster.center.count, 1)
        
    def test_point_init(self):
        point = Point([128, 128, 128], 1)
        
        self.assertEqual(point.color[0], 128)
        self.assertEqual(point.color[1], 128)
        self.assertEqual(point.color[2], 128)
        self.assertEqual(point.count, 1)
    
    def test_point_find_cluster(self):
        points = [Point([255, 255, 255], 5), Point([0, 0, 0], 2)]
        cluster1 = Cluster(points[0])
        cluster2 = Cluster(points[1])
        clusters = [cluster1, cluster2]
        point1 = Point([128, 128, 128], 1)
        point2 = Point([30, 30, 30], 1)
        
        self.assertEqual(point1.find_cluster(clusters), cluster1)
        self.assertEqual(point2.find_cluster(clusters), cluster2)
        
    def test_point_calculate_distance(self):
        point1 = Point([255, 255, 255], 3)
        point2 = Point([255, 255, 255], 3)
        point3 = Point([0, 0, 0], 3)
        
        distance12 = point1.calculate_distance(point2)
        self.assertAlmostEqual(distance12, 0.0, delta=0.000001)
        
        distance13 = point1.calculate_distance(point3)
        self.assertAlmostEqual(distance13, 441.6729559, delta=0.000001)
        
    def test_point_convert_to_hexa(self):
        self.assertEqual(Point.convert_to_hexa([255, 255, 255]), '#ffffff')
        self.assertEqual(Point.convert_to_hexa([255, 0, 0]), '#ff0000')
        self.assertEqual(Point.convert_to_hexa([128, 0, 2]), '#800002')

if __name__ == '__main__':
    unittest.main()