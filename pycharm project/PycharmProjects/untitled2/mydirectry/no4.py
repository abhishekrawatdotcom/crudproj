def countstring(l):
    count = 0

    for w in l:
        if len(w) > 1 and w[0] == w[-1]:
            count = count + 1


    return count

list = ['red','green', 'aba','abc','cbc']

m = countstring(list)
print(m)


