#a challenge from - https://www.practicepython.org/exercise/2017/01/10/32-hangman.html

import random

FILE_NAME = 'sowpods_dictionary.txt'

def fetch_words(file_name: str) -> list[str]:
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return []

def pick_word(words: list[str])-> str | None:  #random word
    if not words:
        return None
    return random.choice(words)


def mask_word(word: str) -> str:
    return " ".join("_" for _ in word)

def update_mask(word: str, tracker:dict[str, bool]) -> str:
    return " ".join(char if tracker[char] else "_" for char in word)

def word_to_dict(word: str) -> dict[str, bool]:
    return  {char: False for char in word}


def draw_hangman(n):            #this is a bit messy
    parts = ['  O',' /', '|',  '\\', ' /', ' \\ ']
    print("  |"+"-"*30+"\n  |" + " "*23 + "HANGMAN")
    
    for part in parts[:6-n]:
        if part in (' /', '|',' |'):
            print(part, end="")        
        else:
            print(part)
    print()



def play_hangman():
    words = fetch_words(FILE_NAME)
    guess_word = pick_word(words)
 

    if guess_word is None:
        print("No words available. Exiting Game...")
        return

    tracker = word_to_dict(guess_word)
    letters_guessed = set()
    guesses_left = 6

    print(mask_word(guess_word))

    while guesses_left > 0:
        letter = input("Guess your letter: ").upper()

        if len(letter) != 1 or not letter.isalpha():
            print("Please input a single letter.")
            continue
            
        if letter in letters_guessed:
            print("You have already used that letter.")
            continue

        letters_guessed.add(letter)

        if letter not in guess_word:
            guesses_left -= 1
            print("Incorrect.")
            print(f"You have {guesses_left} {'guesses' if guesses_left > 1 else 'guess'} left.")
            draw_hangman(guesses_left)
            print(update_mask(guess_word, tracker))

            if guesses_left == 0:
                print(f"Game Over. The word was {guess_word}.")
                return
            continue
    
        tracker[letter] = True
        print(update_mask(guess_word, tracker))


        if all(tracker.values()):
            print(f'You guessed it right!. The word was {guess_word}')
            return
        

def main():
    print("Welcome to Hangman.\n\nTry to guess the word.")
    while True:
        play_hangman()
        retry = input("Play again? Y/N: ").upper()

        if retry != "Y":
            print("Thanks for playing. Exiting Game.")
            return
        

if __name__ == "__main__":
    main()