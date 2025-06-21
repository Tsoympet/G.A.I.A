import datetime
import logging

class LegalComplianceChecker:
    def __init__(self):
        self.last_check = None
        self.warnings = []
        self.check_log = []

    def run_all_checks(self, context=None):
        self.last_check = datetime.datetime.now().isoformat()
        self.warnings.clear()
        self.check_log.clear()

        self._check_data_privacy(context)
        self._check_gambling_compliance(context)
        self._check_plugin_integrity(context)

        return {
            "status": "PASS" if not self.warnings else "WARNING",
            "warnings": self.warnings,
            "checked_at": self.last_check
        }

    def _check_data_privacy(self, context):
        if context and not context.get("user_consent", False):
            self.warnings.append("User data collection may lack proper consent.")
        self.check_log.append("Checked data privacy")

    def _check_gambling_compliance(self, context):
        if context and context.get("mode") == "casino":
            if not context.get("age_verified", False):
                self.warnings.append("Gambling features accessed without age verification.")
            if context.get("region") in ["DE", "FR", "CN"]:
                self.warnings.append(f"Gambling features restricted in region: {context.get('region')}")
        self.check_log.append("Checked gambling compliance")

    def _check_plugin_integrity(self, context):
        plugins = context.get("plugins", []) if context else []
        for plugin in plugins:
            if not plugin.get("signed", False):
                self.warnings.append(f"Unsigned plugin loaded: {plugin.get('name', 'unknown')}")
        self.check_log.append("Checked plugin integrity")

    def get_log(self):
        return self.check_log

    def get_warnings(self):
        return self.warnings

