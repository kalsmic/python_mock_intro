# test_main.py
from unittest import TestCase, main, mock
from main import double, add_two_doubled_values, get_two_doubled_values, add_two


class MainTestCase(TestCase):
    def test_double(self):
        result = double(9)
        expected = 18
        self.assertEqual(expected, result)

    def test_add_two_doubled_values(self):
        result = add_two_doubled_values()
        expected = 10
        self.assertEqual(expected, result)


    def test_add_two_doubled_mocked_return_value(self):
        with mock.patch('main.double', return_value=10):
            result = add_two_doubled_values()
            expected = 20
            self.assertEqual(expected, result)

    def test_add_two_doubled_mocked_side_effect(self):
        with mock.patch('main.double', side_effect = [7,10]):
            result = add_two_doubled_values()
            expected = 17
            self.assertEqual(expected, result)

    def test_get_two_doubled_mocked_side_effect(self):
        with mock.patch('main.double', side_effect= [7,10]):
            result = get_two_doubled_values()
            expected = [7,10]
            self.assertEqual(expected[0], result[0])
            self.assertEqual(expected[1], result[1])

    def test_add_two_mocked_side_effect(self):
        with mock.patch('builtins.input', side_effect= [7,10]):
            result = add_two()
            expected = 17
            self.assertEqual(expected, result)

    def test_add_two_mocked_return_value(self):
        with mock.patch('builtins.input', return_value=10):
            result = add_two()
            expected = 20
            self.assertEqual(expected, result)




if __name__ == "__main__":
    main()