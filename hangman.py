import argparse
import random

hangman_stages = ['''
              +-----+
              |     |
              O     |
             /|\    |
             / \    |
           ---------+
                  ''',
                  '''
              +-----+
              |     |
              O     |
             /|\    |
             /      |
           ---------+
                  ''',
                  '''
              +-----+
              |     |
              O     |
             /|\    |
                    |
           ---------+
                  ''',
                  '''
              +-----+
              |     |
              O     |
             /|     |
                    |
           ---------+
                  ''',
                  '''
              +-----+
              |     |
              O     |
              |     |
                    |
           ---------+
                  ''',
                  '''
              +-----+
              |     |
              O     |
                    |
                    |
           ---------+
                  ''',
                  '''
              +-----+
              |     |
                    |
                    |
                    |
           ---------+
                  ''',
                  '''
              +-----+
                    |
                    |
                    |
                    |
           ---------+
                  ''',
                  '''
              
                    |
                    |
                    |
                    |
           ---------+
                  ''',
                  '''
              
              
                    |
                    |
                    |
           ---------+
                  ''',
                 '''



                    |
                    |
           ---------+
                  ''',
                 '''
                     
                 


                    |
           ---------+
                  ''',
                    
                    
                    '''





           ---------+
                  ''',
                  '''






                  ''',]
words = {
    'regular' : {
        'hard' : ['Jazz', 'Kiwifruit', 'Horror', 'Quiz', 'Rhythm', 'Cowboy', 'Zombie', 'Bookworm', 'Nymph', 'Jacuzzi', 'Zodiac', 'Whiskey'],
        'easy' : ['Pool', 'Mama', 'Egg', 'Fire', 'Arm', 'Sun', 'Dinner', 'Free', 'Horse', 'Book', 'Ice', 'Sea', 'Home', 'Cross', 'Funny', 'House', 'Bed', 'Door', 'Hair', 'Good', 'Rain', 'Drink', 'Eye', 'Blood', 'Dog']
    },
    'harry potter' : {
        'easy' : ['Animagus', 'Hermione Granger', 'Death Eaters', 'Hufflepuff', 'Auror', 'Galleon', 'Slytherin', 'Basilisk', 'Werewolf', 'Pumpkin juice', 'Golden Snitch', 'Gryffindor', 'Basilisk', 'Patronus', 'Gringotts', 'Ravenclaw', 'Quidditch', 'Squib', 'Butterbeer', 'Goblet of Fire', 'Sorting Hat', 'Thestral', 'Hippogriff', 'Seeker', 'Mudblood'],
        'hard' : ['Expelliarmus', 'Expecto Patronum', 'Parselmouth', 'Beauxbatons Academy of Magic', 'Veritaserum', 'Tom Vorlost Riddle', 'Muffliato', 'Rictusempra', 'Draco Dormiens Nunquam Titillandus', 'Cruciatus Curse', 'Broomstick Servicing Kit', 'Grimmauld Place', 'The Forbidden Forest', 'Hogsmeade', 'Heir of Slytherin', 'History of Magic', 'Defence Against the Dark Arts', 'Riddikulus', 'Sectumsempra', 'Flourish and Blotts', 'Dervish and Banges', 'Metamorphmagus', 'Invisibility Cloak'],
    },
    'disney' : {
        'easy' : ['Cinderella', 'Simba', 'Stitch', 'Mulan', 'Arielle', 'Mickey Mouse', 'Bambi', 'Merida', 'Anna', 'Woody', 'Forky', 'Chip', 'Dumbo', 'Tinker Bell', 'Elsa', 'Aladdin', 'Muppets', 'Thor', 'Aurora', 'Goofy', 'Pluto', 'Hercules', 'Yoda', 'Olaf', 'Scar'],
        'hard' : ['Buzz Lightyear', 'Captain America', 'Beauty and the Beast', 'Peter Pan', 'Cheshire Cat', 'Winnie the Po', 'Mary Poppins', 'Maleficent', 'Mike Wazowski', 'Wall-E', 'Kylo Ren', 'Doc McStuffins', 'Snow White', 'Baymax', 'Donald Duck', 'Pocahontas', 'Lightning McQueen', 'Cruella De Vil', 'Pinocchio', 'Ant-Man', 'Snow White and the Seven Dwarfs', 'Dschafar', 'Captain Marvel', 'Jack Skellington', 'Daisy Duck'],
    },
}


def create_parser():
    parser = argparse.ArgumentParser(
        prog = 'HangMan',
        description = 'A program to play hangman',
        epilog = 'Enjoy the game! :)',
    )

    parser.add_argument('-d', '--difficulty', metavar='difficulty', default='easy',
        choices = ['easy', 'hard'],
        help = 'Sets the difficulty of the game. Default is easy. Options are easy, hard',
    )

    parser.add_argument('-t', '--theme', metavar='theme', default='regular',
        choices = ['harry potter', 'disney'],
        help = 'Sets the theme of the game. Default is regular.',
    )

    parser.add_argument('-l', '--lives', metavar='lives', default=6,
        help = 'Sets the amount of lives you have. Default is 6. Maximum is 13',
    )

    return parser

MAX_LIVES = 13
INDENT = ' ' * 12

def print_game_state(lives, guessed_word, guessed_letters, word):
    print()
    print(hangman_stages[lives])
    print(f'{INDENT}{" ".join(guessed_word)}')
    incorrect_guesses = [i for i in guessed_letters if i not in word]
    print(f'{INDENT}{"-" * max(len(" ".join(guessed_word)), len(" ".join(incorrect_guesses)))}')
    print(f'{INDENT}{" ".join(incorrect_guesses)}')

def check_and_update_guess(word, guessed_word, input_letter):
    if input_letter in word:
        for i, ch in enumerate(word):
            if ch == input_letter:
                guessed_word[i] = input_letter
        return True
    return False
    

def play_game(difficulty, theme, lives):
    lives = min(lives, MAX_LIVES)
    header_text = f'Playing {theme.capitalize()} hangman on {difficulty.capitalize()} difficulty'
    print(header_text)
    print('=' * len(header_text))

    word = random.choice(words[theme][difficulty]).lower()
    guessed_word = ['_' if ch != ' ' else ' ' for ch in word]
    guessed_letters = []

    while lives > 0:
        print_game_state(lives, guessed_word, guessed_letters, word)
        input_letter = input(f'{INDENT[:4]}Guess a letter: ').lower()

        if len(input_letter) != 1:
            print(f'{INDENT}Please enter a single letter!')
            continue
    
        if input_letter in guessed_letters:
            print(f'{INDENT}You already guessed that letter!')
            continue

        guessed_letters.append(input_letter)

        if check_and_update_guess(word, guessed_word, input_letter):
            print(f'{INDENT}Correct!')
        else:
            print(f'{INDENT}Incorrect!')
            lives -= 1
        
        if all(ch == ' ' or ch != '_' for ch in guessed_word):
            print_game_state(lives, guessed_word, guessed_letters, word)
            print(f'{INDENT}You won!')
            return
    print(hangman_stages[lives])
    print(f'{INDENT}You lost! The word was {word}')

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    play_game(args.difficulty, args.theme, int(args.lives))