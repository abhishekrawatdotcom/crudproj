def equalcheck(l , l1):
    result = False

    for i in l:
        for y in  l1:
            if i == y:
                result =  True

                return result

list = [2,3,4,5,6]
list1 = [4,5,6,7,8]
m = equalcheck(list,list1)
print(m)

