# Script for utility classes
from collections import defaultdict

class factorial():
    def compute(self, n: int) -> int:
        if type(n) is not int:
            raise TypeError
        else:
            if n<0:
                raise ValueError
            elif n == 0:
                return 1
            else:
                return n*self.compute(n-1)
        return

class check_prime():
    def is_prime(self, n:int) -> bool:
        if type(n) is not int:
            raise TypeError
        if n <= 0:
            raise ValueError
        if n == 1:
            return "false"
        for div in range(2, n):
            if n%div == 0:
                return "false"
        return "true"

class remove_duplicates():
    def preserve_spaces(self, ip_text: str) -> str:
        op_text = ""
        encountered_char = defaultdict(lambda: False)
        for char in ip_text:
            if char == " ":
                op_text += char
            else:
                if not encountered_char[char]:
                    op_text += char
                    encountered_char[char] = True
        return op_text

# if __name__=="__main__":
#     n = int(input("Enter an integer to compute factorial: "))
#     fact = factorial()
#     out = fact.compute(n)
#     print(out)
