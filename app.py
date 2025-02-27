import random

# List of words
words = ["enum", "python", "collab", "vscode", "game"]

# Select a random word
word = random.choice(words)
guessed_letters = []
attempts = 6

# Display welcome message
print("Welcome to Hangman!")
displayed_word = "_" * len(word)  # Initially hide all letters
print(displayed_word)

while attempts > 0:
    guess = input("\nGuess a letter: ").lower()

    # Validate input (must be a single letter)
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter! Try another one.")
        continue

    # Add guessed letter to the list
    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! {attempts} attempts left.")

    # Update the displayed word
    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_word)

    # Check if the player has won
    if "_" not in displayed_word:
        print(f"🎉 Congratulations! You guessed the word: {word}")
        break

# Game over condition
if "_" in displayed_word:
    print(f"💀 Game Over! The correct word was: {word}")
