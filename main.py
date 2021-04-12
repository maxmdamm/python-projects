import random

chars = '1234567890ßqwertzuiopasdfghjklyxcvbnm,.-+!$%&()='

number = input('Wie viele Passwörter? - ')
number = int(number)

length = input('Passwort länge? - ')
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
