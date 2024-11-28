import random, os, time

def binaryGame():
    low = 1
    high = 100
    found = False
    count = 0
    while not found:
        count += 1
        midpoint = (low + high) // 2
        while True:
            print(f"My guess is {midpoint}")
            correct = input("""Is this correct?
1 - Yes
2 - No, you are too high.
3 - No, you are too low.
> """)
            if correct in "123":
                break
            else:
                print("That is not an option. Please choose either 1, 2 or 3. \n")
        if correct == "1":
            found = True
        elif correct == "2":
            high = midpoint - 1
        else:
            low = midpoint + 1
    print(f"Your number was {midpoint}!")
    print(f"Amount of Guesses: {count}")

while True:
    option = input("""Welcome to the guessing game! Which would you like to do?
1 - You Guess
2 - I Guess
3 - Exit
> """)
    if option in "123":
        break
    else:
        print("That is not an option. Please choose either 1, 2 or 3.\n")

if option == "1":
    number = random.randint(1,100)
    found = False
    count = 0
    print("I have chosen a number between 1 and 100. Please guess this number in the shortest amount of attempts possible.")
    while not found:
        count += 1
        while True:
            try: 
                guess = int(input("\nGuess an integer: "))
                if guess in range(1, 101):
                    break
                else:
                    print("Please choose a number between 1 and 100.")
            except:
                print("That is not an integer. Please try again.")
        if guess == number:
            print("Correct!")
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

    print(f"\nAmount of guesses: {count}")
    os.system("pause")
if option == "2":
    print("Please think of a number between 1 and 100. I will give you 5 seconds.")
    time.sleep(5)
    print("Times up!")
    binaryGame()
    os.system("pause")