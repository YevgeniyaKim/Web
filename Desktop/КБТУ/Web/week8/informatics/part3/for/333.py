a = int(input())
b = int(input())
if a < b:
    for i in range(a, b):
        if i % 2 == 0:
            print(i)
