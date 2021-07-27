class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.length_validator(value) and self.upper_case_validator(value) and self.number_validator(value):
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def length_validator(self, password):
        return len(password) >= 8

    def upper_case_validator(self, password):
        upper_letters = [char for char in password if char.isupper()]
        return True if upper_letters else False

    def number_validator(self, password):
        numbers = [num for num in password if num.isdigit()]
        return True if numbers else False

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {'*' * len(self.password)}"



