import pytest
from src.reports.registry import get_report
from src.reports.average_gdp import AverageGDPReport

def test_registry_returns_correct_report():
    report = get_report("average-gdp")
    assert isinstance(report, AverageGDPReport)

def test_registry_raises_for_unknown_report():
    import pytest
    with pytest.raises(ValueError):
        get_report("unknown-report")
