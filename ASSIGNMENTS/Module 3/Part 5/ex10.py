class InvalidPasswordError(Exception):
    def __init__(self, message):
        super().__init__(message)

password = input("Enter your password: ")

def passwordd():
    try:
        if len(password) < 8:
            raise InvalidPasswordError("Password too short")
        else:
            print("Password is valid")
    except InvalidPasswordError as e:
        print("Error:", e)

passwordd()

