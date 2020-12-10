# Script for factorial class

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

if __name__=="__main__":
    n = int(input("Enter an integer to compute factorial: "))
    fact = factorial()
    out = fact.compute(n)
    print(out)
