primes = []
n = 2
while len(primes) < 50:
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        primes.append(n)
    n += 1

print(primes)