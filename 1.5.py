from functools import reduce


def main():
    # 1
    with open(r"C:\Users\Eyal\PycharmProjects\campus-IL-next.py-course\names.txt") as f_names:
        print(sorted(f_names.read().split(), key=len)[-1])

    # 2
    with open(r"C:\Users\Eyal\PycharmProjects\campus-IL-next.py-course\names.txt") as f_names:
        print(len(reduce(lambda x, y: x + y, f_names.read().split())))

    # 3
    with open(r"C:\Users\Eyal\PycharmProjects\campus-IL-next.py-course\names.txt") as f_names:
        names = sorted(f_names.read().split(), key=len)
        print('\n'.join([names[i] for i in range(len(names)) if
                         len(names[0]) == len(names[i])]))

    # 4
    with open(r"C:\Users\Eyal\PycharmProjects\campus-IL-next.py-course\names.txt") as f_names, open(
            r"C:\Users\Eyal\PycharmProjects\campus-IL-next.py-course\name_length.txt", 'w') as s_name:
        s_name.write('\n'.join([str(len(i)) for i in f_names.read().split()]))

    # 5
    number = int(input("Enter _name length: "))
    with open(r"C:\Users\Eyal\PycharmProjects\campus-IL-next.py-course\names.txt") as f_names:
        names = sorted(f_names.read().split(), key=len)
        print('\n'.join([names[i] for i in range(len(names)) if
                         number == len(names[i])]))


if __name__ == "__main__":
    main()
