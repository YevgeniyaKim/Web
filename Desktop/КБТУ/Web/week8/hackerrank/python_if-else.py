n = int(input())
if n % 2 == 1 or (n % 2 == 0 and n in range(6, 21)):
    print("Weird")
elif n > 20 or (n % 2 == 0 and n in range(2, 6)):
    print("Not Weird")
