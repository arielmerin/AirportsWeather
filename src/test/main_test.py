import unittest

# from test.Weather_test import Weather_test
from test.CSVReader_test import CSV_test

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    # suite.addTest(loader.loadTestsFromModule(Weather_test))
    suite.addTest(loader.loadTestsFromModule(CSV_test))
    runner = unittest.TextTestRunner(verbosity=3)
    resultados = runner.run(suite)
