import random

secret = random.randint(1, 100)
tries = 0
while True:
    guess = int(input("Ваша догадка: "))
    tries += 1
    if guess < secret:
        print("Больше")
    elif guess > secret:
        print("Меньше")
    else:
        print("Угадали за", tries, "попыток")
        break