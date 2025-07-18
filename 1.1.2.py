def main():
    print(double_letter("python"))
    print(double_letter("we are the champions!"))


def make_double_letter(val):
    return val * 2


def double_letter(my_str):
    return ''.join(map(make_double_letter, list(my_str)))


if __name__ == "__main__":
    main()
