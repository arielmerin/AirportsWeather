import unittest

from CSVReader import Reader

""" Esta clase modela las pruebas para la lectura de archivos csv """
class CSV_test(unittest.TestCase):

    """ Se encarga de darle formatos inválidos de archivos para intentar cachar la excepción"""
    def test_read_csv(self):
        with self.assertRaises(SystemExit) as cm:
            Reader.read_csv_file(self, "noesvalido.jpg")
        self.assertEqual(cm.exception.code, 1)

    """Se encarga de verificar que la lectura de las cabeceras de los archivos csv estén correctas"""
    def test_read_headers(self):
        cabezera = ['origin', ' destination', ' origin_latitude', ' origin_longitude', ' destination_latitude',
                ' destination_longitude']
        example_fine = Reader.read_headers(self, "test/dataset4.csv")
        example_wrong = Reader.read_headers(self, "test/dataset5.csv")

        self.assertListEqual(cabezera, example_fine)
        self.assertFalse(cabezera == example_wrong)


    """Verifica que dadas las mismas coordenadas, sólo las lea una vez"""
    def test_read_no_repeated_coordinates(self):
        #dataset 6 tiene 3 coordenadas
        data6 = Reader.read_no_repeated_coordinates(self, "test/dataset6.csv")
        self.assertTrue(len(data6) == 3)

        #dataset 7 tiene 2 coordenadas
        data7 = Reader.read_no_repeated_coordinates(self, "test/dataset7.csv")
        self.assertTrue(len(data7) == 2)

        #dataset 8 tiene 2 coordenadas
        data8 = Reader.read_no_repeated_coordinates(self, "test/dataset8.csv")
        self.assertTrue(len(data8) == 2)

        #dataset 9 tiene una coordenada
        data9 = Reader.read_no_repeated_coordinates(self, "test/dataset9.csv")
        self.assertTrue(len(data9) == 1)



if __name__ == "__main__":
    unittest.main()
