class Scanner:
    def run(self):
        checks = [
            "SSH configuration check: pending",
            "Port exposure check: pending",
            "Firewall check: pending",
        ]
        return "\n".join(checks)
