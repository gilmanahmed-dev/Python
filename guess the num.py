import random
num = random.randint(1,100)
attempts = 0

while True:
    guess = int(input("Guess the number between 1 to 100 : "))
    attempts += 1
    
    if num == guess:
        print("You won !")
        break
    elif guess < num:
        print("Think higher")
    elif guess > num:
        print("Think lower")

print(f"Total attempts = {attempts}")