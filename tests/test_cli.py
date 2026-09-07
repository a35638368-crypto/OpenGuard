from openguard.scanner import Scanner


def test_scanner_returns_report():
    report = Scanner().run()
    assert "OpenGuard Security Report" in report
