
## Estructura del Proyecto

### 1️⃣ Herencia y Polimorfismo (25 pts)

**Archivo:** `app.py` (líneas ~7-44)

**Implementación:**
- **Clase Base Abstracta:** `Flight` (abstracta)
  - Define atributos: origin, destination, distance_km, duration_min
  - Define método abstracto: `base_cost()`
  - Define método concreto polimórfico: `calculate_cost()`, `show_details()`

- **Subclases Concretas:**
  - `EconomyFlight`: base_cost = 0.25 * km + 0.5 * duration + 50.0
  - `BusinessFlight`: base_cost = 0.6 * km + 1.0 * duration + 200.0
  - `LowCostFlight`: base_cost = (0.18 * km + 0.4 * duration + 30.0) * 0.9

**Polimorfismo:** El método `calculate_cost()` devuelve resultados diferentes según la subclase, aunque la llamada sea idéntica.

---

### 2️⃣ Patrón Singleton (25 pts)

**Archivo:** `app.py` (líneas ~47-62)

**Implementación:**
- **Metaclase:** `SingletonMeta` asegura una única instancia en `_instances` (diccionario de clase)
- **Clase:** `Config` garantiza que solo exista una instancia global
  - Atributos: `demand_multiplier`, `base_speed_kmh`

**Uso:** Se accede con `Config()` desde cualquier parte del código. Cualquier cambio en `demand_multiplier` afecta globalmente a `PeakDemandStrategy`.

---

### 3️⃣ Patrón Strategy (25 pts)

**Archivo:** `app.py` (líneas ~65-88)

**Implementación (sin if/switch):**
- **Interfaz:** `PricingStrategy` (abstracta) con método `adjust(base_cost, flight)`
- **Estrategias Concretas:**
  - `NullStrategy`: devuelve base_cost sin cambios
  - `PeakDemandStrategy`: multiplica por `Config().demand_multiplier` (ej: 1.25)
  - `PromoDiscountStrategy`: aplica descuento (ej: 15%)

**Sin condicionales:** Las estrategias se asignan mediante un diccionario `strategy_map` que mapea tipos de vuelo a objetos estrategia.

---

### 4️⃣ Integración y Ejecución (25 pts)

**Archivo:** `app.py` (líneas ~91-135)

**Flujo:**

1. **Inicializa Singleton:** `cfg = Config(); cfg.demand_multiplier = 1.25`
   - Configuración global lista

2. **Define rutas:** Argentina → Brazil, Chile, Uruguay, Spain
   - Calcula duración estimada: duration = distance / 900 km/h

3. **Crea estrategias:** 
   - `null` (sin ajuste)
   - `peak` (demanda pico, lee Config)
   - `promo` (descuento 15%)

4. **Asigna estrategias sin if/switch:**
   ```python
   strategy_map = {EconomyFlight: null, BusinessFlight: peak, LowCostFlight: promo}
   for f in flights:
       f.set_pricing_strategy(strategy_map[type(f)])
   ```

5. **Imprime resultados:** Muestra costo base → costo ajustado por estrategia

---

## Cómo Ejecutar

**Desde PowerShell (carpeta practicaFede):**

```powershell
python .\main\app.py
```

**Salida esperada:**
```
rideSHare - Argentina -> Brazil
EconomyFlight - Argentina -> Brazil | 2030 km, 135 min, costo: 625.17
BusinessFlight - Argentina -> Brazil | 2030 km, 135 min, costo: 1941.66
LowCostFlight - Argentina -> Brazil | 2030 km, 135 min, costo: 343.89
---
```

---

## Concepto Clave: Sin if/Switch en Strategy

El patrón Strategy se implementa usando un **diccionario de mapeo** (`strategy_map`) que enlaza tipos de vuelo directamente con objetos estrategia. Esto elimina condicionales y permite agregar nuevas estrategias sin modificar el código existente (Principio Open/Closed).

---

## Archivo Principal
- **`app.py`**: Contiene todas las clases y la ejecución integrada

---

## Notas Finales
- Los comentarios en el código incluyen solo los números de consigna (1️⃣ 2️⃣ 3️⃣ 4️⃣) donde aplica cada patrón
- El proyecto es completamente funcional y modular
- Cambiar `cfg.demand_multiplier` afecta todos los vuelos con `PeakDemandStrategy`
