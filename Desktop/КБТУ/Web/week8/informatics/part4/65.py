n = int(input())
a = []
cnt = 0
for i in range(0, n):
    x = int(input())
    a.append(x)
    if x > 0:
        cnt += 1
print(cnt)
