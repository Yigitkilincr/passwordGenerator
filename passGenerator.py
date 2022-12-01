import secrets
import random
import string

numbers = int(input('Number of digits in Password:'))
lowercase = int(input('Number of lowercase chars in Password:'))
uppercase = int(input('Number of uppercase chars in Password:'))
special_chars = int(input('Number of special chars in Password:'))
total_length = int(input('The total password length. If passed (not 0), it will ignore the inputs and generate completely random passwords with the specified length:'))
amount = int(input('Amount of passwords:'))


# Amount of passwords

passwords = []

# Check total length passed. Then generate password.

for _ in range(amount):
    if total_length:
        passwords.append("".join([secrets.choice(string.digits + string.ascii_letters + string.punctuation)
        for _ in range(total_length)]))
    else:
        password = []

        # If / how many numbers the password should contain
        for _ in range(numbers):
            password.append(secrets.choice(string.digits))

        # If / how many uppercase characters the password should contain
        for _ in range(uppercase):
            password.append(secrets.choice(string.ascii_uppercase))

        # If / how many lowercase characters the password should contain
        for _ in range(lowercase):
            password.append(secrets.choice(string.ascii_lowercase))

        # If / how many special characters the password should contain
        for _ in range(special_chars):
            password.append(secrets.choice(string.punctuation))

        random.shuffle(password)
        password = ''.join(password)

        passwords.append(password)

for i in range(len(passwords)):
    print(passwords[i])
