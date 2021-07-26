"""
Project Number Seven - Hangman
Contains everything needed to play a game of hangman. User is prompted for input which is checked against the
selected word. Progress is printed out throughout the game.
(Project Number Six was done online and had no pushable code)
"""
import random
import time

selected_letters = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

title = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/              
"""


def select_word():
    list_of_words = ['dog', 'cat', 'elephant', 'beach', 'surf', 'wave', 'plane', 'country']
    word = list_of_words[random.randint(0, len(list_of_words)-1)]
    len_word = len(word)
    return word, len_word


def hangman_art(count):
    """
    Returns the hangman art
    :param count: Number of incorrect responses that the user has guessed so far
    :return: List[count] - Appropriate picture to print out
    """

    blank = """
   ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||
| |/         ||
| |          || 
| |          ||
| |        
| |         
| |          
| |            
| |           
| |           
| |           
| |          
| |          
| |           
''''''''''|_        |'''| 
|'|'''''''\ \       ''|'|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .
     """
    response1 = """
   ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \ 
| |          ||  `/,|
| |          (\ `_.' 
| |        
| |         
| |          
| |            
| |           
| |           
| |           
| |          
| |          
| |           
''''''''''|_        |'''| 
|'|'''''''\ \       ''|'|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .
     """
    response2 = """
   ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \ 
| |          ||  `/,|
| |          (\ `_.' 
| |         .-`--'.
| |         Y . . Y
| |          |   | 
| |          | . |   
| |          |   |   
| |           
| |           
| |          
| |          
| |           
''''''''''|_        |'''| 
|'|'''''''\ \       ''|'|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .
     """
    response3 = """
   ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \ 
| |          ||  `/,|
| |          (\ `_.' 
| |         .-`--'.
| |        /Y . . Y
| |       // |   | 
| |      //  | . |   
| |     ')   |   |   
| |           
| |           
| |          
| |          
| |           
''''''''''|_        |'''| 
|'|'''''''\ \       ''|'|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .
     """
    response4 = """
   ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \ 
| |          ||  `/,|
| |          (\ `_.' 
| |         .-`--'.
| |        /Y . . Y \ 
| |       // |   | \ \ 
| |      //  | . |  \ \ 
| |     ')   |   |   (`
| |           
| |           
| |          
| |          
| |           
''''''''''|_        |'''| 
|'|'''''''\ \       ''|'|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .
     """
    response5 = """
   ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \ 
| |          ||  `/,|
| |          (\ `_.' 
| |         .-`--'.
| |        /Y . . Y \ 
| |       // |   | \ \ 
| |      //  | . |  \ \ 
| |     ')   |   |   (`
| |          ||' 
| |          || 
| |          || 
| |          || 
| |         / |  
''''''''''|_`-'     |'''| 
|'|'''''''\ \       ''|'|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .
     """
    response6 = """
   ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \ 
| |          ||  `/,|
| |          (\ `_.' 
| |         .-`--'.
| |        /Y . . Y \ 
| |       // |   | \ \ 
| |      //  | . |  \ \ 
| |     ')   |   |   (`
| |          ||'|| 
| |          || ||
| |          || ||
| |          || ||
| |         / | | \ 
''''''''''|_`-' `-' |'''| 
|'|'''''''\ \       ''|'|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .
 """

    list = [blank, response1, response2, response3, response4, response5, response6]
    return list[count]


def get_user_input():
    """
    Requests input from user - repeats until received.

    :return: letter (User selected response)
    """
    while True:
        letter = (input("What letter would you like to select?\n"))
        if letter in selected_letters or letter.lower() not in letters or len(letter) > 1:
            print("Invalid")
            continue
        break
    return letter


def update_word(word, progress, letter):
    """
    Returns the correct string to print out

    :param word: Selected game word
    :param progress: The users correct guesses in their appropriate place
    :param letter: Current guess
    :return: updated progress variable (str)
    """
    underscores = progress.split(' ')
    for i in range(len(word)):
        if letter == word[i]:
            underscores[i] = letter
    return ' '.join(underscores)


def win_cond(ans, word):
    ans = ''.join((ans.split()))
    if ans.strip() == word.strip():
        print("Congratulations, you win!")
        return True


def main():
    global selected_letters
    game_status = True
    word, len_word = select_word()
    incorrect_count = 0
    progress = "_ " * len_word
    print(title)
    print(hangman_art(incorrect_count))
    print("Welcome to to hangman!")

    while game_status:

        print(progress)
        let = get_user_input()
        selected_letters.append(let)
        print(f"You selected {let}")
        time.sleep(1)

        if let in word:
            print("You guessed correctly")
            progress = update_word(word, progress, let)
            if win_cond(progress, word):
                game_status = False
        else:
            print('You guessed incorrectly')
            incorrect_count += 1
            print(hangman_art(incorrect_count))
            time.sleep(1)

        if incorrect_count == 6:
            print(f"Game Over, you lose\nThe word was {word}")
            game_status = False


if __name__ == "__main__":
    main()
