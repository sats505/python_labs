limit = 2000000
sum_primes = 0

for num in range(2, limit):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        sum_primes += num

print("Sum of primes below two million:", sum_primes)

#5.2
a, b = 1, 2
sum_even = 0

while b <= 4000000:
    if b % 2 == 0:
        sum_even += b
    a, b = b, a + b

print("Sum of even Fibonacci numbers:", sum_even)
