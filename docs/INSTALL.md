# Installationsanleitung

## Voraussetzungen

- Python 3.8 oder höher
- pip (Python Package Manager)

## Installation unter Linux

1. **Repository klonen oder herunterladen**
   ```bash
   cd "/home/jens/Dokumente/Software Projekte/Geothermietool"
   ```

2. **Virtuelle Umgebung erstellen (empfohlen)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

4. **Anwendung starten**
   ```bash
   python main.py
   ```

## Installation unter Windows

1. **Python installieren**
   - Laden Sie Python von https://www.python.org/downloads/ herunter
   - Achten Sie darauf, "Add Python to PATH" zu aktivieren

2. **Kommandozeile öffnen** (cmd oder PowerShell)
   ```cmd
   cd "C:\Pfad\zum\Geothermietool"
   ```

3. **Virtuelle Umgebung erstellen (empfohlen)**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Abhängigkeiten installieren**
   ```cmd
   pip install -r requirements.txt
   ```

5. **Anwendung starten**
   ```cmd
   python main.py
   ```

## Start-Script für Linux erstellen

Sie können ein ausführbares Start-Script erstellen:

```bash
#!/bin/bash
cd "/home/jens/Dokumente/Software Projekte/Geothermietool"
source venv/bin/activate
python main.py
```

Speichern Sie dies als `start.sh` und machen Sie es ausführbar:
```bash
chmod +x start.sh
./start.sh
```

## Fehlerbehebung

### Import-Fehler
Falls Module nicht gefunden werden:
```bash
pip install --upgrade -r requirements.txt
```

### tkinter nicht gefunden (Linux)
Unter Linux müssen Sie möglicherweise tkinter separat installieren:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

### Matplotlib-Fehler
Falls Matplotlib Probleme macht:
```bash
pip install --upgrade matplotlib
```

## Deinstallation

1. Deaktivieren Sie die virtuelle Umgebung:
   ```bash
   deactivate
   ```

2. Löschen Sie den Projektordner

## Support

Bei Problemen überprüfen Sie:
- Python-Version: `python --version` (mindestens 3.8)
- Installierte Pakete: `pip list`
- Fehler-Logs in der Konsole

