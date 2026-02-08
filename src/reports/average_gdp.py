from typing import Iterable, List
from collections import defaultdict
from src.models.record import Record
from .base import BaseReport

class AverageGDPReport(BaseReport):
    def generate(self, records: Iterable[Record]) -> List[List[str]]:
        gdp_data = defaultdict(lambda: {"sum": 0.0, "count": 0})

        for record in records:
            country_stats = gdp_data[record.country]
            country_stats["sum"] += record.gdp
            country_stats["count"] += 1

        table = []
        for country, stats in gdp_data.items():
            avg_gdp = stats["sum"] / stats["count"]
            table.append([country, f"{avg_gdp:.2f}"])


        table.sort(key=lambda x: float(x[1]), reverse=True)

  
        header = ["Country", "Average GDP"]
        return [header] + table
