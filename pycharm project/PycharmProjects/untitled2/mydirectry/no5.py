def last(n):
    return n[-1]

def sortedbylastele(l):
    return sorted(l, key=last)

print(sortedbylastele([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
