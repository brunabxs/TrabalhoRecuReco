from outputGenerator import *
import unittest

class TestOutputGeneratorMethods(unittest.TestCase):

    #def test_load_template(self):
    #    data = OutputGenerator.load_template('test/template-test-load-template.tpl')
    #    self.assertEqual(data, '<html><head></head><body></body></html>')

    def test_init(self):
        og = OutputGenerator('text',['um', 'dois', 'tres'], ['#ffffff'], ['image.jpg'], template='test/template-test-init.tpl', output='test/test-output/output-test-init.html')
        
        self.assertEqual(og.description, 'text')
        self.assertEqual(og.keywords, ['um', 'dois', 'tres'])
        self.assertEqual(og.colors, ['#ffffff'])
        self.assertEqual(og.images, ['image.jpg'])
        self.assertEqual(isinstance(og.output, Template), True)
        
    def test_save_output(self):
        og = OutputGenerator('text', ['um', 'dois', 'tres'], ['#ffffff'], ['image.jpg'], template='test/template-test-save-output.tpl', output='test/test-output/output-test-save-output.html')
        og.save_output()
        self.assertEqual(og.output, '<html><head></head><body><li>um</li><li>dois</li><li>tres</li><li style="background-color: #ffffff"></li><li><img src="image.jpg" /></li></body></html>')
        
if __name__ == '__main__':
    unittest.main()