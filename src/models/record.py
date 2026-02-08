from dataclasses import dataclass


@dataclass(frozen=True)
class Record:
    country: str
    year: int
    gdp: float
    gdp_growth: float
    inflation: float
    unemployment: float
    population: int
    continent: str
