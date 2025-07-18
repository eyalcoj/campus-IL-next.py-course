import itertools
from itertools import combinations


def main():
    wallet = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    counter = 0
    combination = list()

    for i in range(len(wallet)):
        combination += combinations(wallet, i)

    combination = list(dict.fromkeys(combination))

    for j in combination:
        j_sum = sum(j)
        if j_sum == 100:
            counter += 1

    print(counter)


if "__main__" == __name__:
    main()
