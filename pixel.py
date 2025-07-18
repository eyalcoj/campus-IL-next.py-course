class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        self._red = 128
        self._green = 128
        self._red = 128

    def print_pixel_info(self):
        if self._red == self._green == 0 and self._blue > 50:
            print(fr"X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue}) Blue")
        elif self._green == self._blue == 0 and self._red > 50:
            print(fr"X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue}) Red")
        elif self._blue == self._red == 0 and self._green > 50:
            print(fr"X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue}) Green")
        else:
            print(fr"X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue})")


if __name__ == "__main__":
    p1 = Pixel(5, 6, 250,)
    p1.print_pixel_info()
    p1.set_grayscale()
    p1.print_pixel_info()



