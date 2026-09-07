from datetime import datetime


def create_report(results):
    lines = [
        "# OpenGuard Security Report",
        f"Generated: {datetime.utcnow().isoformat()}Z",
        "",
    ]
    lines.extend(results)
    return "\n".join(lines)
