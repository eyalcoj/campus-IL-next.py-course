def main():
    print(is_funny("hahahahahaha"))
    print(is_funny("hahahahbahaha"))


# def is_funny(string):
#     for char in string:
#         if char != 'h' and char != 'a':
#             return False
#     return True


def is_funny(string):
    return 0 == len(list(filter(lambda x: x != 'h' and x != 'a', list(string))))


if __name__ == "__main__":
    main()
