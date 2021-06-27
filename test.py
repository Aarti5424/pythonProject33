import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass
    def test_equal(self):
        firstValue = "Aarti"
        secondValue = "Aarti"
        # error message in case if test case got failed
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(firstValue, secondValue, message)


    def test_True(self):
        testValue = True
        # error message in case if test case got failed
        message = "Test value is not true."
        # assertTrue() to check true of test value
        self.assertTrue(testValue, message)


     # Returns true if 1 + '1' raises a TypeError

    def raises(self):
        with self.assertRaises(Exception):
            1 + '1'

    def Greater(self):
        first = 4
        second = 3

        # error message in case if test case got failed
        message = "first value is not greater that second value."

        # assert function() to check if values1 is
        # greater than value2
        self.assertGreater(first, second, message)


if __name__ == '__main__':
    unittest.main()
