#!/usr/bin/python3
import uuid
import hashlib


class User():
    """
    User class:
    - id: public string unique (uuid)
    - password: private hashed string
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.__password = None

    def __str__(self):
        return "[User] {} - {}".format(self.id, self.__password)

    @property
    def password(self):
        return self.__password

    def set_password(self, password):
        """Set user password, stored as a SHA256 hash"""
        if password is None or not isinstance(password, str):
            self.__password = None
        else:
            self.__password = hashlib.sha256(
                password.encode("utf-8")
            ).hexdigest()

    def is_valid_password(self, password):
        """Check if provided password is correct"""
        if self.__password is None:
            return False
        if password is None or not isinstance(password, str):
            return False
        hashed = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return hashed == self.__password


if __name__ == "__main__":
    print("Test User")
    user = User()
    user.set_password("Holberton")
    if user.is_valid_password("Holberton"):
        print("OK")
    else:
        print("is_valid_password should return True if it's the right password")

