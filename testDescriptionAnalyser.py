from descriptionAnalyser import *
import unittest

class TestDescriptionAnalyserMethods(unittest.TestCase):

    def test_remove_punctuation(self):
        new_description_analyser = DescriptionAnalyser.remove_punctuation('Wireless, Network System with Autonomous Antenna! Actuator; Control; for; Disaster... Information?')
        self.assertEqual(new_description_analyser, 'Wireless Network System with Autonomous Antenna Actuator Control for Disaster Information')
        
    def test_remove_stop_words(self):
        new_description_analyser = DescriptionAnalyser.remove_stopwords(['Wireless', 'Network', 'System', 'with', 'Autonomous', 'Antenna', 'Actuator', 'Control', 'for', 'Disaster', 'Information'])
        self.assertEqual(len(new_description_analyser), 9)
        self.assertEqual(new_description_analyser, ['Wireless', 'Network', 'System', 'Autonomous', 'Antenna', 'Actuator', 'Control', 'Disaster', 'Information'])
        
    def test_stemming_word(self):
        new_description_analyser = DescriptionAnalyser.stemming('Information')
        self.assertEqual(new_description_analyser, 'Informat')
        
    def test_stemming_words(self):
        new_description_analyser = DescriptionAnalyser.stemming(['Autonomous', 'Information', 'information'])
        self.assertEqual(new_description_analyser, ['Autonom', 'Informat', 'inform'])

    def test_prepare(self):
        new_description_analyser = DescriptionAnalyser.prepare('Wireless Network System with Autonomous Antenna Actuator Control for Disaster Information.')
        self.assertEqual(len(new_description_analyser), 8)
        self.assertEqual(new_description_analyser, ['wireless', 'network', 'autonom', 'antenna', 'actuat', 'control', 'disast', 'inform'])
        
    def test_prepare_multiple_whitespaces(self):
        new_description_analyser = DescriptionAnalyser.prepare('Wireless     Network System with   Autonomous Antenna    Actuator Control for Disaster Information.')
        self.assertEqual(len(new_description_analyser), 8)
        self.assertEqual(new_description_analyser, ['wireless', 'network', 'autonom', 'antenna', 'actuat', 'control', 'disast', 'inform'])

    def test_new_description_analyser(self):
        description_analyser = DescriptionAnalyser('A novel technique for optimising the harmonics and reactive power under nonsinusoidal voltage conditions.\n')
        self.assertEqual(description_analyser.text, 'A novel technique for optimising the harmonics and reactive power under nonsinusoidal voltage conditions.')
        
    def test_terms(self):
        description_analyser = DescriptionAnalyser('A novel technique for optimising the harmonics and reactive power under nonsinusoidal voltage conditions.')
        terms = description_analyser.terms()
        self.assertEqual(len(terms), 9)
        self.assertEqual(terms, ['novel', 'techniqu', 'optimis', 'harmon', 'reactiv', 'power', 'nonsinusoid', 'voltag', 'condit'])
        
    def test_calculate_terms_frequency(self):
        description_analyser = DescriptionAnalyser('A novel technique for optimising the harmonics and reactive power under nonsinusoidal voltage conditions.')
        description_analyser.calculate_terms_frequency()
        terms_freq = description_analyser.terms_frequency()
        
        terms = ['novel', 'techniqu', 'optimis', 'harmon', 'reactiv', 'power', 'nonsinusoid', 'voltag', 'condit']
        terms.sort()
        terms_freq_keys = terms_freq.keys()
        terms_freq_keys.sort()
        self.assertEqual(terms_freq_keys, terms)
        
        for term in terms:
            self.assertEqual(type(terms_freq[term]), float)
            self.assertAlmostEqual(terms_freq[term], 1.0/9.0, delta=0.000001)
            
    def test_terms_frequency(self):
        description_analyser = DescriptionAnalyser('A novel technique for optimising the harmonics and reactive power under nonsinusoidal voltage conditions.')
        description_analyser.calculate_terms_frequency()
        self.assertEqual(type(description_analyser.terms_frequency()), dict)
        self.assertEqual(type(description_analyser.terms_frequency('term')), float)
        self.assertAlmostEqual(description_analyser.terms_frequency('novel'), 1.0/9.0, delta=0.000001)
        self.assertAlmostEqual(description_analyser.terms_frequency('harmony'), 0.0, delta=0.000001)

if __name__ == '__main__':
    unittest.main()