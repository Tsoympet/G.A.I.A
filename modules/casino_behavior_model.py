import random
import time
from collections import deque

class CasinoBehaviorModel:
    def __init__(self, window_size=100):
        self.session_log = deque(maxlen=window_size)
        self.behavior_patterns = {}

    def record_game_event(self, game_name, outcome, bet_amount, user_emotion=None):
        event = {
            'time': time.time(),
            'game': game_name,
            'outcome': outcome,
            'bet': bet_amount,
            'emotion': user_emotion
        }
        self.session_log.append(event)
        self._analyze_behavior(event)

    def _analyze_behavior(self, event):
        game = event['game']
        if game not in self.behavior_patterns:
            self.behavior_patterns[game] = {'win_rate': 0.0, 'avg_bet': 0.0, 'emotions': []}

        game_data = [e for e in self.session_log if e['game'] == game]
        wins = sum(1 for e in game_data if e['outcome'] == 'win')
        total = len(game_data)
        avg_bet = sum(e['bet'] for e in game_data) / total

        self.behavior_patterns[game]['win_rate'] = wins / total
        self.behavior_patterns[game]['avg_bet'] = avg_bet
        if event['emotion']:
            self.behavior_patterns[game]['emotions'].append(event['emotion'])

    def get_behavior_profile(self, game_name):
        return self.behavior_patterns.get(game_name, {})

    def suggest_strategy(self, game_name):
        profile = self.get_behavior_profile(game_name)
        if not profile:
            return "No data available for this game."
        if profile['win_rate'] < 0.4:
            return "Consider changing strategy or switching games."
        elif profile['win_rate'] > 0.6:
            return "Your current strategy appears successful."
        return "Maintain cautious play and monitor performance."

    def recent_emotion_trends(self, game_name):
        profile = self.get_behavior_profile(game_name)
        emotions = profile.get('emotions', [])
        return emotions[-5:] if emotions else []
