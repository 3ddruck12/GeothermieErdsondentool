"""Datenbank für Bodentypen mit typischen Werten."""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class SoilType:
    """Bodentyp mit thermischen Eigenschaften."""
    name: str
    thermal_conductivity_min: float  # W/m·K
    thermal_conductivity_max: float  # W/m·K
    thermal_conductivity_typical: float  # W/m·K
    heat_capacity_min: float  # MJ/m³·K
    heat_capacity_max: float  # MJ/m³·K
    heat_capacity_typical: float  # MJ/m³·K
    heat_extraction_rate_min: float  # W/m
    heat_extraction_rate_max: float  # W/m
    description: str
    moisture_dependency: str


class SoilTypeDB:
    """Datenbank für Bodentypen nach VDI 4640."""
    
    SOIL_TYPES = {
        "Sand": SoilType(
            name="Sand",
            thermal_conductivity_min=0.3,
            thermal_conductivity_max=2.4,
            thermal_conductivity_typical=1.8,
            heat_capacity_min=2.0,
            heat_capacity_max=2.8,
            heat_capacity_typical=2.4,
            heat_extraction_rate_min=40,
            heat_extraction_rate_max=80,
            description="Sand, trocken bis wassergesättigt",
            moisture_dependency="Stark abhängig von Wassergehalt"
        ),
        "Lehm": SoilType(
            name="Lehm",
            thermal_conductivity_min=1.1,
            thermal_conductivity_max=1.8,
            thermal_conductivity_typical=1.5,
            heat_capacity_min=2.0,
            heat_capacity_max=2.8,
            heat_capacity_typical=2.4,
            heat_extraction_rate_min=35,
            heat_extraction_rate_max=55,
            description="Lehm, feuchter Zustand",
            moisture_dependency="Mittlere Abhängigkeit vom Wassergehalt"
        ),
        "Schluff": SoilType(
            name="Schluff",
            thermal_conductivity_min=1.0,
            thermal_conductivity_max=1.9,
            thermal_conductivity_typical=1.4,
            heat_capacity_min=2.0,
            heat_capacity_max=2.6,
            heat_capacity_typical=2.3,
            heat_extraction_rate_min=30,
            heat_extraction_rate_max=60,
            description="Schluff, feinkörnig",
            moisture_dependency="Stark abhängig von Wassergehalt"
        ),
        "Sandigerton und Kalkstein": SoilType(
            name="Sandigerton und Kalkstein",
            thermal_conductivity_min=2.2,
            thermal_conductivity_max=2.8,
            thermal_conductivity_typical=2.5,
            heat_capacity_min=2.2,
            heat_capacity_max=2.8,
            heat_capacity_typical=2.5,
            heat_extraction_rate_min=55,
            heat_extraction_rate_max=70,
            description="Sandiger Ton mit Kalkstein, kompakt",
            moisture_dependency="Geringe Abhängigkeit vom Wassergehalt"
        ),
        "Mergelstein/Kalkstein": SoilType(
            name="Mergelstein/Kalkstein",
            thermal_conductivity_min=2.5,
            thermal_conductivity_max=4.0,
            thermal_conductivity_typical=3.2,
            heat_capacity_min=2.4,
            heat_capacity_max=2.8,
            heat_capacity_typical=2.6,
            heat_extraction_rate_min=60,
            heat_extraction_rate_max=80,
            description="Festgestein, hohe Wärmeleitfähigkeit",
            moisture_dependency="Sehr geringe Abhängigkeit"
        ),
        "Granit/Gneis": SoilType(
            name="Granit/Gneis",
            thermal_conductivity_min=2.9,
            thermal_conductivity_max=4.1,
            thermal_conductivity_typical=3.5,
            heat_capacity_min=2.2,
            heat_capacity_max=2.7,
            heat_capacity_typical=2.4,
            heat_extraction_rate_min=65,
            heat_extraction_rate_max=85,
            description="Kristallines Festgestein",
            moisture_dependency="Keine Abhängigkeit"
        ),
        "Basalt": SoilType(
            name="Basalt",
            thermal_conductivity_min=1.7,
            thermal_conductivity_max=2.5,
            thermal_conductivity_typical=2.1,
            heat_capacity_min=2.1,
            heat_capacity_max=2.6,
            heat_capacity_typical=2.3,
            heat_extraction_rate_min=50,
            heat_extraction_rate_max=70,
            description="Vulkanisches Gestein",
            moisture_dependency="Keine Abhängigkeit"
        ),
        "Sandstein": SoilType(
            name="Sandstein",
            thermal_conductivity_min=2.3,
            thermal_conductivity_max=2.8,
            thermal_conductivity_typical=2.5,
            heat_capacity_min=2.2,
            heat_capacity_max=2.6,
            heat_capacity_typical=2.4,
            heat_extraction_rate_min=55,
            heat_extraction_rate_max=75,
            description="Sedimentgestein",
            moisture_dependency="Geringe Abhängigkeit"
        ),
        "Ton (trocken)": SoilType(
            name="Ton (trocken)",
            thermal_conductivity_min=0.5,
            thermal_conductivity_max=1.0,
            thermal_conductivity_typical=0.8,
            heat_capacity_min=1.8,
            heat_capacity_max=2.3,
            heat_capacity_typical=2.0,
            heat_extraction_rate_min=20,
            heat_extraction_rate_max=35,
            description="Ton, trockener Zustand, ungünstig",
            moisture_dependency="Sehr stark abhängig"
        ),
        "Ton (feucht)": SoilType(
            name="Ton (feucht)",
            thermal_conductivity_min=1.1,
            thermal_conductivity_max=1.7,
            thermal_conductivity_typical=1.4,
            heat_capacity_min=2.0,
            heat_capacity_max=2.6,
            heat_capacity_typical=2.3,
            heat_extraction_rate_min=35,
            heat_extraction_rate_max=50,
            description="Ton, feuchter Zustand",
            moisture_dependency="Stark abhängig"
        ),
        "Kies (wasserführend)": SoilType(
            name="Kies (wasserführend)",
            thermal_conductivity_min=1.6,
            thermal_conductivity_max=2.5,
            thermal_conductivity_typical=2.0,
            heat_capacity_min=2.2,
            heat_capacity_max=2.8,
            heat_capacity_typical=2.5,
            heat_extraction_rate_min=80,
            heat_extraction_rate_max=100,
            description="Kies mit Grundwasser, sehr günstig",
            moisture_dependency="Optimal bei Wassersättigung"
        ),
    }
    
    @classmethod
    def get_soil_type(cls, name: str) -> SoilType:
        """Holt einen Bodentyp nach Namen."""
        return cls.SOIL_TYPES.get(name)
    
    @classmethod
    def get_all_names(cls) -> List[str]:
        """Gibt alle Bodentypnamen zurück."""
        return list(cls.SOIL_TYPES.keys())
    
    @classmethod
    def get_all_soil_types(cls) -> Dict[str, SoilType]:
        """Gibt alle Bodentypen zurück."""
        return cls.SOIL_TYPES
    
    @staticmethod
    def estimate_ground_temperature(
        avg_air_temp: float,
        coldest_month_temp: float
    ) -> float:
        """
        Schätzt die ungestörte Bodentemperatur basierend auf Lufttemperaturen.
        
        Args:
            avg_air_temp: Durchschnittliche Jahreslufttemperatur in °C
            coldest_month_temp: Durchschnittstemperatur des kältesten Monats in °C
            
        Returns:
            Geschätzte Bodentemperatur in 10-15m Tiefe in °C
        """
        # Faustformel: Bodentemperatur ≈ Jahresmitteltemperatur + 1-2°C
        ground_temp = avg_air_temp + 1.5
        
        return ground_temp


if __name__ == "__main__":
    # Test
    db = SoilTypeDB()
    
    print("Verfügbare Bodentypen:")
    print("=" * 80)
    
    for name, soil in db.get_all_soil_types().items():
        print(f"\n{name}:")
        print(f"  λ: {soil.thermal_conductivity_min}-{soil.thermal_conductivity_max} W/m·K (typ: {soil.thermal_conductivity_typical})")
        print(f"  c: {soil.heat_capacity_min}-{soil.heat_capacity_max} MJ/m³·K (typ: {soil.heat_capacity_typical})")
        print(f"  Wärmeentzug: {soil.heat_extraction_rate_min}-{soil.heat_extraction_rate_max} W/m")
        print(f"  {soil.description}")
    
    # Beispiel Temperaturschätzung
    print("\n" + "="*80)
    print("Temperaturschätzung:")
    ground_temp = db.estimate_ground_temperature(10.0, 2.0)
    print(f"Bei 10°C Jahresmittel und 2°C im kältesten Monat:")
    print(f"Geschätzte Bodentemperatur: {ground_temp:.1f}°C")

