import random
import sys
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