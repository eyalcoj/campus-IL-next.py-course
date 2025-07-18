class MusicNotes:
    def __init__(self):
        self._note_list_with_actavase = [[55, 110, 220, 440, 880],
                                         [61.74, 123.48, 246.96, 493.92, 987.84],
                                         [65.41, 130.82, 261.64, 523.28, 1046.56],
                                         [73.42, 146.84, 293.68, 587.36, 1174.72],
                                         [82.41, 164.82, 329.64, 659.28, 1318.56],
                                         [87.31, 174.62, 349.24, 698.48, 1396.96],
                                         [98, 196, 392, 784, 1568]]
        self._note_index = 0
        self._actavase_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._actavase_index >= len(self._note_list_with_actavase[0]) - 1:
            raise StopIteration()

        teder = self._note_list_with_actavase[self._note_index][self._actavase_index]

        if self._note_index >= len(self._note_list_with_actavase) - 1:
            self._note_index = 0
            self._actavase_index += 1
        else:
            self._note_index += 1

        return teder


def main():
    notes_iter = iter(MusicNotes())

    for freq in notes_iter:
        print(freq)


if __name__ == "__main__":
    main()
