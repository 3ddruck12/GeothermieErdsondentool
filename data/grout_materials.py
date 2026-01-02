"""Datenbank für Verfüllmaterialien."""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class GroutMaterial:
    """Verfüllmaterial mit Eigenschaften."""
    name: str
    thermal_conductivity: float  # W/m·K
    density: float  # kg/m³
    price_per_kg: float  # EUR/kg (optional)
    description: str
    typical_application: str


class GroutMaterialDB:
    """Datenbank für Verfüllmaterialien."""
    
    MATERIALS = {
        "Zement-Bentonit Standard": GroutMaterial(
            name="Zement-Bentonit Standard",
            thermal_conductivity=0.8,
            density=1800,
            price_per_kg=0.15,
            description="Standardmischung, kostengünstig",
            typical_application="Normale Böden, geringe Anforderungen"
        ),
        "Zement-Bentonit verbessert": GroutMaterial(
            name="Zement-Bentonit verbessert",
            thermal_conductivity=1.3,
            density=1900,
            price_per_kg=0.25,
            description="Verbesserte Wärmeleitfähigkeit",
            typical_application="Standardanwendung, gutes Preis-Leistungs-Verhältnis"
        ),
        "Thermisch optimiert (Sand)": GroutMaterial(
            name="Thermisch optimiert (Sand)",
            thermal_conductivity=1.8,
            density=2000,
            price_per_kg=0.35,
            description="Mit Quarzsand, hohe Wärmeleitfähigkeit",
            typical_application="Hohe Leistungsanforderungen"
        ),
        "Thermisch optimiert (Graphit)": GroutMaterial(
            name="Thermisch optimiert (Graphit)",
            thermal_conductivity=2.0,
            density=1950,
            price_per_kg=0.45,
            description="Mit Graphit-Zusatz, sehr hohe Wärmeleitfähigkeit",
            typical_application="Maximale Leistung, kompakte Systeme"
        ),
        "Hochleistung (Spezial)": GroutMaterial(
            name="Hochleistung (Spezial)",
            thermal_conductivity=2.5,
            density=2100,
            price_per_kg=0.60,
            description="Spezialmischung mit Hochleistungszusätzen",
            typical_application="Extreme Anforderungen, schwierige Böden"
        ),
        "Reiner Bentonit": GroutMaterial(
            name="Reiner Bentonit",
            thermal_conductivity=0.6,
            density=1400,
            price_per_kg=0.20,
            description="Nur Bentonit, niedrige Wärmeleitfähigkeit",
            typical_application="Temporäre Verfüllung, spezielle Anwendungen"
        ),
        "Zement-Bentonit mit Kies": GroutMaterial(
            name="Zement-Bentonit mit Kies",
            thermal_conductivity=1.5,
            density=2050,
            price_per_kg=0.28,
            description="Mit Kies-Anteil, gute Wärmeleitfähigkeit",
            typical_application="Stabile Böden, gute Leistung"
        ),
    }
    
    @classmethod
    def get_material(cls, name: str) -> GroutMaterial:
        """Holt ein Material nach Namen."""
        return cls.MATERIALS.get(name)
    
    @classmethod
    def get_all_names(cls) -> List[str]:
        """Gibt alle Materialnamen zurück."""
        return list(cls.MATERIALS.keys())
    
    @classmethod
    def get_all_materials(cls) -> Dict[str, GroutMaterial]:
        """Gibt alle Materialien zurück."""
        return cls.MATERIALS
    
    @staticmethod
    def calculate_volume(
        borehole_depth: float,
        borehole_diameter: float,
        pipe_outer_diameter: float,
        num_pipes: int = 4
    ) -> float:
        """
        Berechnet das benötigte Verfüllvolumen.
        
        Args:
            borehole_depth: Bohrtiefe in m
            borehole_diameter: Bohrloch-Durchmesser in m
            pipe_outer_diameter: Rohr-Außendurchmesser in m
            num_pipes: Anzahl Rohre (Standard: 4 für 4-Rohr-System)
            
        Returns:
            Volumen in m³
        """
        # Bohrloch-Volumen
        borehole_radius = borehole_diameter / 2
        borehole_volume = 3.14159 * (borehole_radius ** 2) * borehole_depth
        
        # Rohr-Volumen (Außenvolumen)
        pipe_radius = pipe_outer_diameter / 2
        pipe_volume = 3.14159 * (pipe_radius ** 2) * borehole_depth * num_pipes
        
        # Verfüllvolumen
        grout_volume = borehole_volume - pipe_volume
        
        # Sicherheitszuschlag 10%
        grout_volume_with_safety = grout_volume * 1.10
        
        return grout_volume_with_safety
    
    @staticmethod
    def calculate_material_amount(volume_m3: float, material: GroutMaterial) -> Dict[str, float]:
        """
        Berechnet die benötigte Materialmenge und Kosten.
        
        Args:
            volume_m3: Volumen in m³
            material: Verfüllmaterial
            
        Returns:
            Dictionary mit Mengen und Kosten
        """
        # Masse berechnen
        mass_kg = volume_m3 * material.density
        
        # Kosten berechnen
        total_cost = mass_kg * material.price_per_kg
        
        # Säcke (typisch 25 kg pro Sack)
        bags_25kg = mass_kg / 25
        
        return {
            'volume_m3': volume_m3,
            'mass_kg': mass_kg,
            'bags_25kg': bags_25kg,
            'total_cost_eur': total_cost,
            'cost_per_m': total_cost / (volume_m3 * 100) if volume_m3 > 0 else 0  # EUR/m Bohrtiefe
        }


if __name__ == "__main__":
    # Test
    import sys
    # Erzwinge UTF-8 Encoding für Ausgabe (Windows-Kompatibilität)
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')
    
    db = GroutMaterialDB()
    
    print("Verfügbare Materialien:")
    for name, mat in db.get_all_materials().items():
        print(f"\n{name}:")
        print(f"  lambda = {mat.thermal_conductivity} W/m·K")
        print(f"  rho = {mat.density} kg/m³")
        print(f"  Preis: {mat.price_per_kg} EUR/kg")
        print(f"  {mat.description}")
    
    # Beispielberechnung
    print("\n" + "="*60)
    print("Beispielberechnung: 100m Bohrung, Ø 152mm, 4 Rohre Ø 32mm")
    volume = db.calculate_volume(100, 0.152, 0.032, 4)
    print(f"Benötigtes Volumen: {volume:.3f} m³")
    
    material = db.get_material("Zement-Bentonit verbessert")
    amounts = db.calculate_material_amount(volume, material)
    
    print(f"\nMaterial: {material.name}")
    print(f"  Masse: {amounts['mass_kg']:.1f} kg")
    print(f"  Säcke (25kg): {amounts['bags_25kg']:.1f}")
    print(f"  Kosten gesamt: {amounts['total_cost_eur']:.2f} EUR")
    print(f"  Kosten pro Meter: {amounts['cost_per_m']:.2f} EUR/m")

