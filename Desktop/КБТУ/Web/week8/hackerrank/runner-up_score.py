n = int(input())
arr = map(int, input().split())
arr = [i for i in arr if i != max(arr)]
print(max(arr))
