def moxno(l):
    k = l[0]

    for i in l:
        if i>k:
            k = i
            print(k)
    return k

list = [100,2,5,7,1,0,4,10,1,8,500]
p = moxno(list)
print(p)
