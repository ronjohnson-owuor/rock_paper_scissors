import random


def determine_winner(user, computer):
    winning_array = {
        'r': 's',
        'p': 'r',
        's': 'p'
    }
    users = winning_array.get(user)
    if users == computer:
        print("you win")
        print(f'you chose: {user} and computer chose: {computer}')

    elif user == computer:
        print("you draw guys")
        print(f'you chose: {user} and computer chose: {computer}')
    else:
        print("you lost!")
        print(f'you chose: {user} and computer chose: {computer}')



def handle_game_logic(user_guess):
    availlable_choices = ['r', 'p', 's']
    computer_guess = random.choice(availlable_choices)
    determine_winner(user_guess, computer_guess)


while True:
    player_guess = input("choose one (R(rock),P(paper),S(scissors): ").lower()
    if player_guess == 'r' or player_guess == 'p' or player_guess == 's':
        handle_game_logic(player_guess)
        break
    else:
        print("choose between the symbols please")
