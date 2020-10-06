import math
from time import sleep

class Rationals:
    def __init__(self):
        self.next = 0
    
    def rational(self, n):
        diagonal = (-1 + math.sqrt(1 + n * 8)) // 2
        start_of_diagonal = (diagonal * (diagonal +1)) // 2
        numerator = (n - start_of_diagonal) + 1
        denominator = diagonal - (n - start_of_diagonal) + 1
        return f'{int(numerator)}/{int(denominator)}'
    
    def __iter__(self):
        while True:
            yield self.rational(self.next)
            self.next += 1

# Runner
r = Rationals()

try:
    for x in r:
        print(f'{r.next}: {x}')
        sleep(1)
except KeyboardInterrupt as e:
    pass