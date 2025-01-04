import os

# Function to clear the screen (works on most systems)
def clear_screen():
    print(chr(27) + "[2J")

# Function to draw the gallows (hangman), or snowman based on wrong guesses
def draw_hangman(wrong_guesses):
    stages = [
        """
           ------
           |    |
           |    
           |   
           |    
           |
        --------
        """, 
        """
           ------
           |    |
           |    O
           |   
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    print(stages[wrong_guesses])

# Function to display the word with guessed letters and underscores
def display_word(word, correct_guesses):
    display = ''.join([letter if letter in correct_guesses else '_' for letter in word])
    print(f"Word: {' '.join(display)}")
    return display

def hangman_game():
    # 1. Player 1 picks a word
    word = input("Player 1, enter a word: ").lower()
    
    # Clear the screen so Player 2 can't see the word
    clear_screen()

    # 2. Setup the game variables
    wrong_guesses = 0
    max_wrong_guesses = 6  # Can be adjusted for difficulty
    correct_guesses = []
    guessed_letters = []
    
    # 3. Start the game loop
    while wrong_guesses < max_wrong_guesses:
        draw_hangman(wrong_guesses)
        display_word(word, correct_guesses)
        
        # 4. Player 2 guesses a letter
        guess = input("Player 2, guess a letter: ").lower()
        
        # Ensure Player 2 hasn't already guessed this letter
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            correct_guesses.append(guess)
        else:
            wrong_guesses += 1
        
        # Check if Player 2 has won
        if display_word(word, correct_guesses).replace(' ', '') == word:
            print("Congratulations, you guessed the word!")
            break
    else:
        draw_hangman(wrong_guesses)
        print(f"Game Over! The word was: {word}")

# Run the game
hangman_game()
