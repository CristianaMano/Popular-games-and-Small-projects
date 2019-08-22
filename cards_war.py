import random


class card():
    def __init__(self, number, card_type):
        self.number = number
        self.card_type = card_type


class player():
    def __init__(self, name, nr_cards):
        self.name = name
        self.nr_cards = nr_cards
        self.cards = []
        self.war_hand = []


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]
type_cards = ['diamond', 'clover', 'hearts', 'spades']
player1 = player("player 1", 0)
card_picked = card(random.choice(numbers), random.choice(type_cards))
player1.cards.append(card_picked)
while (player1.nr_cards < 25):
    card_picked = card(random.choice(numbers), random.choice(type_cards))
    card_is_in_hand = 0
    for card_in_hand in player1.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
    if card_is_in_hand == 0:
        player1.cards.append(card_picked)
        player1.nr_cards += 1

player2 = player("player 2", 0)
card_is_in_hand = 1
while card_is_in_hand == 1:
    card_picked = card(random.choice(numbers), random.choice(type_cards))
    card_is_in_hand = 0
    for card_in_hand in player1.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
                break

player2.cards.append(card_picked)
card_picked = card(random.choice(numbers), random.choice(type_cards))
player2.cards.append(card_picked)
while (player2.nr_cards < 25):
    card_picked = card(random.choice(numbers), random.choice(type_cards))
    card_is_in_hand = 0
    for card_in_hand in player1.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
    for card_in_hand in player2.cards:
        if card_picked.card_type == card_in_hand.card_type:
            if card_picked.number == card_in_hand.number:
                card_is_in_hand = 1
    if card_is_in_hand == 0:
        player2.cards.append(card_picked)
        player2.nr_cards += 1

print("Cards have been split")
while (player1.nr_cards > 0 and player2.nr_cards > 0):
    card_on_filed1 = random.choice(player1.cards)
    card_on_filed2 = random.choice(player2.cards)
    player1.cards.remove(card_on_filed1)
    player1.nr_cards -= 1
    player2.nr_cards -= 1
    player2.cards.remove(card_on_filed2)
    player1.war_hand.append(card_on_filed1)
    player2.war_hand.append(card_on_filed2)

    if card_on_filed1.number > card_on_filed2.number:
        print(card_on_filed1.number, " is bigger", card_on_filed2.number)
        print("Cards taken by player: ", player1.name)
        player1.cards.extend(player2.war_hand)
        player1.cards.extend(player1.war_hand)
        player2.nr_cards = player2.nr_cards - len(player2.war_hand)
        player1.nr_cards = player1.nr_cards + len(player1.war_hand)
        player2.war_hand = []
        player1.war_hand = []
    elif (card_on_filed1.number < card_on_filed2.number):
        print(card_on_filed2.number, "is bigger", card_on_filed1.number)
        print("Cards taken by player: ", player2.name)
        player2.cards.extend(player2.war_hand)
        player1.cards.extend(player1.war_hand)
        player2.nr_cards = player2.nr_cards + len(player2.war_hand)
        player1.nr_cards = player1.nr_cards - len(player1.war_hand)
        player2.war_hand = []
        player1.war_hand = []
    else:
        if card_on_filed2.number > len(player1.cards):
            for i in range(0, len(player1.cards) - 1):
                card_on_filed1 = random.choice(player1.cards)
                card_on_filed2 = random.choice(player2.cards)
                player1.nr_cards -= 1
                player2.nr_cards -= 1
                player1.war_hand.append(card_on_filed1)
                player1.cards.remove(card_on_filed1)
                player2.war_hand.append(card_on_filed2)
                player2.cards.remove(card_on_filed2)
        elif card_on_filed2.number > len(player2.cards):
            for i in range(0, len(player2.cards) - 1):
                card_on_filed1 = random.choice(player1.cards)
                card_on_filed2 = random.choice(player2.cards)
                player1.nr_cards -= 1
                player2.nr_cards -= 1
                player1.war_hand.append(card_on_filed1)
                player1.cards.remove(card_on_filed1)
                player2.war_hand.append(card_on_filed2)
                player2.cards.remove(card_on_filed2)
        else:
            for i in range(0, card_on_filed2.number - 1):
                card_on_filed1 = random.choice(player1.cards)
                card_on_filed2 = random.choice(player2.cards)
                player1.nr_cards -= 1
                player2.nr_cards -= 1
                player1.war_hand.append(card_on_filed1)
                player1.cards.remove(card_on_filed1)
                player2.war_hand.append(card_on_filed2)
                player2.cards.remove(card_on_filed2)

    for card_in_hand in player1.cards:
        print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
    print()
    for card_in_hand in player2.cards:
        print(card_in_hand.number, " ", card_in_hand.card_type, end=';')
    print()
print()
if player2.nr_cards < 0:
    print(player1.name, " won")
else:
    print(player2.name, " won")
