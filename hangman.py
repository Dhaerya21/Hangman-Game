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

def hangman_man():
    pass

def hangman_answer():
    pass

def hangman_hint():
    pass

def main():
    print(len(hangman_answers["plants"]))

if __name__ == "__main__":
    main()

