# OpenGuard Security Rules

This document describes the design principles for OpenGuard security checks.

## Rule Categories

### SSH

Checks common SSH hardening recommendations:

- Avoid unsafe remote access settings
- Detect risky authentication configuration
- Encourage secure administration practices

### Network

Network checks focus on identifying unnecessary exposure:

- Unexpected listening ports
- Publicly exposed services
- Potential attack surface expansion

### Firewall

Firewall checks verify whether basic host protection is enabled.

## Future Rules

Planned extensions:

- Docker configuration checks
- CVE metadata integration
- Container security checks
- Custom user-defined rules
