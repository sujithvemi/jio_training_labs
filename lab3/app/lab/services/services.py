from scripts.utils import *
import time

class LabService():
    def compute_factorial(self, n: int):
        start = time.time()
        fact = factorial()
        result = fact.compute(n)
        end = time.time()
        
        return result, str((end-start)*1000) + 'ms'

    def check_prime(self, n: int):
        start = time.time()
        prime = check_prime()
        result = prime.is_prime(n)
        end = time.time()
        
        return result, str((end-start)*1000) + 'ms'
    
    def remove_duplicates(self, text: int):
        start = time.time()
        rm_dups = remove_duplicates()
        result = rm_dups.preserve_spaces(text)
        end = time.time()
        
        return result, str((end-start)*1000) + 'ms'
