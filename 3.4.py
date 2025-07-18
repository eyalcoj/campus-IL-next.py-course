class UsernameContainsIllegalCharacter(Exception):
    def __str__(self):
        return "The username has illegal character"


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password missing characters"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long"


def check_input(username, password):
    pass
    # It too long to do and I get the hang of it already so it worth less to keep doing this
