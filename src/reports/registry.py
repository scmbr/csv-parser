from typing import Type
from .base import BaseReport
from .average_gdp import AverageGDPReport


REPORTS_REGISTRY: dict[str, Type[BaseReport]] = {
    "average-gdp": AverageGDPReport,
    # Можно добавлять новые отчёты:
    # "unemployment-trend": UnemploymentReport,
}

def get_report(name: str) -> BaseReport:

    report_class = REPORTS_REGISTRY.get(name)
    if report_class is None:
        raise ValueError(f"Отчёт '{name}' не найден. Доступные отчёты: {list(REPORTS_REGISTRY.keys())}")
    
    return report_class()  
