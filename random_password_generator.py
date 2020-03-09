import random
import string


# gets the lenght of the password from user
def get_length():
    length = int(input("how long do you want your password to be ?\n"))
    while length < 6:
        print("You need to have atleast 6 characters long password...")
        length = int(input("Enter length of your password one more time: \n"))
    letters = int(input("how many letters do you want in your password ?\n"))
    numbers = int(input("how many numbers do you want in your password ?\n"))
    return length, letters, numbers


# generates the password according to input criteria
def password_generator(length, letters, numbers):
    password = "".join(random.choices(string.ascii_letters, k=letters))
    password = password + "".join(random.choices(string.digits, k=numbers))
    if len(password) == length:
        return shuffle_password(password)
    else:
        password = password + "".join(random.choices("!@#$%&*_+=*-",
                                                     k=length - (numbers + letters)))

        return shuffle_password(password)


# shuffles the password
def shuffle_password(password):
    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    return password


values = get_length()
new_password = password_generator(values[0], values[1], values[2])

print(f"Your new password is: \n{new_password}")
