from functools import reduce


def main():
    print(sum_of_digits(104))


def add(val1, val2):
    return val1 + val2


def sum_of_digits(number):
    # I know there is a smarter way to do this but this cleaner because I don't need to make another function
    return reduce(add, list(map(int, list(str(number)))))


if __name__ == "__main__":
    main()
