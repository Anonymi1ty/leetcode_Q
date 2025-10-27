import sys

data = iter(sys.stdin.read().strip().split())

n = int(next(data))

out = []
for _ in range(n):
    a = int(next(data))
    b = int(next(data))
    out.append(str(a+b))

print("\n".join(out))