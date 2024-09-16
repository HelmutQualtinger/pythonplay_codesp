import unittest
from erastophanes import sieve_of_eratosthenes

class TestSieveOfEratosthenes(unittest.TestCase):
    
    def test_primes_up_to_10(self):
        self.assertEqual(sieve_of_eratosthenes(10), [2, 3, 5, 7])
    
    def test_primes_up_to_1(self):
        self.assertEqual(sieve_of_eratosthenes(1), [])
    
    def test_primes_up_to_20(self):
        self.assertEqual(sieve_of_eratosthenes(20), [2, 3, 5, 7, 11, 13, 17, 19])
    
    def test_primes_up_to_0(self):
        self.assertEqual(sieve_of_eratosthenes(0), [])
    
    def test_primes_up_to_2(self):
        self.assertEqual(sieve_of_eratosthenes(2), [2])

if __name__ == '__main__':
    unittest.main()