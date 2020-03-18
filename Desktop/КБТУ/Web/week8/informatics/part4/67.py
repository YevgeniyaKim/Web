n = int(input())
a = []
for i in range(0, n):
    x = int(input())
    a.append(x)

for i in range(1, n):
    while i <= n:
        if (a[i] > 0 and a[i-1] > 0) or (a[i] < 0 and a[i - 1] < 0):
            print("YES")
            exit()
        i += 1
print("NO")