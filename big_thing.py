class BigThing:

    def __init__(self, item):
        self._item = item

    def size(self):
        if isinstance(self._item, int):
            print(int)
        else:
            print(len(self._item))


class BigCat(BigThing):

    def __init__(self, item, wight):
        super().__init__(item)
        self._wight = wight

    def size(self):
        if self._wight > 20:
            return "Very Fat"
        elif self._wight > 15:
            return "Fat"
        else:
            return "OK"


if __name__ == "__main__":
    cutie = BigCat("mitzy", 22)
    print(cutie.size())


