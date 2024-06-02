def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        while not is_prime(divisor):
            divisor += 1
    return factors

def main():
    with open('f_in.dat', 'r') as f_in:
        numbers = [int(line.strip()) for line in f_in]

    with open('f_out.dat', 'w') as f_out:
        for number in numbers:
            factors = prime_factors(number)
            f_out.write(' '.join(map(str, factors)) + '\n')

if __name__ == "__main__":
    main()