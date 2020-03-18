n = int(input())
a = []
cnt = 0
for i in range(0, n):
    x = int(input())
    a.append(x)

for i in range(1, n):
    while i < n:
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            cnt += 1
            break
        i += 1
        print(cnt)
