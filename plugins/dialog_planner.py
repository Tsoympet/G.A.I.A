class DialogPlanner:
    def __init__(self, persona="GAIA", tone="neutral", style="concise"):
        self.persona = persona
        self.tone = tone
        self.style = style

    def plan_response(self, intent, emotional_context=None):
        base = f"[{self.persona}] "
        if intent == "greeting":
            return base + self._apply_style("Hello. How can I assist you today?", emotional_context)
        elif intent == "farewell":
            return base + self._apply_style("Goodbye. I'm here whenever you need.", emotional_context)
        elif intent == "financial_help":
            return base + self._apply_style("Let's look into the financial data and insights.", emotional_context)
        elif intent == "casino_mode":
            return base + self._apply_style("Entering casino insight mode. Be mindful of your strategy.", emotional_context)
        else:
            return base + self._apply_style("I'm not sure how to respond to that, but I'm learning.", emotional_context)

    def _apply_style(self, text, emotion):
        if self.style == "concise":
            return text
        elif self.style == "friendly":
            return text + " π"
        elif emotion:
            return f"{text} (Feeling: {emotion})"
        return text
