import unittest
from erastophanes import count_primes

class TestCountPrimes(unittest.TestCase):
    
    def test_no_primes(self):
        self.assertEqual(count_primes(1), 0)
    
    def test_primes_up_to_10(self):
        self.assertEqual(count_primes(10), 4)  # Primes are 2, 3, 5, 7
    
    def test_primes_up_to_20(self):
        self.assertEqual(count_primes(20), 8)  # Primes are 2, 3, 5, 7, 11, 13, 17, 19
    
    def test_primes_up_to_100(self):
        self.assertEqual(count_primes(100), 25)
    
    def test_large_number(self):
        self.assertEqual(count_primes(1000), 168)

if __name__ == '__main__':
    unittest.main()