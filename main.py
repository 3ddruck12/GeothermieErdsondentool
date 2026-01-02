#!/usr/bin/env python3
"""
Geothermie Erdsonden-Berechnungstool

Haupteinstiegspunkt für die Anwendung.
"""

import tkinter as tk
import sys
import os

# Füge den aktuellen Ordner zum Python-Pfad hinzu
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importiere die GUI
try:
    # Versuche zuerst die erweiterte V2 GUI (funktioniert garantiert)
    from gui.main_window_extended import GeothermieGUIExtended as GUI
    print("✓ Starte Extended GUI V2")
except ImportError as e:
    print(f"Fehler beim Import der Extended GUI: {e}")
    # Fallback auf Original
    from gui.main_window import GeothermieGUI as GUI
    print("✓ Starte Original GUI V1")


def main():
    """Hauptfunktion - startet die GUI."""
    try:
        # Erstelle Hauptfenster
        root = tk.Tk()
        
        # Erstelle GUI
        app = GUI(root)
        
        print("✓ GUI erstellt, starte Event-Loop...")
        
        # Starte Event-Loop
        root.mainloop()
        
    except Exception as e:
        print(f"❌ Fehler beim Starten: {e}")
        import traceback
        traceback.print_exc()
        
        # Zeige Fehler in Dialog
        import tkinter.messagebox as mb
        mb.showerror("Fehler", f"Fehler beim Starten:\n{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

