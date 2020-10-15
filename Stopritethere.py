# import socket
import numpy as np
import time
import random


class Card:
    def __init__(self, suit, order):
        self.suit = suit
        self.order = order


deck = np.arange(52, dtype=object)
hand = np.arange(4, dtype=object)
graveyard = Card(None, None)
endgame = 1
nxt = 0


def setdeck():
    suit = None
    for i in range(0, 52):
        if i/13 == 0:
            suit = 'Spades'
        elif i/13 == 1:
            suit = 'Hearts'
        elif i/13 == 2:
            suit = 'Clubs'
        elif i/13 == 3:
            suit = 'Diamonds'

        if (i + 1) % 13 == 1:
            order = 'Ace'
        elif (i + 1) % 13 == 11:
            order = 'Jack'
        elif (i + 1) % 13 == 12:
            order = 'Queen'
        elif (i + 1) % 13 == 0:
            order = 'King'
        else:
            order = str((i + 1) % 13)
        deck[i] = Card(suit, order)


def shuffle():
    random.shuffle(deck)


# def draw(i, next):
    # hand[i] = deck[next]

def turndraw():
    global nxt
    global graveyard
    if graveyard.order is not None:
        drawmethod = int(input('Take from deck (Type "1") or graveyard (Type "2"): '))
        if drawmethod == 1:
            hand[3] = graveyard
            nxt += 1
        elif drawmethod == 2:
            hand[3] = graveyard
            graveyard = Card(None, None)
    else:
        drawmethod = int(input('Take from deck (Type "1"): '))
        if drawmethod == 1:
            nxt = nxt + 1
            hand[3] = deck[nxt]
        else:
            print('Invalid action.')
            time.sleep(1)
            turndraw()


def firstdraw():
    global nxt
    for i in range(0, 3):
        hand[i] = deck[nxt]
        nxt += 1
    hand[3] = Card(None, None)


def discard():
    global graveyard
    n = int(input('Select a card to discard: '))
    graveyard = hand[n-1]
    if graveyard.suit is not None:
        print('* Current card in graveyard is: ' + graveyard.order + ' of ' + graveyard.suit)
    for x in range(n, 4):
        hand[x-1] = hand[x]
    hand[3] = Card(None, None)


def displayhand():
    for a in range(0, 4):
        if hand[a].order is None:
            pass
        else:
            print(str(a + 1) + '. ' + hand[a].order + ' of ' + hand[a].suit)


def gameturn():
    displayhand()
    turndraw()
    displayhand()
    discard()


def main():
    setdeck()
    shuffle()
    firstdraw()
    while endgame == 1:
        gameturn()


if __name__ == "__main__":
    main()
