import random
from player import *


class Board:
    MAX_NUMBER = 100
    MIN_NUMBER = 1

    PLAYER_MOVEMENTS = 2

    cards_per_players = {
        2: 7,
        3: 6,
        4: 5,
    }

    def __init__(self, n_players):

        self.cards = range(self.MIN_NUMBER + 1, self.MAX_NUMBER - 1)
        self.rows = {}
        self.rows['up_a'] = [self.MIN_NUMBER]
        self.rows['up_b'] = [self.MIN_NUMBER]
        self.rows['down_a'] = [self.MAX_NUMBER]
        self.rows['down_b'] = [self.MAX_NUMBER]
        random.shuffle(self.cards)

        self.players = []
        self.winners = []
        for p in xrange(1, n_players + 1):
            player_cards = []
            for c in xrange(1, self.cards_per_players.get(n_players)):
                player_cards.append(self.cards.pop(0))
            self.players.append(Player('Player' + str(p), player_cards))

    def play(self):
        while (self.players):
            for player in self.players:
                player.play(self)
                if not player.playable:
                    if not player.cards:
                        self.winners.append(player)
                    self.players.remove(player)

    def __str__(self):
        player_list = ''
        for p in self.players:
            player_list = player_list + str(p) + '\n'
        return 'Cards: {cards}\n- Row_up_a: {row_up_a}\n- Row_up_b: {row_up_b}\n- Row_down_a: {row_down_a}\n- Row_down_b: {row_down_b}\n{players}'.format(
            cards=self.cards, row_up_a=self.rows['up_a'], row_up_b=self.rows['up_b'], row_down_a=self.rows['down_a'],
            row_down_b=self.rows['down_b'], players=player_list)
