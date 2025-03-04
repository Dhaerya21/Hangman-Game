Hangman Game 🎮

A fun command-line Hangman game written in Python! Guess the hidden word before the hangman is fully drawn.

📌 Features
- Random word selection from different categories.
- ASCII Hangman visuals that update with each incorrect guess.
- Tracks previously guessed letters to avoid duplicates.
- Optimized input validation and game logic for better performance.
- User-friendly messages and emojis for better engagement.

🚀 Getting Started

Prerequisites
Ensure you have **Python 3.x** installed on your system. You can download it from [python.org](https://www.python.org/).

Installation
1. Clone this repository or download the source code:
   
   git clone https://github.com/Dhaerya21/Hangman-Game.git
   cd Hangman-Game
   
2. Ensure the `hangman_answers.py` file is present and contains category-based word lists.

Running the Game
To start playing, run the following command:

python hangman.py


📝 How to Play
- The game will select a random word from a category.
- You need to guess one letter at a time.
- If the letter is correct, it gets revealed in the word.
- If the letter is incorrect, the hangman drawing progresses.
- You lose if the hangman is fully drawn before guessing the word.
- You win if you guess the word before running out of attempts!

📸 Game Preview

*******************************
Category: Animals
┌────
|  o  
| /|\
|     
_ _ _ g _

Enter your guess: a
✅ Successful guess!


📂 Project Structure

Hangman-Game/
│── hangman.py             # Main game logic
│── hangman_answers.py     # Word categories and answers
│── README.md              # Documentation


📜 License
This open-source project is available under the [MIT License](LICENSE).

🤝 Contributing
Contributions are welcome! Feel free to fork the repo, submit issues, or make pull requests.


Enjoy the game! 🎉

License
This project is licensed under the MIT License.

Author
Dhaerya Khanna

