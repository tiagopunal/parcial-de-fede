from abc import ABC, abstractmethod
from config import Config


# Patrón Strategy
class PricingStrategy(ABC):
    @abstractmethod
    def adjust(self, base_cost: float, flight) -> float:
        pass


class NullStrategy(PricingStrategy):
    def adjust(self, base_cost: float, flight) -> float:
        return base_cost


class PeakDemandStrategy(PricingStrategy):
    def adjust(self, base_cost: float, flight) -> float:
        cfg = Config()
        return round(base_cost * cfg.demand_multiplier, 2)


class PromoDiscountStrategy(PricingStrategy):
    def __init__(self, discount_pct: float):
        self.discount_pct = discount_pct

    def adjust(self, base_cost: float, flight) -> float:
        return round(base_cost * (1 - self.discount_pct), 2)
