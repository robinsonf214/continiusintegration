import unittest
from fibonacci import calculateFibonacci

class TestFibonacci(unittest.TestCase):
    def test_calculateFibonacci_case_n_negative(self):
        result = calculateFibonacci(-5)
        self.assertEqual(result, 0)

    def test_calculateFibonacci_case_n_0(self):
        result = calculateFibonacci(0)
        self.assertEqual(result, 0)

    def test_calculateFibonacci_case_n_1(self):
        result = calculateFibonacci(1)
        self.assertEqual(result, 1)

    def test_calculateFibonacci_case_n_positive(self):
        result = calculateFibonacci(6)
        self.assertEqual(result, 8)

   
if __name__ == '__main__':
    unittest.main()