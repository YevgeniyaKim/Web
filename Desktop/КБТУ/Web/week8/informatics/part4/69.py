n = int(input())
a = []
for i in range(0, n):
    x = int(input())
    a.append(x)
for i in range(0, n):
    while i <= n:
        print(a[n - i - 1])
        break
    i += 1
