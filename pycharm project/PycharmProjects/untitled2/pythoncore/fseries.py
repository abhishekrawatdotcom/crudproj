first = int(input('enter first no'))
second = int(input('enter second no'))
n = int(input('enter n'))

while n-2:
    c = first + second
    first = second
    second = c
    n = n-1
    print(second)
    print(first,second)
