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

    