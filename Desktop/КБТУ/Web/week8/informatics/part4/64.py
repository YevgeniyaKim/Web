n = int(input())
a = []
for i in range(0, n):
    x = int(input())
    a.append(x)
    if x % 2 == 0:
        print(x)
