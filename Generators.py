def Square(n):
    for i in range(1,n + 1):
        yield i * i
def Odd(n):
    for i in range(0,n + 1):
        if i % 2:
            yield i
def f5(n):
    for i in range(n,-1,-1):
        yield i
def f3(n):
    for i in range(0,n + 1):
        if i % 12 == 0:
            yield i
def f4(a,b):
    for i in range(a,b + 1):
        yield i
for num in Square(12):
    print(num,end = ',')
print()
for num in Odd(123):
    print(num,end = ',')
print()
for num in f3(123):
    print(num,end = ',')
print()
for num in f5(24):
    print(num,end = ',')
print()
for num in f4(24,123):
    print(num,end = ',')
print()