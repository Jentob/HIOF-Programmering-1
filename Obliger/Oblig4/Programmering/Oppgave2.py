from collections import namedtuple
from random import shuffle

m = "> "

Card = namedtuple("Card", ("rank", "suit"))


class Deck:
    card_ranks = ()
    card_suits = ()

    def __init__(self):
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        self.cards.clear()
        for rank in self.card_ranks:
            for suit in self.card_suits:
                self.cards.append(Card(rank, suit))
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class Standard52CardDeck(Deck):
    card_ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
    card_suits = ("Clubs", "Diamonds", "Hearts", "Spades")


def card_value(card):
    card_values = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}
    return card_values[card.rank]


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def draw_card(self, card):
        self.cards.append(card)
        self.value += card_value(card)
        if card.rank == "Ace":
            self.aces += 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def print_card(self, card):
        return f"{self.cards[card].rank} of {self.cards[card].suit}"

    def print_list(self):
        mark = "- "
        for card, x in enumerate(self.cards):
            print(mark, self.print_card(card))


class Chips:
    def __init__(self):
        self.amount = 100
        self.bet = 0

    def make_bet(self):
        print(f"You have {self.amount} chips. How many would you like to bet?")
        while True:
            try:
                self.bet = int(input(m))
                if self.bet < 1:
                    print("You can't bet less than 1 chip.")
                if self.bet > self.amount:
                    print(f"You can't bet more than you have. You have {self.amount} chips.")
                else:
                    break
            except ValueError:
                print("Not a number.")

    def win(self):
        self.amount += self.bet
        print(f"You won {self.bet} chips. You now have {self.amount} chips.")

    def lose(self):
        self.amount -= self.bet
        print(f"You lost {self.bet} chips. You now have {self.amount} chips.")

    def blackjack(self):
        self.amount += self.bet * 2
        print(f"You won {self.bet * 2} chips. You now have {self.amount} chips.")


def print_dealt_cards():
    print("The cards have been dealt.")
    print(
        f"You have a {player_hand.print_card(0)} and a {player_hand.print_card(1)} with a total value of {player_hand.value}.")
    print(
        f"The dealer's visible card is a {dealer_hand.print_card(0)} and has a value of {card_value(dealer_hand.cards[0])}.")


def check_for_naturals():
    if dealer_hand.value == 21 and player_hand.value == 21:
        print("You and the dealer both got naturals. Your chips have been returned.")
        return True
    if dealer_hand.value == 21:
        print("The dealer got a natural.")
        chips.lose()
        return True
    if player_hand.value == 21:
        print("You got a natural.")
        chips.blackjack()
        return True


def play():
    i = 2
    while True:
        print("Do you wish to hit or stand?\n1 - Hit\n2 - Stand")
        try:
            inp = int(input(m))
            if inp == 1:
                player_hand.draw_card(deck.deal_card())
                print(f"You got dealt a {player_hand.print_card(i)}.")
                i += 1
                print("Your hand now consists of")
                player_hand.print_list()
                print(f"Your hand has a value of {player_hand.value}")
                if player_hand.value > 21:
                    print("You busted.")
                    chips.lose()
                    break
            if inp == 2:
                i = 2
                while True:
                    if dealer_hand.value > 16:
                        print("The dealer's hand consist of")
                        dealer_hand.print_list()
                        print("While your hand consist of")
                        player_hand.print_list()
                        if dealer_hand.value > player_hand.value:
                            chips.lose()
                        elif dealer_hand.value < player_hand.value:
                            chips.win()
                        else:
                            print("Draw. Your chips have been returned.")
                        break
                    dealer_hand.draw_card(deck.deal_card())
                    print(f"The dealer drew a {dealer_hand.print_card(i)}.")
                    i += 1

                    print(f"The dealer's hand has a value of {dealer_hand.value}")
                    if dealer_hand.value > 21:
                        print("The dealer's hand consists of")
                        dealer_hand.print_list()
                        print("The dealer busted.")
                        chips.win()
                        break
                break
            else:
                continue
        except ValueError:
            continue


def play_again():
    while True:
        print("Do you want to play again?\n1 - Yes\n2 - No")
        try:
            inp = int(input(m))
            if inp == 1:
                return True
            if inp == 2:
                return False
            continue
        except ValueError:
            continue


print("---------\nBLACKJACK\n---------"
      )
chips = Chips()
while True:
    game = True
    deck = Standard52CardDeck()
    player_hand = Hand()
    dealer_hand = Hand()

    chips.make_bet()
    player_hand.draw_card(deck.deal_card())
    dealer_hand.draw_card(deck.deal_card())
    player_hand.draw_card(deck.deal_card())
    dealer_hand.draw_card(deck.deal_card())
    print_dealt_cards()

    if not check_for_naturals():
        play()
    if chips.amount < 1:
        print("You have no more chips.")
        break
    if play_again():
        continue
    break
