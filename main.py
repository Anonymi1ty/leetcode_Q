def solve():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    primes = set()
    for v in arr:
        x = v
        if x <= 1:
            continue
        d = 2
        while d * d <= x:
            if x % d == 0:
                primes.add(d)
                while x % d == 0:
                    x //= d
            d += 1 if d == 2 else 2
        if x > 1:
            primes.add(x)

    if not primes:
        print(0)
        return

    best = 0
    for p in primes:
        ans = 0
        i = 0
        while i < n:
            if arr[i] % p != 0:
                i += 1
                continue
            j = i
            while j < n and arr[j] % p == 0:
                j += 1
            L = j - i
            ans += (L + 1) // 2
            i = j
        if ans > best:
            best = ans

    print(best)


if __name__ == "__main__":
    solve()
