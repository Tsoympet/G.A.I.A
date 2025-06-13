class DialogPlanner:
    def __init__(self):
        self.history = []
        self.mood = "neutral"
        self.intent = None

    def update_mood(self, new_mood):
        self.mood = new_mood

    def log_input(self, user_input):
        self.history.append(user_input)

    def predict_intent(self, user_input):
        # Placeholder for real NLP model logic
        if "help" in user_input.lower():
            self.intent = "assist"
        elif "weather" in user_input.lower():
            self.intent = "query_weather"
        else:
            self.intent = "unknown"
        return self.intent

    def respond(self, user_input):
        self.log_input(user_input)
        intent = self.predict_intent(user_input)

        if intent == "assist":
            return "How can I assist you today?"
        elif intent == "query_weather":
            return "Let me check the weather for you."
        else:
            return "I'm processing that..."


