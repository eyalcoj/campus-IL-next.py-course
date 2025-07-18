def main():
    print(four_dividers(9))
    print(four_dividers(3))


def is_div_four(val):
    return val % 4 == 0


def four_dividers(number):
    return list(filter(is_div_four, range(1, number)))


if __name__ == "__main__":
    main()
