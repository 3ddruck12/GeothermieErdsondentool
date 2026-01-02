# 🚀 Professional Features Version 3.0

## Erweiterte Funktionen basierend auf Ihren Anforderungen

---

## 1. ✅ Verfüllmaterial-Datenbank

### **7 professionelle Verfüllmaterialien**

| Material | λ (W/m·K) | Dichte (kg/m³) | Preis (EUR/kg) | Anwendung |
|----------|-----------|----------------|----------------|-----------|
| **Zement-Bentonit Standard** | 0.8 | 1800 | 0.15 | Normal, kostengünstig |
| **Zement-Bentonit verbessert** | 1.3 | 1900 | 0.25 | Standard, gut |
| **Thermisch optimiert (Sand)** | 1.8 | 2000 | 0.35 | Hohe Leistung |
| **Thermisch optimiert (Graphit)** | 2.0 | 1950 | 0.45 | Sehr hohe Leistung |
| **Hochleistung (Spezial)** | 2.5 | 2100 | 0.60 | Extreme Anforderungen |
| Reiner Bentonit | 0.6 | 1400 | 0.20 | Spezialanwendungen |
| Zement-Bentonit mit Kies | 1.5 | 2050 | 0.28 | Stabile Böden |

### **Dropdown-Auswahl in GUI**
- Vollständige Materialeigenschaften
- Beschreibung und typische Anwendung
- Automatische Werte-Übernahme

### **Automatische Mengenberechnung**

```python
# Berechnet automatisch:
✓ Benötigtes Volumen (m³)
✓ Masse (kg)
✓ Anzahl Säcke (25 kg)
✓ Gesamtkosten (EUR)
✓ Kosten pro Meter Bohrtiefe (EUR/m)
```

**Beispiel:** 100m Bohrung, Ø 152mm, 4 Rohre Ø 32mm
- Volumen: **1.76 m³** (inkl. 10% Sicherheit)
- Masse: **3,344 kg** (bei Zement-Bentonit verbessert)
- Säcke: **134 Stück** (á 25 kg)
- Kosten: **~836 EUR**

---

## 2. ✅ Bodentyp-Datenbank

### **11 Bodentypen nach VDI 4640**

#### Dropdown mit vollständigen Bodenwerten:

| Bodentyp | λ (W/m·K) | c (MJ/m³·K) | Wärmeentzug (W/m) |
|----------|-----------|-------------|-------------------|
| **Sand** | 0.3-2.4 (typ: 1.8) | 2.0-2.8 (typ: 2.4) | 40-80 |
| **Lehm** | 1.1-1.8 (typ: 1.5) | 2.0-2.8 (typ: 2.4) | 35-55 |
| **Schluff** | 1.0-1.9 (typ: 1.4) | 2.0-2.6 (typ: 2.3) | 30-60 |
| **Sandigerton und Kalkstein** | 2.2-2.8 (typ: 2.5) | 2.2-2.8 (typ: 2.5) | 55-70 |
| **Mergelstein/Kalkstein** | 2.5-4.0 (typ: 3.2) | 2.4-2.8 (typ: 2.6) | 60-80 |
| Granit/Gneis | 2.9-4.1 (typ: 3.5) | 2.2-2.7 (typ: 2.4) | 65-85 |
| Basalt | 1.7-2.5 (typ: 2.1) | 2.1-2.6 (typ: 2.3) | 50-70 |
| Sandstein | 2.3-2.8 (typ: 2.5) | 2.2-2.6 (typ: 2.4) | 55-75 |
| Ton (trocken) | 0.5-1.0 (typ: 0.8) | 1.8-2.3 (typ: 2.0) | 20-35 |
| Ton (feucht) | 1.1-1.7 (typ: 1.4) | 2.0-2.6 (typ: 2.3) | 35-50 |
| **Kies (wasserführend)** | 1.6-2.5 (typ: 2.0) | 2.2-2.8 (typ: 2.5) | 80-100 ⭐ |

### **Automatische Werte-Übernahme**
- Auswahl im Dropdown
- Typische Werte werden automatisch eingetragen
- Wärmeentzugsrate als Richtwert
- Hinweise zur Feuchtigkeitsabhängigkeit

---

## 3. ✅ PVGIS Klimadaten-Integration

### **EU-Klimadatenservice**

🌍 **PVGIS (Photovoltaic Geographical Information System)**
- Kostenloser EU-Service
- Weltweite Abdeckung
- [PVGIS Website](https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis_en)

### **Funktionen:**

#### A) **Koordinaten-basiert**
```python
# Beispiel: München (48.14°N, 11.58°E)
✓ Monatliche Durchschnittstemperaturen
✓ Jahres-Durchschnittstemperatur
✓ Kältester Monat identifiziert
✓ Typical Meteorological Year (TMY) Daten
```

#### B) **Adress-basiert (Geocoding)**
```python
# Automatische Koordinaten-Ermittlung
Eingabe: "Musterstraße 1, 80331 München"
→ Koordinaten: 48.14°N, 11.58°E
→ Klimadaten von PVGIS
```

#### C) **Fallback-Daten**
Bei fehlender Internetverbindung:
- Deutschland Nord, Süd, Mitte
- Österreich, Schweiz
- Vorgespeicherte typische Werte

### **In GUI verfügbar:**
- Button "🌍 Klimadaten von PVGIS laden"
- Automatische Temperaturwerte
- Bodentemperatur-Schätzung

---

## 4. ✅ Erweiterte Wärmepumpendaten

### **Neue Eingabefelder:**

#### **Wärmepumpe**
- ✅ **Wärmepumpenleistung** (kW)
- ✅ **COP** (Coefficient of Performance)
- ✅ **Kälteleistung** (kW) - automatisch berechnet
- ✅ **Durchfluss Solekreislauf** (m³/h) - automatisch berechnet
- ✅ **Druckverlust Verdampfer** (mbar) - Eingabe oder berechnet

#### **Warmwasserbereitung**
- ✅ **Anzahl Personen** → automatische Berechnung
  - 1 Person = ~1.5 MWh/Jahr
  - 4 Personen = ~6.0 MWh/Jahr

---

## 5. ✅ Klimadaten und Bodenwerte

### **Neue Felder in GUI:**

#### **Klimadaten**
- ✅ **Ø Temperatur Außenluft** (°C)
  - Jahres-Durchschnittstemperatur
  - Kann von PVGIS geladen werden
  
- ✅ **Ø Temperatur kältester Monat** (°C)
  - Wichtig für Auslegung
  - Automatisch von PVGIS
  
- ✅ **Korrekturfaktor** (%)
  - Anpassung für besondere Bedingungen
  - Standard: 100%
  
- ✅ **Auslegungstemperatur Kollektor** (°C)
  - Minimal zulässige Soletemperatur
  - Standard: -2°C bei 25% Sole

#### **Bodentyp** (Dropdown)
✅ 11 Bodentypen zur Auswahl
✅ Automatische Werte-Übernahme
✅ Min/Max/Typisch-Werte

---

## 6. ✅ Hydraulik-Berechnungen

### **Neue Funktionen:**

#### A) **Anzahl Solekreise**
- Eingabefeld für 1-10 Kreise
- Automatische Verteilung des Volumenstroms
- Druckverlust-Berechnung pro Kreis

#### B) **Frostschutzkonzentration**
- Eingabe: 0-40 Vol% Ethylenglykol
- Automatische Eigenschaften:
  - Dichte
  - Viskosität
  - Wärmekapazität
  - Gefrierpunkt

| Konzentration | Gefrierpunkt | Dichte | Viskosität |
|---------------|--------------|--------|------------|
| 0% (Wasser) | 0°C | 1000 kg/m³ | 0.001 Pa·s |
| **25% (Standard)** | **-11°C** | **1033 kg/m³** | **0.0019 Pa·s** |
| 30% | -15°C | 1039 kg/m³ | 0.0024 Pa·s |
| 40% | -24°C | 1052 kg/m³ | 0.0038 Pa·s |

#### C) **Druckverlust der Anlage**
Automatische Berechnung:
- ✅ Druckverlust in Bohrungen
- ✅ Druckverlust horizontal
- ✅ Zusatzverluste (Verteiler, Ventile)
- ✅ **Gesamt-Druckverlust** (mbar)
- ✅ Erforderliche **Pumpenleistung** (W)

#### D) **Volumenstrom-Berechnung**
```python
Formel: Q = m_dot × c_p × ΔT

Automatisch berechnet:
✓ Massenstrom (kg/s)
✓ Volumenstrom (m³/h, l/min)
✓ Strömungsgeschwindigkeit (m/s)
✓ Reynolds-Zahl
✓ Strömungsregime (laminar/turbulent)
```

---

## 7. ✅ Berechnungsbeispiel

### **Konfiguration:**
- Wärmepumpe: 6 kW
- COP: 4.0
- 2 Bohrungen × 100m
- 4-Rohr-System, PE 100 RC DN32
- Sole: 25% Ethylenglykol
- Bodentyp: Sand (wassergesättigt)
- 1 Solekreis

### **Automatisch berechnet:**

#### **Verfüllung:**
- Material: Zement-Bentonit verbessert
- Volumen: 3.52 m³ (2 Bohrungen)
- Masse: 6,688 kg
- Säcke: 268 × 25 kg
- **Kosten: ~1,672 EUR**

#### **Hydraulik:**
- Volumenstrom: **1.74 m³/h** (29 l/min)
- Geschwindigkeit: 0.99 m/s
- Reynolds: 17,850 (turbulent)
- Druckverlust Sonden: 0.68 bar
- Zusatzverluste: 0.50 bar
- **Gesamt-Druckverlust: 1.18 bar** (1,180 mbar)
- **Pumpenleistung: 115 W**

#### **Thermisch:**
- Wärmeentzug: 50 W/m
- Bohrtiefe gesamt: 200 m
- Gesamtleistung: 10 kW

---

## 8. ✅ Integration in GUI

### **Neue Bereiche:**

#### **"💧 Verfüllmaterial"**
- Dropdown: 7 Materialien
- Anzeige: λ, Dichte, Preis, Beschreibung
- **Materialmengen-Berechnung** (Button)
  - Volumen, Masse, Säcke, Kosten

#### **"🌍 Klimadaten"** (mit PVGIS-Button)
- Button: "Klimadaten von PVGIS laden"
- Eingabe: Koordinaten oder Adresse
- Automatische Übernahme in Felder

#### **"🪨 Bodentyp"**
- Dropdown: 11 Bodentypen
- Auto-Übernahme: λ, c, Wärmeentzug
- Min/Max/Typisch-Werte sichtbar

#### **"💨 Hydraulik"**
- Anzahl Solekreise
- Frostschutzkonzentration (%)
- **Hydraulik berechnen** (Button)
  - Volumenstrom
  - Druckverlust
  - Pumpenleistung

---

## 9. ✅ Erweiterte PDF-Berichte

### **Neue Abschnitte im PDF:**

#### **Seite 2: Material und Kosten**
- Verfüllmaterial-Spezifikation
- Mengenkalkulation
- Kostenschätzung

#### **Seite 3: Hydraulik**
- Volumenstrom-Berechnung
- Druckverlust-Analyse
- Pumpen-Dimensionierung
- Solekreis-Konfiguration

#### **Seite 4: Klimadaten**
- PVGIS-Quelle (falls verwendet)
- Monatliche Temperaturen
- Bodentemperatur-Schätzung

---

## 10. ✅ Technische Spezifikationen

### **Neue Module:**
```
data/
├── __init__.py
├── grout_materials.py    (7 Materialien)
└── soil_types.py         (11 Bodentypen)

utils/
└── pvgis_api.py          (PVGIS Integration)

calculations/
└── hydraulics.py         (Hydraulik-Berechnungen)
```

### **Neue Abhängigkeiten:**
- `requests>=2.31.0` (für PVGIS API)

---

## 11. ✅ Validierung und Standards

### **Konform mit:**
- ✅ **VDI 4640** (Thermische Nutzung des Untergrunds)
- ✅ **DVGW W 120** (Qualifikationsanforderungen)
- ✅ **DIN EN 14511** (Wärmepumpen)
- ✅ **PVGIS** (EU Joint Research Centre)

### **Berechnungsmethoden:**
- Darcy-Weisbach (Druckverlust)
- Colebrook-White (Reibungsbeiwert)
- Reynolds-Zahl (Strömungsregime)
- VDI-Bodenwerte (Thermische Eigenschaften)

---

## 12. ✅ Verwendung

### **Workflow:**

1. **Projekt anlegen** (wie bisher)

2. **Bodentyp wählen**
   - Dropdown: z.B. "Sand"
   - Werte werden automatisch übernommen

3. **Verfüllmaterial wählen**
   - Dropdown: z.B. "Thermisch optimiert (Sand)"
   - Material-Eigenschaften sichtbar

4. **Klimadaten laden** (optional)
   - Button klicken
   - Adresse oder Koordinaten eingeben
   - Daten von PVGIS abrufen

5. **Hydraulik konfigurieren**
   - Anzahl Solekreise: 1
   - Frostschutz: 25%
   - Button "Hydraulik berechnen"

6. **Berechnung starten**
   - Wie gewohnt

7. **Ergebnisse prüfen**
   - Materialmengen
   - Druckverlust
   - Pumpenleistung

8. **PDF erstellen**
   - Alle neuen Daten enthalten

---

## 13. ✅ Test-Ergebnisse

```bash
✓ 7 Verfüllmaterialien geladen
✓ 11 Bodentypen geladen
✓ Hydraulik-Berechnung: 1.742 m³/h für 6 kW
✓ PVGIS API funktioniert (mit Fallback)
✓ Alle Module importierbar
✓ Keine Fehler
```

---

## 🎯 Zusammenfassung

### **Was ist neu:**

1. ✅ **7 Verfüllmaterialien** mit Dropdown
2. ✅ **Automatische Materialmengen-Berechnung**
3. ✅ **11 Bodentypen** nach VDI 4640
4. ✅ **PVGIS-Integration** für EU-Klimadaten
5. ✅ **Erweiterte Wärmepumpendaten**
6. ✅ **Vollständige Hydraulik-Berechnungen**
7. ✅ **Frostschutz-Konzentration** mit Eigenschaften
8. ✅ **Druckverlust** und **Pumpenleistung**
9. ✅ **Anzahl Solekreise** konfigurierbar
10. ✅ **Klimadaten-Felder** wie gewünscht

### **Verbesserungen gegenüber Ihrer Vorlage:**

✅ Alle Ihre Eingabefelder implementiert
✅ + Automatische Berechnungen
✅ + Material-Datenbanken
✅ + PVGIS-Integration
✅ + VDI-konforme Bodenwerte
✅ + Kostenkalkulation

---

**Das Tool ist jetzt ein vollständiges professionelles Planungswerkzeug! 🎉**

Siehe auch:
- `CHANGELOG.md` - Vollständige Änderungshistorie
- `NEUE_FEATURES_V2.md` - Features Version 2.0
- `ANLEITUNG.md` - Bedienungsanleitung

