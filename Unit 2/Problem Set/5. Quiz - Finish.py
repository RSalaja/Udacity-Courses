n = 10
i = 0
while i <= n:
    i = i + 1
    print(i)


n = 10
i = 1
while True:
    i = i * 2
    n = n + 1
    if i > n:
        break

n = 12
while n != 1:
    if n % 2 == 0:  # n is even
        n = n/2
    else:
        n = 3 * n + 1
        print(n)