# Import the random module
import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Initialize the number of guesses
guesses = 0

# Loop until the user guesses correctly or runs out of attempts
while guesses < 5:
  # Ask the user to enter a guess
  guess = int(input("Enter your guess: "))

  # Increment the number of guesses
  guesses += 1

  # Check if the guess is correct
  if guess == number:
    # Print a congratulatory message
    print("Correct!")
    print("Congratulations! You guessed the number.")
    # Break out of the loop
    break
  # Check if the guess is too high
  elif guess > number:
    # Print a feedback message
    print("Too high")
  # Check if the guess is too low
  else:
    # Print a feedback message
    print("Too low")

# Check if the user ran out of guesses
if guesses == 5 and guess != number:
  # Print a game over message
  print("Game over! You ran out of guesses.")
  print("The number was", number)
