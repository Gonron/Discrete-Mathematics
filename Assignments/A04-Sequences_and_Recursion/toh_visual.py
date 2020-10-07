import time

"""
Max number of moves for:
    3 Rings: 7
    4 Rings: 15
    5 Rings: 31
    6 Rings: 63
    7 Rings: 127

    ...

    nMaxMoves = cMaxMoves * 2 + 1 // 15 * 2 + 1 = 31
"""



class Hanoi():
    def __init__(self, n):
        self.n = n
        self. moves = 0
        self.A = list(range(n, 0, -1)) # Populate pole A with numbers n to 1
        self.B = list()
        self.C = list()
        return

    def __str__(self):
        return f'Move: {self.moves}\n\tA: {self.A}\n\tB: {self.B}\n\tC: {self.C}'

    def solve(self, rings, origin, odd, target):
        if rings == 1:
            move = origin.pop() # Remove ring from origin pole
            target.append(move) # Appends ring to target pole
            self.moves += 1 # Counts up moves
            print(tower)
        else:
            self.solve(rings-1, origin, target, odd)
            move = origin.pop() 
            target.append(move) 
            self.moves += 1
            print(tower)
            self.solve(rings-1, odd, origin, target)
        return

if __name__ == "__main__":
    n = 4
    tower = Hanoi(n)
    print(tower)
    tower.solve(tower.n, tower.A, tower.B, tower.C)


    
