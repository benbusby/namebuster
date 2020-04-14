from namebuster import generate, name_with_symbol
import unittest


class TestNamebuster(unittest.TestCase):
    def test_generate_list(self):
        list_results = generate('John Mango, Joe Blueberry')
        self.assertTrue(len(list_results) > 200)
        self.assertTrue('mangoj' in list_results)
        self.assertTrue('blueberry_j' in list_results)

    def test_generate_dict(self):
        dict_results = generate('https://benbusby.com', name_sep=True)
        self.assertTrue('Ben Busby' in dict_results)
        self.assertTrue('busbyb' in dict_results['Ben Busby'])
        self.assertTrue(len(dict_results['Ben Busby']) > 200)

    def test_name_symbol(self):
        name_list = ['John', 'Jane']
        symbols = ['.', '_', '-', '+']
        names_and_symbol = name_with_symbol(name_list)

        for symbol in symbols:
            self.assertTrue(name_list[0] + symbol in names_and_symbol)
            self.assertTrue(name_list[1] + symbol in names_and_symbol)

    def test_no_results(self):
        empty_results = generate('Name1, Name2')
        self.assertTrue(len(empty_results) == 0)


    def test_partial_results(self):
        partial_results = generate('John Doe, Jane Doe, JosephDoe', name_sep=True)
        self.assertTrue(len(partial_results) == 2)
        self.assertTrue('JosephDoe' not in partial_results)


if __name__ == '__main__':
    unittest.main()
