"""Hauptfenster der GUI für das Geothermietool."""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from typing import Optional
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

from parsers import PipeParser, EEDParser
from calculations import BoreholeCalculator


class GeothermieGUI:
    """Hauptfenster der Geothermie-Erdsonden-Anwendung."""
    
    def __init__(self, root):
        """Initialisiert die GUI."""
        self.root = root
        self.root.title("Geothermie Erdsonden-Berechnungstool")
        self.root.geometry("1400x900")
        
        # Parser und Rechner
        self.pipe_parser = PipeParser()
        self.eed_parser = EEDParser()
        self.calculator = BoreholeCalculator()
        
        # Daten
        self.pipes = []
        self.current_config = None
        self.result = None
        
        # GUI aufbauen
        self._create_menu()
        self._create_main_layout()
        self._create_status_bar()
        
        # Lade Standard-Rohrtypen
        self._load_default_pipes()
    
    def _create_menu(self):
        """Erstellt die Menüleiste."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Datei-Menü
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Datei", menu=file_menu)
        file_menu.add_command(label="Pipe.txt laden", command=self._load_pipe_file)
        file_menu.add_command(label="EED .dat laden", command=self._load_eed_file)
        file_menu.add_separator()
        file_menu.add_command(label="Ergebnis exportieren", command=self._export_results)
        file_menu.add_separator()
        file_menu.add_command(label="Beenden", command=self.root.quit)
        
        # Hilfe-Menü
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Hilfe", menu=help_menu)
        help_menu.add_command(label="Über", command=self._show_about)
    
    def _create_main_layout(self):
        """Erstellt das Hauptlayout."""
        # Hauptcontainer mit Notebook (Tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Tab 1: Eingabe
        self.input_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.input_frame, text="Eingabe")
        self._create_input_tab()
        
        # Tab 2: Ergebnisse
        self.results_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.results_frame, text="Ergebnisse")
        self._create_results_tab()
        
        # Tab 3: Visualisierung
        self.viz_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.viz_frame, text="Diagramme")
        self._create_visualization_tab()
    
    def _create_input_tab(self):
        """Erstellt den Eingabe-Tab."""
        # Scrollbarer Container
        canvas = tk.Canvas(self.input_frame)
        scrollbar = ttk.Scrollbar(self.input_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Eingabefelder
        row = 0
        
        # === Bodeneigenschaften ===
        ttk.Label(scrollable_frame, text="Bodeneigenschaften", font=("Arial", 12, "bold")).grid(
            row=row, column=0, columnspan=2, sticky="w", padx=10, pady=(10, 5)
        )
        row += 1
        
        self.entries = {}
        
        self._add_input_field(scrollable_frame, row, "Wärmeleitfähigkeit Boden [W/m·K]:", "ground_thermal_cond", "3.4")
        row += 1
        self._add_input_field(scrollable_frame, row, "Wärmekapazität Boden [J/m³·K]:", "ground_heat_cap", "2400000")
        row += 1
        self._add_input_field(scrollable_frame, row, "Ungestörte Bodentemperatur [°C]:", "ground_temp", "10.0")
        row += 1
        self._add_input_field(scrollable_frame, row, "Geothermischer Gradient [K/m]:", "geothermal_gradient", "0.03")
        row += 1
        
        # === Bohrloch-Konfiguration ===
        ttk.Label(scrollable_frame, text="Bohrloch-Konfiguration", font=("Arial", 12, "bold")).grid(
            row=row, column=0, columnspan=2, sticky="w", padx=10, pady=(15, 5)
        )
        row += 1
        
        self._add_input_field(scrollable_frame, row, "Bohrloch-Durchmesser [m]:", "borehole_diameter", "0.152")
        row += 1
        
        ttk.Label(scrollable_frame, text="Rohrkonfiguration:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.pipe_config_var = tk.StringVar(value="single-u")
        pipe_config_combo = ttk.Combobox(
            scrollable_frame, 
            textvariable=self.pipe_config_var,
            values=["single-u", "double-u", "coaxial"],
            state="readonly",
            width=30
        )
        pipe_config_combo.grid(row=row, column=1, sticky="w", padx=10, pady=5)
        row += 1
        
        # === Rohr-Eigenschaften ===
        ttk.Label(scrollable_frame, text="Rohr-Eigenschaften", font=("Arial", 12, "bold")).grid(
            row=row, column=0, columnspan=2, sticky="w", padx=10, pady=(15, 5)
        )
        row += 1
        
        ttk.Label(scrollable_frame, text="Rohrtyp:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.pipe_type_var = tk.StringVar()
        self.pipe_type_combo = ttk.Combobox(
            scrollable_frame, 
            textvariable=self.pipe_type_var,
            state="readonly",
            width=30
        )
        self.pipe_type_combo.grid(row=row, column=1, sticky="w", padx=10, pady=5)
        self.pipe_type_combo.bind("<<ComboboxSelected>>", self._on_pipe_selected)
        row += 1
        
        self._add_input_field(scrollable_frame, row, "Rohr Außendurchmesser [m]:", "pipe_outer_diameter", "0.040")
        row += 1
        self._add_input_field(scrollable_frame, row, "Rohr Wandstärke [m]:", "pipe_thickness", "0.0037")
        row += 1
        self._add_input_field(scrollable_frame, row, "Rohr Wärmeleitfähigkeit [W/m·K]:", "pipe_thermal_cond", "0.42")
        row += 1
        self._add_input_field(scrollable_frame, row, "Schenkelabstand [m]:", "shank_spacing", "0.052")
        row += 1
        
        # === Verfüllung ===
        ttk.Label(scrollable_frame, text="Verfüllung", font=("Arial", 12, "bold")).grid(
            row=row, column=0, columnspan=2, sticky="w", padx=10, pady=(15, 5)
        )
        row += 1
        
        self._add_input_field(scrollable_frame, row, "Wärmeleitfähigkeit Verfüllung [W/m·K]:", "grout_thermal_cond", "1.3")
        row += 1
        
        # === Wärmeträgerflüssigkeit ===
        ttk.Label(scrollable_frame, text="Wärmeträgerflüssigkeit", font=("Arial", 12, "bold")).grid(
            row=row, column=0, columnspan=2, sticky="w", padx=10, pady=(15, 5)
        )
        row += 1
        
        self._add_input_field(scrollable_frame, row, "Volumenstrom [m³/s]:", "fluid_flow_rate", "0.0005")
        row += 1
        self._add_input_field(scrollable_frame, row, "Wärmeleitfähigkeit [W/m·K]:", "fluid_thermal_cond", "0.48")
        row += 1
        self._add_input_field(scrollable_frame, row, "Wärmekapazität [J/kg·K]:", "fluid_heat_cap", "3800")
        row += 1
        self._add_input_field(scrollable_frame, row, "Dichte [kg/m³]:", "fluid_density", "1030")
        row += 1
        self._add_input_field(scrollable_frame, row, "Viskosität [Pa·s]:", "fluid_viscosity", "0.004")
        row += 1
        
        # === Lasten ===
        ttk.Label(scrollable_frame, text="Heiz- und Kühllast", font=("Arial", 12, "bold")).grid(
            row=row, column=0, columnspan=2, sticky="w", padx=10, pady=(15, 5)
        )
        row += 1
        
        self._add_input_field(scrollable_frame, row, "Jahres-Heizenergie [MWh]:", "annual_heating", "12.0")
        row += 1
        self._add_input_field(scrollable_frame, row, "Jahres-Kühlenergie [MWh]:", "annual_cooling", "0.0")
        row += 1
        self._add_input_field(scrollable_frame, row, "Heiz-Spitzenlast [kW]:", "peak_heating", "6.0")
        row += 1
        self._add_input_field(scrollable_frame, row, "Kühl-Spitzenlast [kW]:", "peak_cooling", "0.0")
        row += 1
        self._add_input_field(scrollable_frame, row, "Wärmepumpen-COP:", "heat_pump_cop", "4.0")
        row += 1
        
        # === Temperaturanforderungen ===
        ttk.Label(scrollable_frame, text="Temperaturanforderungen", font=("Arial", 12, "bold")).grid(
            row=row, column=0, columnspan=2, sticky="w", padx=10, pady=(15, 5)
        )
        row += 1
        
        self._add_input_field(scrollable_frame, row, "Min. Fluidtemperatur [°C]:", "min_fluid_temp", "-2.0")
        row += 1
        self._add_input_field(scrollable_frame, row, "Max. Fluidtemperatur [°C]:", "max_fluid_temp", "15.0")
        row += 1
        
        # === Simulation ===
        ttk.Label(scrollable_frame, text="Simulation", font=("Arial", 12, "bold")).grid(
            row=row, column=0, columnspan=2, sticky="w", padx=10, pady=(15, 5)
        )
        row += 1
        
        self._add_input_field(scrollable_frame, row, "Simulationsdauer [Jahre]:", "simulation_years", "25")
        row += 1
        self._add_input_field(scrollable_frame, row, "Startwert Bohrtiefe [m]:", "initial_depth", "100")
        row += 1
        
        # Berechnen-Button
        calc_button = ttk.Button(
            scrollable_frame, 
            text="Berechnung starten",
            command=self._run_calculation,
            style="Accent.TButton"
        )
        calc_button.grid(row=row, column=0, columnspan=2, pady=20, padx=10)
    
    def _add_input_field(self, parent, row, label, key, default_value):
        """Fügt ein Eingabefeld hinzu."""
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w", padx=10, pady=5)
        entry = ttk.Entry(parent, width=32)
        entry.insert(0, default_value)
        entry.grid(row=row, column=1, sticky="w", padx=10, pady=5)
        self.entries[key] = entry
    
    def _create_results_tab(self):
        """Erstellt den Ergebnisse-Tab."""
        # Scrollbarer Text-Widget
        text_frame = ttk.Frame(self.results_frame)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.results_text = tk.Text(
            text_frame, 
            wrap=tk.WORD,
            font=("Courier", 10),
            yscrollcommand=scrollbar.set
        )
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.results_text.yview)
        
        # Initial-Text
        self.results_text.insert("1.0", "Keine Berechnung durchgeführt.\n\nBitte Parameter eingeben und Berechnung starten.")
        self.results_text.config(state=tk.DISABLED)
    
    def _create_visualization_tab(self):
        """Erstellt den Visualisierungs-Tab."""
        # Matplotlib Figure
        self.fig = Figure(figsize=(12, 8))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.viz_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def _create_status_bar(self):
        """Erstellt die Statusleiste."""
        self.status_var = tk.StringVar(value="Bereit")
        status_bar = ttk.Label(
            self.root, 
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def _load_default_pipes(self):
        """Lädt Standard-Rohrtypen."""
        default_pipe_file = os.path.join(os.path.dirname(__file__), "..", "pipe.txt")
        if os.path.exists(default_pipe_file):
            try:
                self.pipes = self.pipe_parser.parse_file(default_pipe_file)
                self._update_pipe_combo()
                self.status_var.set(f"{len(self.pipes)} Rohrtypen geladen")
            except Exception as e:
                print(f"Fehler beim Laden der Standard-Rohre: {e}")
    
    def _load_pipe_file(self):
        """Lädt eine pipe.txt Datei."""
        filename = filedialog.askopenfilename(
            title="Pipe.txt öffnen",
            filetypes=[("Text-Dateien", "*.txt"), ("Alle Dateien", "*.*")]
        )
        if filename:
            try:
                self.pipes = self.pipe_parser.parse_file(filename)
                self._update_pipe_combo()
                self.status_var.set(f"{len(self.pipes)} Rohrtypen aus {os.path.basename(filename)} geladen")
                messagebox.showinfo("Erfolg", f"{len(self.pipes)} Rohrtypen wurden geladen.")
            except Exception as e:
                messagebox.showerror("Fehler", f"Fehler beim Laden: {str(e)}")
    
    def _load_eed_file(self):
        """Lädt eine EED .dat Datei."""
        filename = filedialog.askopenfilename(
            title="EED .dat öffnen",
            filetypes=[("DAT-Dateien", "*.dat"), ("Alle Dateien", "*.*")]
        )
        if filename:
            try:
                config = self.eed_parser.parse_file(filename)
                self._populate_from_eed_config(config)
                self.status_var.set(f"EED-Konfiguration aus {os.path.basename(filename)} geladen")
                messagebox.showinfo("Erfolg", "EED-Konfiguration wurde geladen.")
            except Exception as e:
                messagebox.showerror("Fehler", f"Fehler beim Laden: {str(e)}")
    
    def _populate_from_eed_config(self, config):
        """Füllt Eingabefelder mit EED-Konfiguration."""
        # Bodeneigenschaften
        self.entries["ground_thermal_cond"].delete(0, tk.END)
        self.entries["ground_thermal_cond"].insert(0, str(config.thermal_conductivity_ground))
        
        self.entries["ground_heat_cap"].delete(0, tk.END)
        self.entries["ground_heat_cap"].insert(0, str(config.heat_capacity))
        
        self.entries["ground_temp"].delete(0, tk.END)
        self.entries["ground_temp"].insert(0, str(config.init_ground_surface_temp))
        
        # Bohrloch
        self.entries["borehole_diameter"].delete(0, tk.END)
        self.entries["borehole_diameter"].insert(0, str(config.borehole_diameter))
        
        # Rohr
        if config.u_pipe_diameter > 0:
            self.entries["pipe_outer_diameter"].delete(0, tk.END)
            self.entries["pipe_outer_diameter"].insert(0, str(config.u_pipe_diameter))
            
            self.entries["pipe_thickness"].delete(0, tk.END)
            self.entries["pipe_thickness"].insert(0, str(config.u_pipe_thickness))
            
            self.entries["pipe_thermal_cond"].delete(0, tk.END)
            self.entries["pipe_thermal_cond"].insert(0, str(config.u_pipe_thermal_conductivity))
            
            self.entries["shank_spacing"].delete(0, tk.END)
            self.entries["shank_spacing"].insert(0, str(config.u_pipe_shank_space))
        
        # Verfüllung
        self.entries["grout_thermal_cond"].delete(0, tk.END)
        self.entries["grout_thermal_cond"].insert(0, str(config.thermal_conductivity_fill))
        
        # Fluid
        if config.hc_thermal_conductivity > 0:
            self.entries["fluid_thermal_cond"].delete(0, tk.END)
            self.entries["fluid_thermal_cond"].insert(0, str(config.hc_thermal_conductivity))
            
            self.entries["fluid_heat_cap"].delete(0, tk.END)
            self.entries["fluid_heat_cap"].insert(0, str(config.hc_heat_capacity))
            
            self.entries["fluid_density"].delete(0, tk.END)
            self.entries["fluid_density"].insert(0, str(config.hc_density))
            
            self.entries["fluid_viscosity"].delete(0, tk.END)
            self.entries["fluid_viscosity"].insert(0, str(abs(config.hc_viscosity)))
        
        # Lasten
        self.entries["annual_heating"].delete(0, tk.END)
        self.entries["annual_heating"].insert(0, str(config.annual_heat_load))
        
        self.entries["annual_cooling"].delete(0, tk.END)
        self.entries["annual_cooling"].insert(0, str(config.annual_cool_load))
        
        self.entries["heat_pump_cop"].delete(0, tk.END)
        self.entries["heat_pump_cop"].insert(0, str(config.spf_heat))
        
        # Temperaturanforderungen
        self.entries["min_fluid_temp"].delete(0, tk.END)
        self.entries["min_fluid_temp"].insert(0, str(config.tfluid_min_required))
        
        self.entries["max_fluid_temp"].delete(0, tk.END)
        self.entries["max_fluid_temp"].insert(0, str(config.tfluid_max_required))
    
    def _update_pipe_combo(self):
        """Aktualisiert die Rohrtyp-Combobox."""
        if self.pipes:
            pipe_names = [pipe.name for pipe in self.pipes]
            self.pipe_type_combo['values'] = pipe_names
            self.pipe_type_combo.current(0)
            self._on_pipe_selected(None)
    
    def _on_pipe_selected(self, event):
        """Callback wenn ein Rohrtyp ausgewählt wird."""
        if not self.pipes:
            return
        
        selected_name = self.pipe_type_var.get()
        for pipe in self.pipes:
            if pipe.name == selected_name:
                # Aktualisiere Eingabefelder
                self.entries["pipe_outer_diameter"].delete(0, tk.END)
                self.entries["pipe_outer_diameter"].insert(0, f"{pipe.diameter_m:.4f}")
                
                self.entries["pipe_thickness"].delete(0, tk.END)
                self.entries["pipe_thickness"].insert(0, f"{pipe.thickness_m:.4f}")
                
                self.entries["pipe_thermal_cond"].delete(0, tk.END)
                self.entries["pipe_thermal_cond"].insert(0, str(pipe.thermal_conductivity))
                break
    
    def _run_calculation(self):
        """Führt die Berechnung durch."""
        try:
            # Sammle Eingabewerte
            params = {}
            for key, entry in self.entries.items():
                params[key] = float(entry.get())
            
            # Status aktualisieren
            self.status_var.set("Berechnung läuft...")
            self.root.update()
            
            # Berechnung durchführen
            self.result = self.calculator.calculate_required_depth(
                ground_thermal_conductivity=params["ground_thermal_cond"],
                ground_heat_capacity=params["ground_heat_cap"],
                undisturbed_ground_temp=params["ground_temp"],
                geothermal_gradient=params["geothermal_gradient"],
                borehole_diameter=params["borehole_diameter"],
                pipe_configuration=self.pipe_config_var.get(),
                pipe_outer_diameter=params["pipe_outer_diameter"],
                pipe_wall_thickness=params["pipe_thickness"],
                pipe_thermal_conductivity=params["pipe_thermal_cond"],
                shank_spacing=params["shank_spacing"],
                grout_thermal_conductivity=params["grout_thermal_cond"],
                fluid_thermal_conductivity=params["fluid_thermal_cond"],
                fluid_heat_capacity=params["fluid_heat_cap"],
                fluid_density=params["fluid_density"],
                fluid_viscosity=params["fluid_viscosity"],
                fluid_flow_rate=params["fluid_flow_rate"],
                annual_heating_demand=params["annual_heating"],
                annual_cooling_demand=params["annual_cooling"],
                peak_heating_load=params["peak_heating"],
                peak_cooling_load=params["peak_cooling"],
                heat_pump_cop=params["heat_pump_cop"],
                min_fluid_temperature=params["min_fluid_temp"],
                max_fluid_temperature=params["max_fluid_temp"],
                simulation_years=int(params["simulation_years"]),
                initial_depth=params["initial_depth"]
            )
            
            # Ergebnisse anzeigen
            self._display_results()
            self._plot_results()
            
            # Status aktualisieren
            self.status_var.set("Berechnung erfolgreich abgeschlossen")
            
            # Wechsle zum Ergebnisse-Tab
            self.notebook.select(self.results_frame)
            
        except ValueError as e:
            messagebox.showerror("Eingabefehler", f"Ungültige Eingabe: {str(e)}")
            self.status_var.set("Berechnung fehlgeschlagen")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler bei der Berechnung: {str(e)}")
            self.status_var.set("Berechnung fehlgeschlagen")
    
    def _display_results(self):
        """Zeigt die Ergebnisse im Text-Widget an."""
        if not self.result:
            return
        
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete("1.0", tk.END)
        
        text = "=" * 60 + "\n"
        text += "ERDWÄRMESONDEN-BERECHNUNGSERGEBNIS\n"
        text += "=" * 60 + "\n\n"
        
        text += f"Erforderliche Bohrtiefe:     {self.result.required_depth:>10.1f} m\n"
        text += f"Wärmeentzugsrate:            {self.result.heat_extraction_rate:>10.2f} W/m\n\n"
        
        text += "TEMPERATUREN\n"
        text += "-" * 60 + "\n"
        text += f"Min. Fluidtemperatur:        {self.result.fluid_temperature_min:>10.2f} °C\n"
        text += f"Max. Fluidtemperatur:        {self.result.fluid_temperature_max:>10.2f} °C\n\n"
        
        text += "THERMISCHE WIDERSTÄNDE\n"
        text += "-" * 60 + "\n"
        text += f"Bohrloch-Widerstand (R_b):   {self.result.borehole_resistance:>10.4f} m·K/W\n"
        text += f"Effektiver Widerstand:       {self.result.effective_resistance:>10.4f} m·K/W\n\n"
        
        text += "MONATLICHE DURCHSCHNITTSTEMPERATUREN\n"
        text += "-" * 60 + "\n"
        months = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", 
                  "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]
        for i, (month, temp) in enumerate(zip(months, self.result.monthly_temperatures)):
            text += f"{month}: {temp:>6.2f} °C    "
            if (i + 1) % 3 == 0:
                text += "\n"
        
        text += "\n\n"
        text += "=" * 60 + "\n"
        
        self.results_text.insert("1.0", text)
        self.results_text.config(state=tk.DISABLED)
    
    def _plot_results(self):
        """Erstellt Visualisierungen der Ergebnisse."""
        if not self.result:
            return
        
        self.fig.clear()
        
        # 2 Subplots
        ax1 = self.fig.add_subplot(1, 2, 1)
        ax2 = self.fig.add_subplot(1, 2, 2)
        
        # Plot 1: Monatliche Temperaturen
        months = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]
        x = np.arange(len(months))
        
        ax1.plot(x, self.result.monthly_temperatures, 'o-', linewidth=2, markersize=8)
        ax1.axhline(y=self.result.fluid_temperature_min, color='b', linestyle='--', 
                    label=f'Min: {self.result.fluid_temperature_min:.1f}°C')
        ax1.axhline(y=self.result.fluid_temperature_max, color='r', linestyle='--',
                    label=f'Max: {self.result.fluid_temperature_max:.1f}°C')
        ax1.set_xlabel('Monat', fontsize=12)
        ax1.set_ylabel('Temperatur [°C]', fontsize=12)
        ax1.set_title('Monatliche Fluidtemperaturen', fontsize=14, fontweight='bold')
        ax1.set_xticks(x)
        ax1.set_xticklabels(months)
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # Plot 2: Bohrloch-Visualisierung
        depth = self.result.required_depth
        y_profile = np.linspace(0, depth, 100)
        temp_profile = [self.entries["ground_temp"].get()] * 100  # Vereinfacht
        
        # Zeichne Bohrloch schematisch
        ax2.barh(y=depth/2, width=float(self.entries["borehole_diameter"].get()), 
                 height=depth, color='lightgray', edgecolor='black', linewidth=2)
        ax2.text(0, -depth*0.1, f'Tiefe: {depth:.1f} m', 
                 ha='center', fontsize=14, fontweight='bold')
        ax2.text(0, depth*1.05, 'Bohrloch-Schema', 
                 ha='center', fontsize=14, fontweight='bold')
        ax2.set_ylim(-depth*0.15, depth*1.1)
        ax2.set_xlim(-0.3, 0.3)
        ax2.set_ylabel('Tiefe [m]', fontsize=12)
        ax2.invert_yaxis()
        ax2.set_xlabel('Durchmesser [m]', fontsize=12)
        ax2.grid(True, alpha=0.3, axis='y')
        
        self.fig.tight_layout()
        self.canvas.draw()
    
    def _export_results(self):
        """Exportiert die Ergebnisse in eine Textdatei."""
        if not self.result:
            messagebox.showwarning("Keine Daten", "Keine Berechnungsergebnisse zum Exportieren vorhanden.")
            return
        
        filename = filedialog.asksaveasfilename(
            title="Ergebnisse speichern",
            defaultextension=".txt",
            filetypes=[("Text-Dateien", "*.txt"), ("Alle Dateien", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.results_text.get("1.0", tk.END))
                messagebox.showinfo("Erfolg", f"Ergebnisse wurden in {os.path.basename(filename)} gespeichert.")
            except Exception as e:
                messagebox.showerror("Fehler", f"Fehler beim Speichern: {str(e)}")
    
    def _show_about(self):
        """Zeigt den Über-Dialog."""
        about_text = """Geothermie Erdsonden-Berechnungstool
        
Version: 1.0
        
Ein Open-Source-Tool zur Dimensionierung von
Erdwärmesonden bis 100m Tiefe.

Inspiriert von Earth Energy Designer (EED)

Entwickelt mit Python und tkinter
        
© 2026 - Open Source (MIT Lizenz)
        """
        messagebox.showinfo("Über", about_text)


def main():
    """Haupteinstiegspunkt."""
    root = tk.Tk()
    app = GeothermieGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

