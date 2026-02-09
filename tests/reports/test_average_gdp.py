from src.reports.average_gdp import AverageGDPReport
from src.models.record import Record


def test_average_gdp_calculation():
    records = [
        Record("USA", 2023, 25000, 2.0, 3.5, 4.0, 330, "North America"),
        Record("USA", 2022, 23000, 1.8, 4.0, 4.2, 329, "North America"),
        Record("China", 2023, 18000, 5.0, 2.5, 5.0, 1400, "Asia"),
    ]

    report = AverageGDPReport()
    table = report.generate(records)

    header, *rows = table

    assert header == ["Country", "Average GDP"]

    usa_row = next(row for row in rows if row[0] == "USA")
    china_row = next(row for row in rows if row[0] == "China")

    assert usa_row[1] == "24000.00"
    assert china_row[1] == "18000.00"
