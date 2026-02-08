import argparse
from typing import List, Namespace


def parse_args() -> Namespace:
    parser = argparse.ArgumentParser(
        description="Скрипт для анализа макроэкономических данных"
    )


    parser.add_argument(
        "--files",
        type=str,
        nargs="+",      
        required=True,
        help="Пути к CSV файлам с макроэкономическими данными"
    )


    parser.add_argument(
        "--report",
        type=str,
        required=True,
        help="Название отчёта (например, average-gdp)"
    )

    args = parser.parse_args()


    if not args.files:
        parser.error("Необходимо указать хотя бы один CSV файл через --files")

    if not args.report.strip():
        parser.error("Название отчёта не может быть пустым (--report)")

    return args


if __name__ == "__main__":
    args = parse_args()
    print(f"Файлы: {args.files}")
    print(f"Отчёт: {args.report}")
