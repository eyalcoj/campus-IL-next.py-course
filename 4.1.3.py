def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    n += 1
    range(10, 0)
    next_prime = (i for i in range(n, n * n) if is_prime(i))
    value = next(next_prime)
    return value


if "__main__" == __name__:
    print(first_prime_over(1000000))
