def smallestno(l):
    s = l[0]

    for i in l:
        if i > s:
            s = i
    return s

list = [2,4,5,6,7,8,0]

m = smallestno(list)
print(m)
