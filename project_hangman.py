import random

words = ["python", "program", "developer", "hangman", "intern"]
word = random.choice(words)
guessed_letters = []
attempts = 6

print(" Welcome to Hangman!")
print("Guess the word, one letter at a time.")

display = ["_" for _ in word]

while attempts > 0 and "_" in display:
    print("\nWord: ", " ".join(display))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print(f" Wrong guess! Attempts left: {attempts}")

if "_" not in display:
    print(f"\n You won! The word was: {word}")
else:
    print(f"\n You lost! The word was: {word}")
