from datetime import datetime

from .checks.ssh import check_ssh
from .checks.ports import check_ports
from .checks.firewall import check_firewall


class Scanner:
    def run(self):
        results = [
            check_ssh(),
            check_ports(),
            check_firewall(),
        ]

        return "\n".join(
            [
                "OpenGuard Security Report",
                "=" * 24,
                f"Generated: {datetime.now().isoformat(timespec='seconds')}",
                "",
                *results,
            ]
        )
