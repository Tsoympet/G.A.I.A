import re
import json
from collections import Counter

class PragmaticParser:
    def __init__(self):
        self.symbol_stats = Counter()
        self.feature_triggers = []
        self.rtp_logs = []

    def parse_log(self, session_log: str):
        """
        Parses a raw session log string from a Pragmatic Play game session.
        """
        symbols = re.findall(r'\[SYM:([A-Z0-9_]+)\]', session_log)
        features = re.findall(r'\[FEATURE:(.*?)\]', session_log)
        rtp_match = re.findall(r'RTP:([\d.]+)%', session_log)

        self.symbol_stats.update(symbols)
        self.feature_triggers.extend(features)
        self.rtp_logs.extend([float(r) for r in rtp_match])

    def summarize(self):
        """
        Returns a summary dictionary of session analysis.
        """
        avg_rtp = sum(self.rtp_logs) / len(self.rtp_logs) if self.rtp_logs else 0.0
        top_symbols = self.symbol_stats.most_common(5)
        top_features = Counter(self.feature_triggers).most_common(3)

        return {
            "average_rtp": round(avg_rtp, 2),
            "most_common_symbols": top_symbols,
            "most_common_features": top_features,
            "total_spins": sum(self.symbol_stats.values())
        }

    def export_json(self):
        """
        Returns the summary in JSON format.
        """
        return json.dumps(self.summarize(), indent=2)

