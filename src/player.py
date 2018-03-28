class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.playable = True

    def play(self, board):
        removed_cards = 0

        for m in range(board.PLAYER_MOVEMENTS):

            movements = {}

            for card in self.cards:
                # Look for range aumenters
                if (board.rows['up_a'][-1] == card + 10):
                    self.cards.remove(card)
                    board.rows['up_a'].append(card)
                    removed_cards += 1
                elif (board.rows['up_b'][-1] == card + 10):
                    self.cards.remove(card)
                    board.rows['up_b'].append(card)
                    removed_cards += 1
                elif (board.rows['down_a'][-1] == card - 10):
                    self.cards.remove(card)
                    board.rows['down_a'].append(card)
                    removed_cards += 1
                elif (board.rows['down_b'][-1] == card - 10):
                    self.cards.remove(card)
                    board.rows['down_b'].append(card)
                    removed_cards += 1
                else:
                    movements[card] = {}
                    if (board.rows['up_a'][-1] < card):
                        movements[card]['up_a'] = abs((card - board.rows['up_a'][-1]))
                    if (board.rows['up_b'][-1] < card):
                        movements[card]['up_b'] = abs((card - board.rows['up_b'][-1]))
                    if (board.rows['down_a'][-1] > card):
                        movements[card]['down_a'] = abs((board.rows['down_a'][-1] - card))
                    if (board.rows['down_b'][-1] > card):
                        movements[card]['down_b'] = abs((board.rows['down_b'][-1] - card))

            # Look for all cards the minimun

            min = board.MAX_NUMBER
            min_card = -1
            min_row = ''

            for card in movements:
                for row in movements[card]:
                    if movements[card][row] < min:
                        min = movements[card][row]
                        min_card = card
                        min_row = row

            if min != board.MAX_NUMBER:
                self.cards.remove(min_card)
                board.rows[min_row].append(min_card)
                removed_cards += 1

        print board
        if removed_cards == 0:
            self.playable = False
        else:
            for r in xrange(removed_cards):
                if board.cards:
                    self.cards.append(board.cards.pop(0))

    def __str__(self):
        return '+ {name}: {cards}'.format(name=self.name, cards=self.cards)
