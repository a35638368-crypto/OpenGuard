# OpenGuard

A lightweight open-source server security scanner for developers and small teams.

OpenGuard helps identify common server configuration risks through an extensible command-line security auditing framework.

## Features

- SSH configuration checks
- Exposed port detection
- Firewall status checks
- Markdown security reports
- Extensible security rules
- Automated testing with GitHub Actions

## Quick Start

```bash
pip install openguard
```

Run a scan:

```bash
openguard scan
```

Example output:

```text
OpenGuard Security Report
========================

[PASS] SSH configuration
[WARN] Port exposure detected
[PASS] Firewall status
```

## Development

Clone the repository:

```bash
git clone https://github.com/a35638368-crypto/OpenGuard.git
cd OpenGuard
```

Install development dependencies:

```bash
pip install -e .
```

Run tests:

```bash
pytest
```

## Roadmap

- Add Docker security checks
- Add JSON and HTML reports
- Add vulnerability database integration
- Improve CI security scanning

## Security

See `SECURITY.md` for responsible vulnerability reporting.

## License

MIT License
