import random

def number(): # generates random number between 1 and 100
    return random.randint(1, 100)

attempts = 0  # attempts variable to count attempts
num = number() # num for storing generated number

# Game title
print("Welcome to The Perfect Guess Game.")
print("where you can guess number between 1 and 100.")


while True:
        guess = int(input("Guess a number: ")) # takes guess from user
        attempts += 1 # counts the number of attempts

# Conditions for number guesses
        if (guess > num):
            print("🔺 Too High. Lower number please...")
        elif (guess < num):
            print("🔻 Too Low. Higher number please...")
        elif (guess == num):
            print(f"Congratulations 🎉 You have guessed the number; {num} in {attempts} attempts.")
            break # breaks the loop
        elif (guess > 100):
            print("Guess 🤔 a number between 1 and 100, please...")
        else:
            print("❌ Something went wrong...")
