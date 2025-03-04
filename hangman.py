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
    print("Answer: " + "".join(answer))
    print(f"you took a total of {guess_count} guesses")

def hangman_hint(category,hint,guess_count):
    print("*******************************")
    print(f"category: {category} ")
    hangman_man(guess_count)
    print(" ".join(hint))
    print("\n")


def main():
    category = random.choice(list(hangman_answers.keys()))
    answer = random.choice(hangman_answers[category])
    guess_count = 0
    guessed_words = set()
    hint = ["_" for _ in range(len(answer))]
    while True:
        if "_" not in hint:
            print("🎉 You Win!!")
            hangman_answer(answer,guess_count)
            break
        elif guess_count >= len(hangman_art)-1:
            print("❌ You Lose!!")
            hangman_answer(answer,guess_count)
            break
        hangman_hint(category,hint,guess_count)
        guess = input("enter your guess: ").lower()
        if len(guess)>1 or not guess.isalpha() :
            print("⚠️ Enter a valid single letter.")
            continue
        if guess in guessed_words:
            print("🔁 Already guessed!")
            continue
        guessed_words.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i]= guess
            print("✅ Successful guess!")
        else:
            print("❌ Incorrect guess.")
            guess_count+=1
    print("\n🎮 Thanks for playing!")

if __name__ == "__main__":
    main()

