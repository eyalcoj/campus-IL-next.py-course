def main():
    print(is_prime(42))
    print(is_prime(43))


def is_prime(number):
    return not len(list(filter(lambda x: number % x == 0, range(2, number))))


if __name__ == "__main__":
    main()
