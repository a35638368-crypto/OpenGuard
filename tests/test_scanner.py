from openguard.scanner import Scanner


def test_scanner_exists():
    scanner = Scanner()
    assert scanner is not None
