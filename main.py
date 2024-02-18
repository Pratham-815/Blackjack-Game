import random
import os


def deal_cards():
    """Returns a random card from the deck"""

    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card)


def calculate_score(cards):
    """Takes the list of cards and returns the score"""

    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):

    if user_score>21 and computer_score>21:
        print("You went over...You loose")

    if user_score==computer_score:
        print("Its a draw")

    elif computer_score==0:
        print("You lost...Computer has a blackjack")

    elif user_score==0:
        print("You win...It was a blackjack!!!")

    elif user_score>21:
        print("You lost...Your score went over 21")

    elif computer_score>21:
        print("You win...Computer's score went over 21")

    elif user_score>computer_score:
        print("You win...You score is greater than that of computer's")

    else:
        print("You lost...Computer's score is greater than that of your's")


def play_game():
    
    from art import logo
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer cards: {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over = True
        
        else:
            user_choice = input("Type 'y' to draw another card, type 'n' to pass: ").lower()
            if user_choice=='y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play the game blackjack ? Type 'y' for yes and 'n' for no: ").lower()=='y' :
    os.system('cls')
    play_game()