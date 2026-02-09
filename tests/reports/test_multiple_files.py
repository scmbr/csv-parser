from pathlib import Path
from src.reader.csv_reader import read_csv_files
from src.reports.average_gdp import AverageGDPReport


def test_average_gdp_multiple_files():
    base = Path(__file__).parent.parent / "fixtures"

    files = [
        str(base / "multiple_first.csv"),
        str(base / "multiple_second.csv"),
    ]

    records = list(read_csv_files(files))
    report = AverageGDPReport()
    table = report.generate(records)

    countries = [row[0] for row in table[1:]]

    assert "China" in countries
    assert "Netherlands" in countries
