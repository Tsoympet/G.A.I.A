import re

class SmartContractAuditor:
    def __init__(self, contract_code):
        self.contract_code = contract_code
        self.report = []

    def check_reentrancy(self):
        if "call.value" in self.contract_code or "send(" in self.contract_code:
            if "mutex" not in self.contract_code:
                self.report.append("β οΈ Possible reentrancy vulnerability: Missing reentrancy guard.")

    def check_visibility(self):
        pattern = re.compile(r"function\s+\w+\s*\([^)]*\)\s*{")
        matches = pattern.findall(self.contract_code)
        if matches:
            self.report.append("β οΈ Functions missing visibility specifiers detected.")

    def check_safe_math(self):
        if "SafeMath" not in self.contract_code:
            self.report.append("β οΈ Consider using SafeMath for secure arithmetic operations.")

    def check_upgradeability(self):
        if "delegatecall" in self.contract_code:
            self.report.append("β οΈ Upgradeable pattern (delegatecall) found. Ensure proxy patterns are safe.")

    def generate_report(self):
        self.check_reentrancy()
        self.check_visibility()
        self.check_safe_math()
        self.check_upgradeability()
        if not self.report:
            self.report.append("β… No common vulnerabilities detected.")
        return self.report

# Example usage:
# auditor = SmartContractAuditor(contract_code)
# print("\n".join(auditor.generate_report()))
