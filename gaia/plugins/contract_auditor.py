import json
import re

class ContractAuditor:
    def __init__(self):
        self.warnings = []

    def audit(self, contract_code):
        self.warnings.clear()
        if "tx.origin" in contract_code:
            self.warnings.append("β οΈ Use of tx.origin is dangerous for authentication.")
        if "call.value" in contract_code:
            self.warnings.append("β οΈ Use of call.value can lead to reentrancy vulnerabilities.")
        if "delegatecall" in contract_code:
            self.warnings.append("β οΈ Use of delegatecall can lead to code injection vulnerabilities.")
        if re.search(r'assert\s*\(.*\)', contract_code):
            self.warnings.append("β οΈ Usage of assert may consume all gas on failure.")
        if "require" not in contract_code:
            self.warnings.append("β οΈ No require statements found. Validation may be weak.")
        return self.warnings

    def generate_report(self, contract_code):
        findings = self.audit(contract_code)
        return {
            "summary": f"{len(findings)} issues detected.",
            "issues": findings
        }

    def export_report(self, contract_code, filename="audit_report.json"):
        report = self.generate_report(contract_code)
        with open(filename, "w") as f:
            json.dump(report, f, indent=4)

