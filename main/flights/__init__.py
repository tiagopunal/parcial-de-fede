from abc import ABC, abstractmethod


# Herencia y Polimorfismo
class Flight(ABC):
    def __init__(self, origin: str, destination: str, distance_km: float, duration_min: float):
        self.origin = origin
        self.destination = destination
        self.distance = distance_km
        self.duration = duration_min
        self.pricing_strategy = None

    def set_pricing_strategy(self, strategy):
        self.pricing_strategy = strategy

    @abstractmethod
    def base_cost(self) -> float:
        pass

    def calculate_cost(self) -> float:
        base = round(self.base_cost(), 2)
        return self.pricing_strategy.adjust(base, self)

    def show_details(self) -> str:
        return f"{self.__class__.__name__} - {self.origin} -> {self.destination} | {self.distance} km, {self.duration:.0f} min, costo: {self.calculate_cost():.2f}"


class EconomyFlight(Flight):
    def base_cost(self) -> float:
        return 0.25 * self.distance + 0.5 * self.duration + 50.0


class BusinessFlight(Flight):
    def base_cost(self) -> float:
        return 0.6 * self.distance + 1.0 * self.duration + 200.0


class LowCostFlight(Flight):
    def base_cost(self) -> float:
        return (0.18 * self.distance + 0.4 * self.duration + 30.0) * 0.9
