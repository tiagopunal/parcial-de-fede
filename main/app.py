from flights import EconomyFlight, BusinessFlight, LowCostFlight
from strategies import NullStrategy, PeakDemandStrategy, PromoDiscountStrategy
from config import Config


# Integración y Ejecución 
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
