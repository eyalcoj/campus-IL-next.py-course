def main():
    print(combine_coins('$', range(5)))


# def combine_coins(coin, numbers):
#     output = ""
#     for num in numbers:
#         output += coin + str(num) + ', '
#     # Ignore the last comma.
#     return output[:-2]


def combine_coins(coin,  numbers):
    return ", ".join([coin + str(number) for number in numbers])


if __name__ == "__main__":
    main()
