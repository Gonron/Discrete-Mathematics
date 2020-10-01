

class Sets:
    def __init__(self, lower, upper):
        self.s = list(x for x in range(lower, upper +1))
    
    def __repr__(self):
        return str(self.s)

    # Membership
    def is_member(self, ele):
        return ele in self.s

    def intersection(self, l):
        i, j = 0, 0
        res = []

        while i < len(self.s) and j < len(l):
            if self.s[i] == l[j]:
                res.append(self.s[i])
                i += 1
                j += 1
            elif self.s[i] > l[j]:
                j += 1
            else:
                i += 1
        return res
    
    def intersection_two(self, l):
        return [ele for ele in self.s if ele in l]
        
    def union(self, l):
        i, j = 0, 0
        res = []

        while i < len(self.s) and j < len(l):
            if self.s[i] == l[j]:
                res.append(l[j])
                i += 1
                j += 1
            elif self.s[i] < l[j]:
                res.append(self.s[i])
                i += 1
            else:
                res.append(l[j])
                j += 1
        return res + self.s[i:] + l[j:]

    def difference(self, l):
        return "not yet implemented"
    
    def complement(self):
        return "not yet implemented"

s = Sets(-10,10)
al = [2, 10, 20]
bl = [-4, -2, 0, 1, 2, 3, 12]


print(s, sep='\n')
print(s.is_member(5))
print(s.is_member(20))
print(s.intersection(al))
print(s.intersection_two(al))
print(s.union(bl))

