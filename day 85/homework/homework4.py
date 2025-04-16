def sum_of_primes():
    n = int(input("Enter a number: "))
    total = 0
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            total += num
    return f"The sum of all prime numbers up to {n} is {total}"
