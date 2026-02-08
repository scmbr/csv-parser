from typing import List
import sys

from src.cli import parse_args
from src.reader.csv_reader import read_csv_files
from src.models.record import Record
from src.reports.registry import get_report
from src.output.table import print_table

def main() -> None:

    args = parse_args()  


    try:
        records: List[Record] = list(read_csv_files(args.files))
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Непредвиденная ошибка при чтении CSV: {e}", file=sys.stderr)
        sys.exit(1)

    if not records:
        print("Нет данных для обработки", file=sys.stderr)
        sys.exit(1)

    try:
        report = get_report(args.report)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

       
    table_data = report.generate(records)


    print_table(table_data)

if __name__ == "__main__":
    main()
