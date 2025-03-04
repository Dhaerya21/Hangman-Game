import random 
from hangman_answers import hangman_answers

hangman_art ={0:("┌──── ",
                 "|     ",
                 "|     ",
                 "|     "),
              1:("┌──── ",
                 "|  o  ",
                 "|     ",
                 "|     "),
              2:("┌──── ",
                 "|  o  ",
                 "|  |  ",
                 "|     "),
              3:("┌──── ",
                 "|  o  ",
                 "| /|  ",
                 "|     "),
              4:("┌──── ",
                 "|  o  ",
                 "| /|\\ ",
                 "|     "),
              5:("┌──── ",
                 "|  o  ",
                 "| /|\\ ",
                 "| /   "),
              6:("┌──── ",
                 "|  o  ",
                 "| /|\\ ",
                 "| / \\ "),}

def hangman_man(guess_count):
    for line in hangman_art[guess_count]:
        print(line)

def hangman_answer(answer, guess_count):
    print(" ".join(answer))
    print(f"you took a total of {guess_count} guesses")
    pass

def hangman_hint(category,hint,guess_count):
    print(f"category is {category} ")
    hangman_man(guess_count)
    print(" ".join(hint))


def main():
    category = random.choice(list(hangman_answers.keys()))
    answer = random.choice(hangman_answers[category])
    guess_count = 0
    guessed_words = set()
    hint = ["_" for _ in range(len(answer))]
    hangman_hint(category,hint,guess_count)
    
    
    

if __name__ == "__main__":
    main()

