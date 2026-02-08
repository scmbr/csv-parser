from typing import List
from tabulate import tabulate


def print_table(table_data: List[List[str]]) -> None:
    if not table_data:
        print("Нет данных для отображения")
        return

    headers = table_data[0]
    rows = table_data[1:] if len(table_data) > 1 else []

    print(tabulate(rows, headers=headers, tablefmt="grid"))
