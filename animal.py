class Animal:
    count_animals = 0
    zoo_name = "Hayaton"

    def __init__(self, name, hanger=0):
        self._name = name
        self._hunger = hanger
        self._age = 0
        Animal.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger > 0

    def feed(self):
        self._hunger -= 1

    def talk(self):
        pass

    def __str__(self):
        return self._name


class Dog(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def __str__(self):
        return "Dog" + super().__str__()

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def __str__(self):
        return "Cat" + super().__str__()

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def __str__(self):
        return "Skunk" + super().__str__()

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def __str__(self):
        return "Unicorn" + super().__str__()

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger=0, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    def __str__(self):
        return "Dragon" + super().__str__()

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


if __name__ == "__main__":
    # dog1 = Animal("snow")
    # dog2 = Animal()
    #
    # dog1.birthday()
    # print(dog1.get_age())
    # print(dog2.get_age())
    #
    # print(dog1.get_name())
    # print(dog2.get_name())
    #
    # dog2.set_name("white")
    #
    # print(dog2.get_name())
    #
    # print(Animal.count_animals)

    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    slunk = Skunk("Stinky", 0)
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)

    zoo_lst = [dog, cat, slunk, unicorn, dragon]

    dog2 = Dog("Doggo", 80)
    zoo_lst.append(dog2)
    cat2 = Cat("Kitty", 80)
    zoo_lst.append(cat2)
    slunk2 = Skunk("Stinky Jr.", 80)
    zoo_lst.append(slunk2)
    unicorn2 = Unicorn("Clair", 80)
    zoo_lst.append(unicorn2)
    dragon2 = Dragon("McFly", 80)
    zoo_lst.append(dragon2)

    for animal in zoo_lst:
        if animal.is_hungry():
            while animal.is_hungry():
                animal.feed()
            print(animal)
            animal.talk()
            if isinstance(animal, Dog):
                animal.fetch_stick()
            elif isinstance(animal, Cat):
                animal.chase_laser()
            elif isinstance(animal, Skunk):
                animal.stink()
            elif isinstance(animal, Unicorn):
                animal.sing()
            elif isinstance(animal, Dragon):
                animal.breath_fire()

    print(Animal.zoo_name)