import random

number_test = 10
random_number = random.randint(1, 100)
counter = 0

while True:
    try:
        user_number = int(input("Please enter number or q for exit: ")) 
        counter += 1

        if user_number.lower() == "q":
            print("See you later. Bye bye")
            break

        

        if user_number > random_number:
            print(f"your number {user_number} is bigger than random number")

        if user_number < random_number:
            print(f"your number {user_number} is lower than random number")

        if user_number == 10:
            print(f"sorry, you have only 10 attempts. Ramdom number was: {random_number}")
            break
        if user_number == random_number:
            print("Congratulations! You guess in {counter} attempts")
            break

    except ValueError:
        print("")