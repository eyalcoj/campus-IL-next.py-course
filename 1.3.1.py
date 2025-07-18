def main():
    print(intersection([1, 2, 3, 4], [8, 3, 9]))
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))


def intersection(list_1, list_2):
    return [list_1[i] for i in range(len(list_1)) if list_1[i] in list_2
            if len(list(filter(lambda x: x == list_1[i], (list_1[i:])))) == 1]


if __name__ == "__main__":
    main()
