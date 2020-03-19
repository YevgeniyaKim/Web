from pip._vendor.msgpack.fallback import xrange

n = int(input())
for i in xrange(n):
    print(i + 1, end="")
