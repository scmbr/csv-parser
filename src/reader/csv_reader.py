import csv
from pathlib import Path
from typing import Iterable, List

from src.models.record import Record


def read_csv_files(file_paths: List[str]) -> Iterable[Record]:
    for file_path in file_paths:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        with path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
             
                    record = Record(
                        country=row["country"],
                        year=int(row["year"]),
                        gdp=float(row["gdp"]),
                        gdp_growth=float(row["gdp_growth"]),
                        inflation=float(row["inflation"]),
                        unemployment=float(row["unemployment"]),
                        population=int(row["population"]),
                        continent=row["continent"]
                    )
                    yield record
                except KeyError as e:
                  
                    raise ValueError(f"Отсутствует колонка {e} в файле {file_path}")
                except ValueError as e:
                    raise ValueError(f"Ошибка обработки строки в файле {file_path}: {e}")
