class UnderAge(Exception):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f"Under age exception for \"{self._name}\" which he is {self._age} years old"


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(name, age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)


if __name__ == "__main__":
    send_invitation("shalom", 5)
    send_invitation("world",19)
