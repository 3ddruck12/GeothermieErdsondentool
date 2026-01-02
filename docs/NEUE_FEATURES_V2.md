# 🎉 Neue Features in Version 2.0 - Professional Edition

## ✅ Alle gewünschten Funktionen implementiert!

### 1. ✅ PE 100 RC 32mm Rohre

**4 neue Rohrtypen hinzugefügt:**

- **PE 100 RC DN32 4-Rohr Dual-Verbinder** (empfohlen)
- **PE 100 RC DN32 4-Rohr 4-Verbinder**
- PE 100 RC DN32 Single-U
- PE 100 RC DN32 Double-U

**Spezifikationen:**
- Außendurchmesser: 32 mm
- Wandstärke: 3 mm
- Wärmeleitfähigkeit: 0.42 W/m·K
- Alle in pipe.txt verfügbar

---

### 2. ✅ PDF-Bericht mit einem Klick

**Button: "📄 PDF-Bericht erstellen"**

Der PDF-Bericht enthält:

#### Seite 1: Projektübersicht
- ✅ **Projektinformationen**
  - Projektname
  - Kundenname
  - Vollständige Adresse (Straße, PLZ, Ort)
  - Erstellungsdatum

- ✅ **Bohrfeld-Konfiguration**
  - Anzahl Bohrungen
  - Tiefe pro Bohrung
  - Gesamtbohrmeter
  - **Abstand zwischen Bohrungen**
  - **Abstand zum Grundstücksrand**
  - **Abstand zum Gebäude**
  - Bohrloch-Durchmesser
  - Rohrkonfiguration

- ✅ **Berechnungsergebnisse**
  - Erforderliche Bohrtiefe
  - Gesamte Bohrmeter
  - Wärmeentzugsrate
  - Gesamtleistung Bohrfeld
  - Min/Max Fluidtemperaturen
  - Thermische Widerstände

#### Seite 2: Technische Details
- ✅ **Bodeneigenschaften** (Tabelle)
- ✅ **Rohr-Eigenschaften** (Tabelle)
- ✅ **Heiz- und Kühllast** (Tabelle)

#### Seite 3: Visualisierungen
- ✅ **Monatliche Temperaturen** (Diagramm)
- ✅ **Detaillierte Bohrloch-Grafik** (siehe unten)

**Export-Funktion:**
- Keyboard Shortcut: **Strg+P**
- Dateiname wird automatisch vorgeschlagen
- Professionelles Layout mit Farben und Tabellen

---

### 3. ✅ Projektdaten in der Maske

**Neuer Bereich ganz oben: "🏢 Projektinformationen"**

Eingabefelder:
- ✅ **Projektname**
- ✅ **Kundenname**
- ✅ **Straße + Nr.**
- ✅ **PLZ**
- ✅ **Ort**

Alle Daten werden:
- Im Hauptfenster angezeigt
- In Berechnungsergebnissen ausgegeben
- Im PDF-Bericht übernommen

---

### 4. ✅ Bohrfeld mit mehreren Bohrungen

**Neuer Bereich: "🎯 Bohrfeld-Konfiguration"**

Konfigurierbare Parameter:
- ✅ **Anzahl Bohrungen** (1, 2, 3, 4, ...)
- ✅ **Abstand zwischen Bohrungen** [m] (Standard: 6 m)
- ✅ **Abstand zum Grundstücksrand** [m] (Standard: 3 m)
- ✅ **Abstand zum Gebäude** [m] (Standard: 3 m)

**Automatische Berechnungen:**
- Gesamtbohrmeter = Tiefe × Anzahl Bohrungen
- Gesamtleistung Bohrfeld = Leistung pro Meter × Gesamtbohrmeter

**Visualisierung:**
- Bohrfeld-Layout-Diagramm zeigt alle Bohrungen
- Abstände werden eingezeichnet
- Nummerierung der Bohrungen (1, 2, 3, ...)

---

### 5. ✅ Detaillierte Bohrloch-Grafik mit 4 Leitungen

**Rechts in der Eingabemaske:**
- Live-Vorschau des Bohrloch-Querschnitts
- Zeigt 4-Rohr-System
- Aktualisiert sich bei Änderungen

**Im PDF-Bericht (große Grafik):**

```
┌─────────────────────────────────────┐
│   ERDWÄRMESONDEN-SCHEMA (4-ROHR)    │
│                                     │
│         ╔════════════╗              │
│         ║            ║  ← Ø 152 mm │
│         ║  ①    ②   ║              │
│         ║    ▓▓▓     ║              │
│         ║  ③    ④   ║              │
│         ╚════════════╝              │
│                                     │
│  Legende:                           │
│  ① = Vorlauf 1  (rot)               │
│  ② = Rücklauf 1 (türkis)            │
│  ③ = Vorlauf 2  (rot)               │
│  ④ = Rücklauf 2 (türkis)            │
│                                     │
│  Beschriftungen:                    │
│  → Bohrtiefe: 100.0 m               │
│  → Wärmeentzug: 52.3 W/m            │
│  → Fluid-Temp: -2.0°C bis 15.0°C    │
│  → Rohr Ø 32 mm                     │
└─────────────────────────────────────┘
```

**Grafik-Details:**
- ✅ 4 Rohre farblich unterschieden (Vorlauf rot, Rücklauf türkis)
- ✅ Nummerierung 1-4 auf jedem Rohr
- ✅ Bohrloch-Durchmesser mit Maßpfeilen
- ✅ **Wärmeentzugsrate beschriftet**
- ✅ **Fluidtemperaturen angezeigt**
- ✅ **Bohrtiefe prominent dargestellt**
- ✅ Rohrdurchmesser beschriftet
- ✅ Professionelles Layout mit Farben

---

## 🎨 GUI-Verbesserungen

### Übersichtlichere Struktur
- Emojis für bessere Orientierung (🏢, 🎯, 🌍, ⚙️, etc.)
- Farbcodierung wichtiger Bereiche
- Zweispaltiges Layout (Eingabe links, Vorschau rechts)

### Neue Buttons
- **🚀 Berechnung starten** (grün hervorgehoben)
- **📄 PDF-Bericht erstellen** (direkt neben Berechnen)

### Statusleiste
- Zeigt detaillierte Informationen
- Icons für Status (✓ Erfolg, ❌ Fehler, ⏳ Lädt)
- Zusammenfassung nach Berechnung

---

## 📊 Erweiterte Visualisierungen

### Tab "📈 Diagramme"

**3 Diagramme nebeneinander:**

1. **Monatliche Temperaturen**
   - Jahresverlauf
   - Min/Max-Linien

2. **Bohrloch-Querschnitt**
   - 4 Rohre nummeriert
   - Farbcodierung
   - Durchmesser-Angabe

3. **Bohrfeld-Layout** (NEU!)
   - Alle Bohrungen im Grundriss
   - Abstände eingezeichnet
   - Nummerierung

---

## 📁 Neue Dateien

```
Geothermietool/
├── utils/
│   ├── __init__.py              ← NEU
│   └── pdf_export.py            ← NEU (500+ Zeilen)
├── gui/
│   └── main_window_extended.py  ← NEU (1400+ Zeilen)
├── pipe.txt                     ← ERWEITERT (+4 PE 100 Rohre)
├── CHANGELOG.md                 ← NEU
└── NEUE_FEATURES_V2.md         ← Diese Datei
```

---

## 🚀 Installation und Update

### Neue Abhängigkeit
```bash
cd "/home/jens/Dokumente/Software Projekte/Geothermietool"
source venv/bin/activate
pip install reportlab
```

### Start
```bash
./start.sh
```
oder
```bash
python main.py
```

---

## ✅ Checkliste - Alle Anforderungen erfüllt

- [x] PE 100 RC 32mm Rohre mit Dual-Verbinder
- [x] PE 100 RC 32mm Rohre mit 4-Verbinder
- [x] PDF-Bericht mit Button
- [x] Projektdaten (Name, Kunde, Adresse) in Maske
- [x] Mehrere Bohrungen konfigurierbar
- [x] Abstand zwischen Bohrungen (6m)
- [x] Abstand zum Grundstücksrand (3m)
- [x] Abstand zum Gebäude (3m)
- [x] Rechts Grafik mit Bohrung und 4 Leitungen
- [x] Werte in Grafik erklärt (beschriftet)

---

## 🎯 Beispiel-Workflow

1. **Projekt anlegen**
   - Projektname: "Einfamilienhaus Müller"
   - Kunde: "Familie Müller"
   - Adresse eingeben

2. **Bohrfeld konfigurieren**
   - 2 Bohrungen
   - 6m Abstand zwischen Bohrungen
   - 3m zum Grundstück, 3m zum Haus

3. **Rohr auswählen**
   - "PE 100 RC DN32 4-Rohr Dual-Verbinder" aus Liste wählen

4. **Parameter einstellen**
   - Bodenwerte, Lasten, etc. eingeben
   - oder EED-Datei laden

5. **Berechnen**
   - Button "🚀 Berechnung starten" klicken
   - Ergebnisse werden angezeigt

6. **PDF erstellen**
   - Button "📄 PDF-Bericht erstellen" klicken
   - oder Strg+P drücken
   - Datei speichern

7. **Fertig!**
   - Professioneller Bericht zum Ausdrucken oder Versenden

---

## 📞 Support

Bei Fragen siehe:
- `ANLEITUNG.md` - Bedienungsanleitung
- `CHANGELOG.md` - Alle Änderungen
- `README.md` - Übersicht

---

**Viel Erfolg mit der Professional Edition! 🎉**

