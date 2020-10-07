
"""
    N:umber of discs
    F:rom
    H:elper
    T:arget
"""

def move(o, t):
    print(f'Move disc from {o} to {t}')
 

def hanoi(n, o, h, t):
    if n==0:
        pass
    else:
        hanoi(n-1, o, t, h)
        move(o, t)
        hanoi(n-1, h, o, t)

hanoi(4, 'A', 'B', 'C')


  