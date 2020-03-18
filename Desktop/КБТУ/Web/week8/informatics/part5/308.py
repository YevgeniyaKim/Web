def xor(a: int, b: int):
    return (a and not b) or (not a and b)


a = int(input())
b = int(input())

print(xor(a, b))
