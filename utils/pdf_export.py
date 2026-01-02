"""PDF-Bericht-Generator für Erdwärmesonden-Berechnungen."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas
from datetime import datetime
import os
import tempfile
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch
import matplotlib.patches as mpatches
from typing import Optional


class PDFReportGenerator:
    """Generiert professionelle PDF-Berichte für Erdwärmesonden-Berechnungen."""
    
    def __init__(self):
        """Initialisiert den PDF-Generator."""
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Erstellt benutzerdefinierte Styles."""
        # Titel-Style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1f4788'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Untertitel
        self.styles.add(ParagraphStyle(
            name='CustomHeading',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#1f4788'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        ))
        
        # Normal mit Einzug
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceAfter=6
        ))
    
    def generate_report(
        self,
        filepath: str,
        result,
        params: dict,
        project_info: dict,
        borehole_config: dict
    ):
        """
        Generiert einen kompletten PDF-Bericht.
        
        Args:
            filepath: Pfad für die PDF-Datei
            result: Berechnungsergebnis (BoreholeResult)
            params: Berechnungsparameter
            project_info: Projektinformationen (Name, Kunde, Adresse)
            borehole_config: Bohrfeld-Konfiguration (Anzahl, Abstände)
        """
        # PDF erstellen
        doc = SimpleDocTemplate(
            filepath,
            pagesize=A4,
            rightMargin=2*cm,
            leftMargin=2*cm,
            topMargin=2*cm,
            bottomMargin=2*cm
        )
        
        story = []
        
        # === TITELSEITE ===
        story.append(Spacer(1, 1*cm))
        
        # Logo-Platzhalter / Titel
        title = Paragraph(
            "Erdwärmesonden-Berechnung",
            self.styles['CustomTitle']
        )
        story.append(title)
        story.append(Spacer(1, 0.5*cm))
        
        # Datum
        date_para = Paragraph(
            f"<para align='center'>Erstellt am: {datetime.now().strftime('%d.%m.%Y %H:%M')}</para>",
            self.styles['CustomBody']
        )
        story.append(date_para)
        story.append(Spacer(1, 1*cm))
        
        # === PROJEKTINFORMATIONEN ===
        story.append(Paragraph("Projektinformationen", self.styles['CustomHeading']))
        
        project_data = [
            ['Projekt:', project_info.get('project_name', 'N/A')],
            ['Kunde:', project_info.get('customer_name', 'N/A')],
            ['Adresse:', project_info.get('address', 'N/A')],
            ['Ort:', project_info.get('city', 'N/A')],
            ['PLZ:', project_info.get('postal_code', 'N/A')]
        ]
        
        project_table = Table(project_data, colWidths=[4*cm, 13*cm])
        project_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e8f4f8')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
            ('ALIGN', (1, 0), (1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ]))
        story.append(project_table)
        story.append(Spacer(1, 0.8*cm))
        
        # === BOHRFELD-KONFIGURATION ===
        story.append(Paragraph("Bohrfeld-Konfiguration", self.styles['CustomHeading']))
        
        num_boreholes = borehole_config.get('num_boreholes', 1)
        borehole_data = [
            ['Anzahl Bohrungen:', str(num_boreholes)],
            ['Abstand zwischen Bohrungen:', f"{borehole_config.get('spacing_between', 6)} m"],
            ['Abstand zum Grundstücksrand:', f"{borehole_config.get('spacing_property', 3)} m"],
            ['Abstand zum Gebäude:', f"{borehole_config.get('spacing_building', 3)} m"],
            ['Bohrloch-Durchmesser:', f"{params.get('borehole_diameter', 0.152)*1000:.0f} mm"],
            ['Rohrkonfiguration:', params.get('pipe_configuration', 'single-u').upper()]
        ]
        
        borehole_table = Table(borehole_data, colWidths=[6*cm, 11*cm])
        borehole_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e8f4f8')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
            ('ALIGN', (1, 0), (1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ]))
        story.append(borehole_table)
        story.append(Spacer(1, 1*cm))
        
        # === BERECHNUNGSERGEBNISSE ===
        story.append(Paragraph("Berechnungsergebnisse", self.styles['CustomHeading']))
        
        results_data = [
            ['Parameter', 'Wert', 'Einheit'],
            ['Erforderliche Bohrtiefe (pro Bohrung)', f"{result.required_depth:.1f}", 'm'],
            ['Gesamte Bohrmeter', f"{result.required_depth * num_boreholes:.1f}", 'm'],
            ['Wärmeentzugsrate', f"{result.heat_extraction_rate:.2f}", 'W/m'],
            ['Gesamtleistung Bohrfeld', f"{result.heat_extraction_rate * result.required_depth * num_boreholes / 1000:.2f}", 'kW'],
            ['Min. Fluidtemperatur', f"{result.fluid_temperature_min:.2f}", '°C'],
            ['Max. Fluidtemperatur', f"{result.fluid_temperature_max:.2f}", '°C'],
            ['Bohrloch-Widerstand (Rb)', f"{result.borehole_resistance:.4f}", 'm·K/W'],
            ['Effektiver Widerstand', f"{result.effective_resistance:.4f}", 'm·K/W']
        ]
        
        results_table = Table(results_data, colWidths=[9*cm, 5*cm, 3*cm])
        results_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')])
        ]))
        story.append(results_table)
        story.append(Spacer(1, 1*cm))
        
        # === EINGABEPARAMETER ===
        story.append(PageBreak())
        story.append(Paragraph("Bodeneigenschaften", self.styles['CustomHeading']))
        
        ground_data = [
            ['Parameter', 'Wert', 'Einheit'],
            ['Wärmeleitfähigkeit Boden', f"{params.get('ground_thermal_conductivity', 0):.2f}", 'W/m·K'],
            ['Wärmekapazität Boden', f"{params.get('ground_heat_capacity', 0)/1e6:.2f}", 'MJ/m³·K'],
            ['Ungestörte Bodentemperatur', f"{params.get('undisturbed_ground_temp', 0):.1f}", '°C'],
            ['Geothermischer Gradient', f"{params.get('geothermal_gradient', 0)*100:.2f}", 'K/100m']
        ]
        
        ground_table = Table(ground_data, colWidths=[9*cm, 5*cm, 3*cm])
        ground_table.setStyle(self._get_table_style())
        story.append(ground_table)
        story.append(Spacer(1, 0.8*cm))
        
        # Rohr-Eigenschaften
        story.append(Paragraph("Rohr-Eigenschaften", self.styles['CustomHeading']))
        
        pipe_data = [
            ['Parameter', 'Wert', 'Einheit'],
            ['Außendurchmesser', f"{params.get('pipe_outer_diameter', 0)*1000:.1f}", 'mm'],
            ['Wandstärke', f"{params.get('pipe_wall_thickness', 0)*1000:.1f}", 'mm'],
            ['Wärmeleitfähigkeit Rohr', f"{params.get('pipe_thermal_conductivity', 0):.2f}", 'W/m·K'],
            ['Schenkelabstand', f"{params.get('shank_spacing', 0)*1000:.0f}", 'mm'],
            ['Wärmeleitfähigkeit Verfüllung', f"{params.get('grout_thermal_conductivity', 0):.2f}", 'W/m·K']
        ]
        
        pipe_table = Table(pipe_data, colWidths=[9*cm, 5*cm, 3*cm])
        pipe_table.setStyle(self._get_table_style())
        story.append(pipe_table)
        story.append(Spacer(1, 0.8*cm))
        
        # Lasten
        story.append(Paragraph("Heiz- und Kühllast", self.styles['CustomHeading']))
        
        load_data = [
            ['Parameter', 'Wert', 'Einheit'],
            ['Jahres-Heizenergie', f"{params.get('annual_heating_demand', 0):.2f}", 'MWh'],
            ['Jahres-Kühlenergie', f"{params.get('annual_cooling_demand', 0):.2f}", 'MWh'],
            ['Heiz-Spitzenlast', f"{params.get('peak_heating_load', 0):.1f}", 'kW'],
            ['Kühl-Spitzenlast', f"{params.get('peak_cooling_load', 0):.1f}", 'kW'],
            ['Wärmepumpen-COP', f"{params.get('heat_pump_cop', 0):.1f}", '-'],
            ['Simulationsdauer', f"{params.get('simulation_years', 25):.0f}", 'Jahre']
        ]
        
        load_table = Table(load_data, colWidths=[9*cm, 5*cm, 3*cm])
        load_table.setStyle(self._get_table_style())
        story.append(load_table)
        story.append(Spacer(1, 1*cm))
        
        # === VISUALISIERUNGEN ===
        story.append(PageBreak())
        story.append(Paragraph("Visualisierungen", self.styles['CustomHeading']))
        
        # Erstelle Diagramme
        temp_plot_path = self._create_temperature_plot(result)
        borehole_plot_path = self._create_detailed_borehole_plot(params, result)
        
        if temp_plot_path and os.path.exists(temp_plot_path):
            story.append(Paragraph("Monatliche Fluidtemperaturen", self.styles['CustomBody']))
            img = Image(temp_plot_path, width=16*cm, height=10*cm)
            story.append(img)
            story.append(Spacer(1, 0.5*cm))
        
        if borehole_plot_path and os.path.exists(borehole_plot_path):
            story.append(Paragraph("Bohrloch-Schema mit Werten", self.styles['CustomBody']))
            img = Image(borehole_plot_path, width=16*cm, height=12*cm)
            story.append(img)
        
        # === FUSSNOTE ===
        story.append(Spacer(1, 2*cm))
        footer = Paragraph(
            "<para align='center'><font size=8>"
            "Dieser Bericht wurde automatisch mit dem Geothermie Erdsonden-Berechnungstool erstellt.<br/>"
            "Open Source Software - MIT Lizenz<br/>"
            "Berechnungen nach VDI 4640, Eskilson (1987) und Hellström (1991)"
            "</font></para>",
            self.styles['Normal']
        )
        story.append(footer)
        
        # PDF bauen
        doc.build(story)
        
        # Temporäre Dateien löschen
        if temp_plot_path and os.path.exists(temp_plot_path):
            os.remove(temp_plot_path)
        if borehole_plot_path and os.path.exists(borehole_plot_path):
            os.remove(borehole_plot_path)
    
    def _get_table_style(self):
        """Gibt einen Standard-Tabellenstyle zurück."""
        return TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')])
        ])
    
    def _create_temperature_plot(self, result):
        """Erstellt das Temperatur-Diagramm."""
        try:
            fig, ax = plt.subplots(figsize=(12, 6))
            
            months = ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 
                     'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez']
            x = range(len(months))
            
            ax.plot(x, result.monthly_temperatures, 'o-', linewidth=2.5, 
                   markersize=8, color='#1f4788', label='Monatliche Temperatur')
            ax.axhline(y=result.fluid_temperature_min, color='blue', linestyle='--', 
                      linewidth=2, label=f'Min: {result.fluid_temperature_min:.1f}°C')
            ax.axhline(y=result.fluid_temperature_max, color='red', linestyle='--',
                      linewidth=2, label=f'Max: {result.fluid_temperature_max:.1f}°C')
            
            ax.set_xlabel('Monat', fontsize=14, fontweight='bold')
            ax.set_ylabel('Temperatur [°C]', fontsize=14, fontweight='bold')
            ax.set_title('Jahresverlauf der Fluidtemperatur', fontsize=16, fontweight='bold')
            ax.set_xticks(x)
            ax.set_xticklabels(months)
            ax.grid(True, alpha=0.3, linestyle='--')
            ax.legend(fontsize=12, loc='best')
            
            plt.tight_layout()
            
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            plt.savefig(temp_file.name, dpi=150, bbox_inches='tight')
            plt.close(fig)
            
            return temp_file.name
        except Exception as e:
            print(f"Fehler beim Erstellen des Temperatur-Plots: {e}")
            return None
    
    def _create_detailed_borehole_plot(self, params, result):
        """Erstellt eine detaillierte Bohrloch-Grafik mit Beschriftungen."""
        try:
            fig, ax = plt.subplots(figsize=(14, 10))
            
            # Bohrloch-Parameter
            depth = result.required_depth
            bh_diameter = params.get('borehole_diameter', 0.152)
            pipe_diameter = params.get('pipe_outer_diameter', 0.040)
            
            # Skalierung für bessere Darstellung
            scale = 100  # cm
            depth_cm = depth * scale
            bh_radius_cm = (bh_diameter / 2) * scale
            pipe_radius_cm = (pipe_diameter / 2) * scale
            
            # Bohrloch zeichnen
            borehole = Rectangle(
                (-bh_radius_cm, 0), 2*bh_radius_cm, depth_cm,
                facecolor='#d9d9d9', edgecolor='black', linewidth=2
            )
            ax.add_patch(borehole)
            
            # 4 Rohre zeichnen (typische Position für 4-Rohr-System)
            pipe_positions = [
                (-bh_radius_cm*0.5, depth_cm*0.5),  # Links oben
                (bh_radius_cm*0.5, depth_cm*0.5),   # Rechts oben
                (-bh_radius_cm*0.5, depth_cm*0.8),  # Links unten
                (bh_radius_cm*0.5, depth_cm*0.8)    # Rechts unten
            ]
            
            colors_pipes = ['#ff6b6b', '#4ecdc4', '#ff6b6b', '#4ecdc4']
            labels_pipes = ['Vorlauf 1', 'Rücklauf 1', 'Vorlauf 2', 'Rücklauf 2']
            
            for i, ((x, y), color, label) in enumerate(zip(pipe_positions, colors_pipes, labels_pipes)):
                pipe = Circle((x, y), pipe_radius_cm*2, 
                            facecolor=color, edgecolor='black', linewidth=1.5,
                            alpha=0.8, label=label if i < 2 else '')
                ax.add_patch(pipe)
                
                # Beschriftung
                ax.text(x, y, str(i+1), ha='center', va='center', 
                       fontsize=10, fontweight='bold', color='white')
            
            # Beschriftungen mit Pfeilen
            # Bohrtiefe
            ax.annotate(f'Bohrtiefe:\n{depth:.1f} m', 
                       xy=(bh_radius_cm*1.5, depth_cm/2),
                       xytext=(bh_radius_cm*3, depth_cm/2),
                       fontsize=12, fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                       arrowprops=dict(arrowstyle='->', lw=2, color='black'))
            
            # Bohrloch-Durchmesser
            ax.plot([0, 0], [-bh_radius_cm*1.5, 0], 'k-', linewidth=1)
            ax.plot([-bh_radius_cm, bh_radius_cm], [-bh_radius_cm, -bh_radius_cm], 'k-', linewidth=2)
            ax.plot([-bh_radius_cm, -bh_radius_cm], [-bh_radius_cm*1.2, -bh_radius_cm*0.8], 'k-', linewidth=2)
            ax.plot([bh_radius_cm, bh_radius_cm], [-bh_radius_cm*1.2, -bh_radius_cm*0.8], 'k-', linewidth=2)
            ax.text(0, -bh_radius_cm*2, f'Ø {bh_diameter*1000:.0f} mm',
                   ha='center', fontsize=11, fontweight='bold')
            
            # Wärmeentzugsrate
            ax.annotate(f'Wärmeentzug:\n{result.heat_extraction_rate:.1f} W/m',
                       xy=(-bh_radius_cm*1.5, depth_cm*0.2),
                       xytext=(-bh_radius_cm*4, depth_cm*0.2),
                       fontsize=12, fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.7),
                       arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
            
            # Temperaturbereich
            temp_text = f'Fluid-Temp:\n{result.fluid_temperature_min:.1f}°C bis {result.fluid_temperature_max:.1f}°C'
            ax.annotate(temp_text,
                       xy=(bh_radius_cm*1.5, depth_cm*0.8),
                       xytext=(bh_radius_cm*3, depth_cm*0.8),
                       fontsize=11, fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.7),
                       arrowprops=dict(arrowstyle='->', lw=2, color='red'))
            
            # Rohrdurchmesser
            ax.annotate(f'Rohr Ø {pipe_diameter*1000:.0f} mm',
                       xy=pipe_positions[0],
                       xytext=(-bh_radius_cm*4, depth_cm*0.5),
                       fontsize=10,
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8),
                       arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))
            
            # Titel und Achsen
            ax.set_title('Erdwärmesonden-Schema (4-Rohr-System)', 
                        fontsize=16, fontweight='bold', pad=20)
            ax.set_xlabel('Breite [cm]', fontsize=12)
            ax.set_ylabel('Tiefe [cm]', fontsize=12)
            ax.set_aspect('equal')
            ax.grid(True, alpha=0.2, linestyle='--')
            ax.legend(loc='upper right', fontsize=10)
            
            # Achsengrenzen
            ax.set_xlim(-bh_radius_cm*5, bh_radius_cm*4)
            ax.set_ylim(-bh_radius_cm*3, depth_cm*1.1)
            ax.invert_yaxis()
            
            plt.tight_layout()
            
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            plt.savefig(temp_file.name, dpi=150, bbox_inches='tight')
            plt.close(fig)
            
            return temp_file.name
        except Exception as e:
            print(f"Fehler beim Erstellen des Bohrloch-Plots: {e}")
            return None


if __name__ == "__main__":
    print("PDF-Export-Modul geladen")

