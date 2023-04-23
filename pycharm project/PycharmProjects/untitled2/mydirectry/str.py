str = input('enter str')

l = len(str)

list = []

for s in str:
    list += str[l-1]
    l  = l-1


print(list)
