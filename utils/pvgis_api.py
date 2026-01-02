"""PVGIS API Integration für Klimadaten.

PVGIS (Photovoltaic Geographical Information System) der EU bietet
kostenlose Klimadaten für Europa und weitere Regionen.

https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis_en
"""

import requests
import json
from typing import Dict, Optional, Tuple


class PVGISClient:
    """Client für PVGIS API um Klimadaten abzurufen."""
    
    BASE_URL = "https://re.jrc.ec.europa.eu/api/v5_2"
    
    @staticmethod
    def get_monthly_temperature_data(
        latitude: float,
        longitude: float
    ) -> Optional[Dict]:
        """
        Holt monatliche Temperaturdaten von PVGIS.
        
        Args:
            latitude: Breitengrad (z.B. 51.5 für Deutschland)
            longitude: Längengrad (z.B. 10.0 für Deutschland)
            
        Returns:
            Dictionary mit Klimadaten oder None bei Fehler
            
        Hinweis:
            PVGIS bietet primär Solardaten. Für detaillierte Temperaturdaten
            sollten zusätzlich nationale Wetterdienste verwendet werden.
        """
        try:
            # TMY (Typical Meteorological Year) Daten abrufen
            url = f"{PVGISClient.BASE_URL}/tmy"
            
            params = {
                'lat': latitude,
                'lon': longitude,
                'outputformat': 'json',
                'browser': '0'
            }
            
            response = requests.get(url, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                return PVGISClient._process_tmy_data(data)
            else:
                print(f"PVGIS API Fehler: Status {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Netzwerkfehler bei PVGIS-Anfrage: {e}")
            return None
        except Exception as e:
            print(f"Fehler beim Abrufen von PVGIS-Daten: {e}")
            return None
    
    @staticmethod
    def _process_tmy_data(data: Dict) -> Dict:
        """
        Verarbeitet TMY-Daten von PVGIS.
        
        Extrahiert monatliche Durchschnittstemperaturen und andere relevante Daten.
        """
        try:
            # TMY enthält stündliche Daten für ein typisches Jahr
            hourly_data = data.get('outputs', {}).get('tmy_hourly', [])
            
            if not hourly_data:
                return None
            
            # Berechne monatliche Durchschnitte
            monthly_temps = [[] for _ in range(12)]
            
            for entry in hourly_data:
                month = int(entry.get('time(UTC)', '').split(':')[0].split('-')[1]) - 1
                temp = entry.get('T2m', 0)  # Temperatur in 2m Höhe
                if 0 <= month < 12:
                    monthly_temps[month].append(temp)
            
            # Durchschnitte berechnen
            avg_temps = []
            for temps in monthly_temps:
                if temps:
                    avg_temps.append(sum(temps) / len(temps))
                else:
                    avg_temps.append(0)
            
            # Jahrestemperatur
            all_temps = [t for month in monthly_temps for t in month]
            yearly_avg = sum(all_temps) / len(all_temps) if all_temps else 0
            
            # Kältester Monat
            coldest_month_temp = min(avg_temps) if avg_temps else 0
            coldest_month_idx = avg_temps.index(coldest_month_temp) if avg_temps else 0
            
            return {
                'monthly_avg_temps': avg_temps,
                'yearly_avg_temp': yearly_avg,
                'coldest_month_temp': coldest_month_temp,
                'coldest_month': coldest_month_idx + 1,
                'source': 'PVGIS TMY',
                'location': data.get('inputs', {}).get('location', {})
            }
            
        except Exception as e:
            print(f"Fehler beim Verarbeiten der PVGIS-Daten: {e}")
            return None
    
    @staticmethod
    def get_location_from_address(address: str) -> Optional[Tuple[float, float]]:
        """
        Konvertiert eine Adresse in Koordinaten (Geocoding).
        
        Hinweis: Dies erfordert einen Geocoding-Service wie OpenStreetMap Nominatim.
        Für Produktionsumgebungen sollte ein dedizierter Service verwendet werden.
        
        Args:
            address: Adresse als String
            
        Returns:
            Tuple (latitude, longitude) oder None
        """
        try:
            # OpenStreetMap Nominatim für Geocoding
            url = "https://nominatim.openstreetmap.org/search"
            
            params = {
                'q': address,
                'format': 'json',
                'limit': 1
            }
            
            headers = {
                'User-Agent': 'GeothermieErdsonden-Tool/2.0'
            }
            
            response = requests.get(url, params=params, headers=headers, timeout=10)
            
            if response.status_code == 200:
                results = response.json()
                if results:
                    lat = float(results[0]['lat'])
                    lon = float(results[0]['lon'])
                    return (lat, lon)
            
            return None
            
        except Exception as e:
            print(f"Fehler beim Geocoding: {e}")
            return None
    
    @staticmethod
    def get_climate_data_for_address(address: str) -> Optional[Dict]:
        """
        Convenience-Methode: Holt Klimadaten für eine Adresse.
        
        Args:
            address: Vollständige Adresse
            
        Returns:
            Dictionary mit Klimadaten oder None
        """
        coords = PVGISClient.get_location_from_address(address)
        
        if coords:
            lat, lon = coords
            print(f"Koordinaten gefunden: {lat:.4f}, {lon:.4f}")
            return PVGISClient.get_monthly_temperature_data(lat, lon)
        else:
            print("Koordinaten konnten nicht ermittelt werden")
            return None


# Beispieldaten für Deutschland (Fallback wenn PVGIS nicht erreichbar)
FALLBACK_CLIMATE_DATA = {
    "Deutschland Nord": {
        'monthly_avg_temps': [1.0, 1.5, 4.5, 8.5, 13.0, 16.0, 18.0, 17.5, 14.0, 9.5, 5.0, 2.0],
        'yearly_avg_temp': 9.2,
        'coldest_month_temp': 1.0,
        'coldest_month': 1
    },
    "Deutschland Süd": {
        'monthly_avg_temps': [-1.0, 0.5, 4.0, 8.5, 13.5, 16.5, 18.5, 18.0, 14.5, 9.0, 4.0, 0.5],
        'yearly_avg_temp': 8.8,
        'coldest_month_temp': -1.0,
        'coldest_month': 1
    },
    "Deutschland Mitte": {
        'monthly_avg_temps': [0.5, 1.5, 5.0, 9.0, 13.5, 16.5, 18.5, 18.0, 14.0, 9.5, 4.5, 1.5],
        'yearly_avg_temp': 9.3,
        'coldest_month_temp': 0.5,
        'coldest_month': 1
    },
    "Österreich": {
        'monthly_avg_temps': [-2.0, -0.5, 4.0, 9.0, 14.0, 17.0, 19.0, 18.5, 14.0, 8.5, 3.0, -1.0],
        'yearly_avg_temp': 8.6,
        'coldest_month_temp': -2.0,
        'coldest_month': 1
    },
    "Schweiz": {
        'monthly_avg_temps': [-1.5, 0.0, 4.5, 8.5, 13.0, 16.0, 18.0, 17.5, 13.5, 8.5, 3.5, -0.5],
        'yearly_avg_temp': 8.4,
        'coldest_month_temp': -1.5,
        'coldest_month': 1
    }
}


def get_climate_data(latitude: float, longitude: float) -> Optional[Dict]:
    """
    Convenience-Funktion für GUI: Holt Klimadaten für Koordinaten.
    
    Args:
        latitude: Breitengrad
        longitude: Längengrad
        
    Returns:
        Dictionary mit Klimadaten oder None
    """
    data = PVGISClient.get_monthly_temperature_data(latitude, longitude)
    
    if data:
        return {
            'avg_temp': data['yearly_avg_temp'],
            'coldest_month_temp': data['coldest_month_temp'],
            'monthly_temps': data['monthly_avg_temps']
        }
    
    return None


if __name__ == "__main__":
    # Test
    print("PVGIS API Test")
    print("=" * 60)
    
    # Teste mit Koordinaten (München)
    print("\n1. Test mit Koordinaten (München: 48.14, 11.58):")
    data = PVGISClient.get_monthly_temperature_data(48.14, 11.58)
    
    if data:
        print(f"Jahres-Durchschnittstemperatur: {data['yearly_avg_temp']:.1f}°C")
        print(f"Kältester Monat: {data['coldest_month']} ({data['coldest_month_temp']:.1f}°C)")
        print(f"Monatliche Temperaturen:")
        months = ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez']
        for month, temp in zip(months, data['monthly_avg_temps']):
            print(f"  {month}: {temp:.1f}°C")
    else:
        print("Keine Daten erhalten (offline oder Fehler)")
        print("Verwende Fallback-Daten für Deutschland Süd:")
        data = FALLBACK_CLIMATE_DATA["Deutschland Süd"]
        print(f"Jahres-Durchschnittstemperatur: {data['yearly_avg_temp']:.1f}°C")
    
    print("\n" + "=" * 60)
    print("PVGIS-Dokumentation:")
    print("https://joint-research-centre.ec.europa.eu/pvgis-photovoltaic-geographical-information-system_en")

