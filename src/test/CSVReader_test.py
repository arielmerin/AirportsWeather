import unittest

from CSVReader import Reader

class CSV_test(unittest.TestCase):

    def test_read_csv(self):
        with self.assertRaises(SystemExit) as cm:
            Reader.read_csv_file(self, "noesvalido.jpg")
        self.assertEqual(cm.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
