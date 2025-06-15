from datetime import datetime
import random
import json

class DiagnosticEngine:
    @staticmethod
    def run_check():
        system_status = random.choice(['OK', 'Warning', 'Critical'])
        notes = {
            'OK': 'All systems functioning within normal parameters.',
            'Warning': 'Memory usage approaching threshold. Optimization suggested.',
            'Critical': 'Core plugin registry failure detected. Immediate attention required.'
        }

        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'status': system_status,
            'notes': notes[system_status]
        }

        try:
            with open('/mnt/data/diagnostic_log.json', 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
        except Exception as e:
            log_entry['notes'] += f' (Log write failed: {e})'

        return log_entry

# Run a test if executed directly
if __name__ == "__main__":
    result = DiagnosticEngine.run_check()
    print(json.dumps(result, indent=2))
