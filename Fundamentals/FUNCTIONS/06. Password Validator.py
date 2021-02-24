def password_validator(a):
    validation_length = True
    validation_ch = True
    validation_digits = True
    if not 6 <= len(a) <= 10:
        validation_length = False
    if not a.isalnum():
        validation_ch = False
    numbers = sum(ch.isdigit() for ch in a)
    if numbers < 2:
        validation_digits = False
    if validation_ch and validation_digits and validation_length:
        print("Password is valid")
    else:
        if not validation_length:
            print("Password must be between 6 and 10 characters")
        if not validation_ch:
            print("Password must consist only of letters and digits")
        if not validation_digits:
            print("Password must have at least 2 digits")


password = input()
password_validator(password)




