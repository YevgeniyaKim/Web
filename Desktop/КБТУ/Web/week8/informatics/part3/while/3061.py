n = int(input())
i = 1
k = 0
while True:
    if i >= n:
        print(k)
        exit()
    i *= 2
    k += 1
