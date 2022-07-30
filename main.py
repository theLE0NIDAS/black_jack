############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def add_card(player):
    player.append(random.choice(cards))


def sum_checkerl21(player):
    for n in range(len(player)):
        if sum(player) > 20 and player[n] == 11:
            player[n] = 1


def init():
    add_card(dealer)
    add_card(dealer)

    sum_checkerl21(dealer)
    print(f"dealer {dealer[0]}")

    add_card(you)
    add_card(you)

    sum_checkerl21(you)
    print(f"you {you}")


def adder():
    want_to_add = "y"
    while want_to_add == 'y':
        if sum(you) < 21:
            want_to_add = input("Want to add card? 'y' for yes, 'n' for no: ")
            if want_to_add == 'y':
                add_card(you)
                if you[-1]==11 and sum(you)>21:
                    you[-1]=1
                if sum(you) >= 21:
                    break
                else:
                    print(f"you {you}")

    while sum(dealer) < 16:
        add_card(dealer)


def score():
    if sum(you) <= 21 and sum(dealer) > 21:
        print(f"you win")
        score = 1
    elif sum(you) > sum(dealer) and sum(you) <= 21:
        print(f"you win")
        score = 1
    elif sum(you) == sum(dealer):
        print("draw")
        score = 0
    else:
        print("you lose")
        score = -1
    print(f"dealer {dealer}")
    print(f"you {you}")
    return score


print(logo)
player_score = 0
while True:
    want_to_play = input("Want to play Blackjack? 'y' for yes, 'n' for no: ")
    clear()
    if want_to_play == "y":
        print(logo)
        dealer = []
        you = []
        init()
        adder()
        player_score = player_score + score()
        if player_score < 0:
            player_score = 0
        print(f"your score: {player_score}")
    else:
        print("bye")
        break
