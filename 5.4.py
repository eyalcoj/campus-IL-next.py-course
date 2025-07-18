def check_id_valid(id_number):
    """
    Checks if an ID number is valid.
    :param id_number: The ID number to validate
    :type id_number: int
    :return: True if the ID is valid otherwise False
    :rtype: bool
    """
    # Calculate weighted digits and sum their individual digits
    weighted_digits = [int(str(i)[0]) + int(str(i)[1]) if len(str(i)) == 2 else i
                       for i in [int(str(id_number)[i]) * (i % 2 + 1)
                                 for i in range(len(str(id_number)))]]
    # Check if the sum is divisible by 10
    return sum(weighted_digits) % 10 == 0


def id_generator(ID):
    """
    Generates valid ID numbers starting from ID + 1 up to 999999999.
    :param ID: The starting ID number (exclusive)
    :type ID: int
    :return: Yields the next valid ID number
    :rtype: Generator[int]
    """
    for i in range(ID + 1, 999999999):
        if check_id_valid(i):
            yield i


class IDIterator:
    """
    A class used to iterate over valid ID numbers starting from a given ID.
    """

    def __iter__(self, ID):
        """
        Initializes the iterator with a starting ID.
        :param ID: The starting ID number
        :type ID: int
        :return: The iterator object
        :rtype: IDIterator
        """
        self._id = ID
        return self

    def __next__(self):
        """
        Returns the next valid ID number.
        :return: The next valid ID number
        :rtype: int
        :raise: StopIteration: no more found up to 999999999
        """
        for i in range(self._id + 1, 999999999):
            self._id = i
            if check_id_valid(i):
                return i
        raise StopIteration()


def main():
    """
    Main function allowing to choose between a generator or iterator to produce the next 10 valid ID numbers
    :raise: ValueError: If the input ID is not a valid integer
    """
    try:
        user_id = int(input("Enter ID: "))
        type_of_logic = input("Generator or Iterator? (gen / it)? ")
        times = 0

        if type_of_logic == "gen":
            IDs_generator = id_generator(user_id)
            while times < 10:
                print(next(IDs_generator))
                times += 1

        elif type_of_logic == "it":
            IDs_iterator = IDIterator()
            IDs_iterator = IDs_iterator.__iter__(user_id)
            while times < 10:
                print(next(IDs_iterator))
                times += 1

        else:
            print("You entered an incorrect logic type")

    except ValueError:
        print("Invalid input: Please enter a valid ID")


if __name__ == "__main__":
    main()
