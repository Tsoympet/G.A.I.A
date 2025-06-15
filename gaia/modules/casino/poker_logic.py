import random

class PokerHandEvaluator:
    def __init__(self):
        self.ranks = '23456789TJQKA'
        self.suits = 'β™ β™¥β™¦β™£'

    def generate_hand(self):
        deck = [r + s for r in self.ranks for s in self.suits]
        random.shuffle(deck)
        return deck[:5]

    def evaluate_hand(self, hand):
        values = sorted([self.ranks.index(card[0]) for card in hand], reverse=True)
        suits = [card[1] for card in hand]
        flush = len(set(suits)) == 1
        straight = all(values[i] - 1 == values[i + 1] for i in range(4))
        counts = {v: values.count(v) for v in values}
        unique_counts = sorted(counts.values(), reverse=True)

        if straight and flush:
            return "Straight Flush"
        elif unique_counts == [4, 1]:
            return "Four of a Kind"
        elif unique_counts == [3, 2]:
            return "Full House"
        elif flush:
            return "Flush"
        elif straight:
            return "Straight"
        elif unique_counts == [3, 1, 1]:
            return "Three of a Kind"
        elif unique_counts == [2, 2, 1]:
            return "Two Pair"
        elif unique_counts == [2, 1, 1, 1]:
            return "One Pair"
        else:
            return "High Card"

# Example usage
if __name__ == "__main__":
    evaluator = PokerHandEvaluator()
    hand = evaluator.generate_hand()
    print("Hand:", hand)
    print("Evaluation:", evaluator.evaluate_hand(hand))
