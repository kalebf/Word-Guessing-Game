import random

def choose_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
           displayed_word += '_ '
    return displayed_word

def check_guess(word, guessed_letters, guess):
    guessed_letters = guessed_letters.add(guess)
    
    if guess in word:
        return True
    else:
        return False

def is_word_guessed(word, guessed_letters):
    return all(c in guessed_letters for c in word)

def start_game():
    play_again = 'yes'
    words = ["PYTHON", "JAVASCRIPT", "JAVA", "HTML", "CSS"]
    while play_again.lower() in ['yes', 'y']:
        guessed_letters = set()
        word = choose_word(words)

        while True:
            print(f"Guess the Word: {display_word(word, guessed_letters)}")
            guess = input("Enter your guess: ").upper()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single alphabetical character.")
                continue

            if check_guess(word, guessed_letters, guess):
                print(f'Correct Guess! Word: {display_word(word, guessed_letters)} Guessed Letters: {", ".join(guessed_letters)}')

                if is_word_guessed(word, guessed_letters):
                    print(f"Congratulations! You guessed the word: {word}")
                    break
            else:
                print(f'Incorrect Guess! Word: {display_word(word, guessed_letters)} Guessed Letters: {", ".join(guessed_letters)}')

        play_again = input("Do you want to play again? (yes/no): ").lower()

    print("Thank you for playing the Word Game!")
if __name__ == "__main__":
    start_game()        
