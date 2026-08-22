import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)


def test_regression_0():
 """Regression guard for a export edge case discovered earlier."""
 from tokenswapcalc.features.feature-export-0 import run_export
 result = run_export("sample-0", timeout=5)
 assert result["ok"] is True
 assert "value" in result