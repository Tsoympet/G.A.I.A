import random

class BaccaratGame:
    def __init__(self):
        self.deck = self._create_deck()
        random.shuffle(self.deck)

    def _create_deck(self):
        # 8 decks used in most Baccarat games
        deck = []
        for _ in range(8):
            for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
                for value in range(1, 14):  # Ace to King
                    if value >= 10:
                        points = 0
                    elif value == 1:
                        points = 1
                    else:
                        points = value
                    deck.append({'suit': suit, 'value': value, 'points': points})
        return deck

    def draw_card(self):
        if not self.deck:
            self.deck = self._create_deck()
            random.shuffle(self.deck)
        return self.deck.pop()

    def hand_score(self, hand):
        total = sum(card['points'] for card in hand)
        return total % 10

    def play_round(self):
        player_hand = [self.draw_card(), self.draw_card()]
        banker_hand = [self.draw_card(), self.draw_card()]

        player_score = self.hand_score(player_hand)
        banker_score = self.hand_score(banker_hand)

        if player_score > banker_score:
            result = "Player Wins"
        elif banker_score > player_score:
            result = "Banker Wins"
        else:
            result = "Tie"

        return {
            'player_hand': player_hand,
            'banker_hand': banker_hand,
            'player_score': player_score,
            'banker_score': banker_score,
            'result': result
        }
