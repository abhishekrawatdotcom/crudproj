def checknoofword(n, str):
    re = []
    text = str.split(" ")
    for i in text:
        if len(i) > n:
            re.append(i)
    return re


m = checknoofword(3 , 'the bomb bosss doggy kutta ca')
print(m)
