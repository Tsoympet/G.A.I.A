import random

class MutationSuggester:
    def __init__(self, intelligence_engine, dream_state_engine):
        self.intelligence_engine = intelligence_engine
        self.dream_state_engine = dream_state_engine

    def suggest_mutations(self, context):
        suggestions = []

        # Gather insights from dream logs and performance metrics
        dream_insights = self.dream_state_engine.extract_insights(context)
        performance = self.intelligence_engine.evaluate_performance()

        if performance.get('stagnation_detected', False):
            suggestions.append({
                'type': 'neural',
                'description': 'Adjust learning rate to escape local minima.'
            })

        if 'pattern_recognition' in dream_insights:
            suggestions.append({
                'type': 'pattern_enhancement',
                'description': 'Refine pattern recognition for better long-term reasoning.'
            })

        if context.get('user_feedback', {}).get('confused', False):
            suggestions.append({
                'type': 'dialog_update',
                'description': 'Refine response phrasing to reduce ambiguity.'
            })

        if random.random() > 0.7:
            suggestions.append({
                'type': 'exploratory',
                'description': 'Introduce novelty to encourage creative behavior.'
            })

        return suggestions
