from entities.game_level import Level
from entities.card_suit import Suit


class Card:
    """ Luokka, joka antaa yhden kortin tiedot.

    Attributes:
        suit: numeroarvo, class Suit
        value: numeroarvo, kuvaa kortin numeroa
        display: Boolean-arvo, kuvaa, että onko kortti oikeinpäin vai väärinpäin
        game: objekti, kuvaa nykyistä peliä
        card_button: esittää korttia ui:ssa
        column: kertoo kortin column tiedon
        row: kertoo kortin row tiedon
    """

    def __init__(self, suit, value, game):
        """ Luokan konstruktori, joka antaa kortille nämä tiedot.
        Args:
            suit: numeroarvo, class Suit
            value: numeroarvo, kuvaa kortin numeroa
            game: objekti, kuvaa nykyistä peliä
        """
        self.suit = suit
        self.value = value
        self.display = False
        self.game = game
        self.card_button = None
        self.column = None
        self.row = None

    def set_button(self, card_button):
        self.card_button = card_button

    def suitname(self):
        return self.suit.name

    def to_string(self):
        return f'{self.suitname()}-{self.value}'

    def is_same(self, card):
        if self.game.level == Level.EASY:
            if self.value == card.value:
                return True
        elif self.game.level == Level.MEDIUM:
            if self.value == card.value:
                return True
        elif self.game.level == Level.HARD:
            if self.is_same_color(card) and self.value == card.value:
                return True
        return False

    def is_same_color(self, card):
        if self.suit in (Suit.SPADE, Suit.CLUB) and card.suit in (Suit.SPADE, Suit.CLUB):
            return True
        if self.suit in (Suit.HEART, Suit.DIAMOND) and card.suit in (Suit.HEART, Suit.DIAMOND):
            return True
        return False

    def button_place_x(self):
        if self.game.level == Level.EASY:
            return 285*self.column+300
        return 185*self.column+50

    def button_place_y(self):
        return 200*self.row+100

    def set_card_on_table(self, column, row):
        self.column = column
        self.row = row

    def turn_card(self):
        """ Kääntää kortin. """
        self.display = not self.display

    def click_card(self):
        """ Kun pelaaja painaa korttia, niin menee sovelluslogikkaan."""
        self.game.handle_card_turn(self)
