def my(l):
    h = [k for i in l for k in i]
    return h


list = ['red', 'white','green','yellow']
m = my(list)
print(m)
