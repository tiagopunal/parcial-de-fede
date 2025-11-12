from abc import ABC, abstractmethod


# 1️⃣ Herencia y Polimorfismo
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


# 2️⃣ Patrón Singleton
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.demand_multiplier = 1.0
        self.base_speed_kmh = 900.0


# 3️⃣ Patrón Strategy
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


# 4️⃣ Integración y Ejecución
if __name__ == "__main__":
    cfg = Config()
    cfg.demand_multiplier = 1.25

    routes = [
        ("Argentina", "Brazil", 2030),
        ("Argentina", "Chile", 1140),
        ("Argentina", "Uruguay", 200),
        ("Argentina", "Spain", 10350),
    ]

    avg_speed = cfg.base_speed_kmh

    null = NullStrategy()
    peak = PeakDemandStrategy()
    promo = PromoDiscountStrategy(0.15)

    strategy_map = {EconomyFlight: null, BusinessFlight: peak, LowCostFlight: promo}

    for origin, dest, km in routes:
        duration_min = km / avg_speed * 60.0

        flights = [
            EconomyFlight(origin, dest, km, duration_min),
            BusinessFlight(origin, dest, km, duration_min),
            LowCostFlight(origin, dest, km, duration_min),
        ]

        for f in flights:
            f.set_pricing_strategy(strategy_map[type(f)])

        print(f"rideSHare - {origin} -> {dest}")
        for f in flights:
            print(f.show_details())
        print("---\n")
