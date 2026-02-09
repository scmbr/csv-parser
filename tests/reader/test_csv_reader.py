import pytest
from pathlib import Path
from src.reader.csv_reader import read_csv_files
from src.models.record import Record


def test_csv_reader_reads_records():
    path = Path(__file__).parent.parent / "fixtures" / "sample.csv"

    records = list(read_csv_files([str(path)]))

    assert len(records) == 39
    assert isinstance(records[0], Record)
    assert records[0].country == "United States"
    assert records[0].gdp == 25462


def test_csv_reader_empty_file():
    path = Path(__file__).parent.parent / "fixtures" / "empty.csv"

    records = list(read_csv_files([str(path)]))

    assert records == []

def test_average_gdp_single_row():
    path = Path(__file__).parent.parent / "fixtures" / "single_row.csv"

    records = list(read_csv_files([str(path)]))

    assert len(records) == 1
    assert isinstance(records[0], Record)
    assert records[0].country == "United States"
    assert records[0].gdp == 25462

def test_csv_reader_bad_data_raises():
    path = Path(__file__).parent.parent / "fixtures" / "bad_data.csv"

    with pytest.raises(ValueError):
        list(read_csv_files([str(path)]))