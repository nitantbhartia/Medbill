"""Tests for appeal playbook generation."""

from analyzer import analyze_bill, save_bill_and_findings
from appeal_playbooks import generate_appeal_playbook
from tests.conftest import SAMPLE_BILL


class TestAppealPlaybooks:
    def test_generates_steps(self):
        analysis = analyze_bill(SAMPLE_BILL, "33021")
        bill_id = save_bill_and_findings(None, SAMPLE_BILL, analysis)
        playbook = generate_appeal_playbook(bill_id)
        assert playbook is not None
        assert playbook["bill_id"] == bill_id
        assert len(playbook["steps"]) > 0
