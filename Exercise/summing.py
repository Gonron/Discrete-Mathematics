class Math:
    @staticmethod
    def sum_even_integers_below(n):
        res = 0
        for k in range(2, n + 1, 2):
            print(k)
            res += k
        return res
    
    @staticmethod
    def sum_integers_below(n):
        return (n * (n + 1)) // 2

print(*map(Math.sum_even_integers_below,[100,1000,1000000]),sep='\n')