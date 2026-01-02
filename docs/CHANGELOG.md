# Changelog - Geothermie Erdsonden-Tool

## Version 2.0 - Professional Edition (02.01.2026)

### 🎉 Neue Hauptfunktionen

#### 1. **Projektdaten und Kundeninformationen**
- ✅ Eingabefelder für Projektname
- ✅ Kundenname und vollständige Adresse
- ✅ Alle Daten werden in PDF-Berichten übernommen

#### 2. **Bohrfeld-Konfiguration**
- ✅ **Mehrere Bohrungen**: Beliebige Anzahl konfigurierbar
- ✅ **Abstände**:
  - Abstand zwischen Bohrungen (Standard: 6 m)
  - Abstand zum Grundstücksrand (Standard: 3 m)
  - Abstand zum Gebäude (Standard: 3 m)
- ✅ **Automatische Berechnung**: Gesamtbohrmeter und Gesamtleistung
- ✅ **Visualisierung**: Bohrfeld-Layout-Diagramm

#### 3. **PE 100 RC Rohrsysteme**
- ✅ PE 100 RC DN32 4-Rohr Dual-Verbinder
- ✅ PE 100 RC DN32 4-Rohr 4-Verbinder
- ✅ PE 100 RC DN32 Single-U
- ✅ PE 100 RC DN32 Double-U
- ✅ Alle mit optimierten Parametern (32mm Ø, 3mm Wandstärke)

#### 4. **Professioneller PDF-Bericht**
- ✅ **Automatische PDF-Generierung** mit einem Klick
- ✅ **Inhalt**:
  - Projektinformationen und Kundendaten
  - Bohrfeld-Konfiguration mit allen Abständen
  - Vollständige Berechnungsergebnisse
  - Eingabeparameter (Boden, Rohr, Lasten)
  - Monatliche Temperaturdiagramme
  - **Detaillierte Bohrloch-Grafik mit 4 Rohren und Beschriftungen**
- ✅ **Design**: Professionelles Layout mit Tabellen und Farben
- ✅ **Export**: Speicherbar als PDF-Datei

#### 5. **Erweiterte Visualisierungen**
- ✅ **Bohrloch-Schema rechts in der Eingabemaske**:
  - Zeigt 4-Rohr-System
  - Live-Vorschau der Konfiguration
  - Beschriftete Durchmesser
- ✅ **Detaillierte Bohrloch-Grafik im PDF**:
  - 4 Rohre mit Nummerierung
  - Vorlauf (rot) und Rücklauf (türkis) gekennzeichnet
  - Maßangaben mit Pfeilen
  - Wärmeentzugsrate angezeigt
  - Temperaturbereich beschriftet
- ✅ **Bohrfeld-Layout**: Zeigt alle Bohrungen mit Abständen

### 🔧 Technische Verbesserungen

- **Neue Abhängigkeit**: reportlab 4.4.7 für PDF-Export
- **Erweitertes GUI-Modul**: `main_window_extended.py`
- **PDF-Generator**: `utils/pdf_export.py` mit vollständiger Funktionalität
- **Keyboard Shortcuts**: Strg+P für schnellen PDF-Export

### 📊 Berechnungen

- ✅ Gesamtbohrmeter werden automatisch berechnet
- ✅ Gesamtleistung des Bohrfelds wird ausgegeben
- ✅ Alle Ergebnisse berücksichtigen Anzahl der Bohrungen

### 🎨 GUI-Verbesserungen

- **Übersichtlichere Struktur** mit Emojis und Farben
- **Zweispaltige Eingabemaske**: Links Parameter, rechts Vorschau
- **Projektdaten-Bereich** ganz oben für einfachen Zugriff
- **Bohrfeld-Konfiguration** prominent platziert
- **PDF-Export-Button** direkt in der Eingabemaske
- **Bessere Statusmeldungen** mit Icons (✓, ❌, ⏳)

### 📁 Dateien

**Neue Dateien:**
- `gui/main_window_extended.py` - Erweiterte GUI (1400+ Zeilen)
- `utils/__init__.py` - Utils-Paket
- `utils/pdf_export.py` - PDF-Generator (500+ Zeilen)
- `CHANGELOG.md` - Diese Datei

**Aktualisierte Dateien:**
- `pipe.txt` - 4 neue PE 100 RC Rohre hinzugefügt (jetzt 65 Rohre)
- `requirements.txt` - reportlab hinzugefügt
- `main.py` - Verwendet jetzt erweiterte GUI

### 📖 Dokumentation

Siehe:
- `ANLEITUNG.md` - Vollständige Bedienungsanleitung
- `ZUSAMMENFASSUNG.md` - Projekt-Übersicht
- `INSTALL.md` - Installationsanleitung

---

## Version 1.0 - Initial Release (02.01.2026)

### Basis-Funktionen

- ✅ Parser für pipe.txt (61 Rohrtypen)
- ✅ Parser für EED .dat Dateien
- ✅ Erdwärmesonden-Berechnung (Single-U, Double-U, Coaxial)
- ✅ G-Funktionen nach Eskilson
- ✅ Thermische Widerstände (Multipol-Methode)
- ✅ GUI mit tkinter
- ✅ Monatliche Temperaturanalyse
- ✅ Visualisierung mit Matplotlib
- ✅ Text-Export

---

## Geplante Features (Version 3.0)

### In Planung

- [ ] Geschichtete Böden (mehrere Schichten)
- [ ] Grundwasserströmung berücksichtigen
- [ ] Kostenrechnung mit Material- und Arbeitskosten
- [ ] Excel-Export
- [ ] 3D-Visualisierung des Bohrfelds
- [ ] Optimierungsalgorithmen für Bohrfeld-Anordnung
- [ ] Mehrsprachigkeit (Englisch)
- [ ] Web-basierte Version

---

## Bekannte Einschränkungen

- Maximale Bohrtiefe: 300 m
- Bohrfeld-Berechnungen verwenden vereinfachte Überlagerung
- Keine detaillierte thermische Wechselwirkung zwischen Bohrungen
- Homogener Untergrund angenommen

---

**Für Fragen und Support siehe README.md oder ANLEITUNG.md**

