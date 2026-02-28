import random
computer_choice=random.randint(0,500)
user_guess=-1
attempt_taken=0
while (user_guess!=computer_choice):
    user_guess=int(input("Guess a Number Between 0 to 500: "))
    if user_guess > computer_choice:
        print("The Computer Choice is Lower Than Your Guess! ")
        attempt_taken+=1
    elif user_guess < computer_choice:
        print("The Computer Choice is Higher Than Your Guess! ")
        attempt_taken+=1
    else:
        print("Hurray!!! You Guessed it Right!")
        attempt_taken+=1
print(f"The Total Number of Attempt You Taken To Guess {computer_choice} is: {attempt_taken}")