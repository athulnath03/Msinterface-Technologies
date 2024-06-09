import random

def main():
    target_number = random.randint(1, 10)
    attempts = 0
    guessed = False
    
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 10. Can you guess what it is?")
    
    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {target_number} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
if __name__ == "__main__":
    main()