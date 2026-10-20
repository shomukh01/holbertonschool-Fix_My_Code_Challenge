#!/usr/bin/python3
"""
 User Model
"""
import hashlib
import uuid


class User:
    """User with a unique id and an MD5-hashed password."""

    __password = None

    def __init__(self):
        """Initialize a new user with a unique id."""
        self.id = str(uuid.uuid4())

    @property
    def password(self):
        """Return the stored password hash."""
        return self.__password

    @password.setter
    def password(self, pwd):
        """Store an MD5 hash for string passwords, otherwise clear it."""
        if pwd is None or type(pwd) is not str:
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd):
        """Return whether pwd matches the stored password hash."""
        if pwd is None or type(pwd) is not str:
            return False
        if self.__password is None:
            return False
        password_hash = hashlib.md5(pwd.encode()).hexdigest().lower()
        return password_hash == self.__password


if __name__ == '__main__':
    print("Test User")

    user_1 = User()
    if user_1.id is None:
        print("New User should have an id")

    user_2 = User()
    if user_1.id == user_2.id:
        print("User.id should be unique")

    u_pwd = "myPassword"
    user_1.password = u_pwd
    if user_1.password == u_pwd:
        print("User.password should be hashed")

    if user_2.password is not None:
        print("User.password should be None by default")

    user_2.password = None
    if user_2.password is not None:
        print("User.password should be None if setter to None")

    user_2.password = 89
    if user_2.password is not None:
        print("User.password should be None if setter to an integer")

    if not user_1.is_valid_password(u_pwd):
        print("is_valid_password should return True if it's the right password")

    if user_1.is_valid_password("Fakepwd"):
        print("is_valid_password should return False if it's not the right password")

    if user_1.is_valid_password(None):
        print("is_valid_password should return False if compare with None")

    if user_1.is_valid_password(89):
        print("is_valid_password should return False if compare with integer")

    if user_2.is_valid_password("No pwd"):
        print("is_valid_password should return False if no password set before")
