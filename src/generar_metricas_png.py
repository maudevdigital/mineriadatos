"""
Script para generar visualizaciones PNG de las métricas de los modelos.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from pathlib import Path

# Configurar matplotlib para modo no interactivo
plt.switch_backend('Agg')

def generar_tabla_metricas_comparativa():
    """Genera imagen PNG con tabla comparativa de métricas."""
    
    # Datos de las métricas
    modelos = ['Regresión\nLogística', 'Random\nForest']
    metrics_data = {
        'Accuracy': [85.26, 85.67],
        'Precision': [73.82, 79.59],
        'Recall': [60.08, 54.46],
        'F1-Score': [66.24, 64.67],
        'ROC-AUC': [90.24, 90.70]
    }
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Crear tabla
    cell_text = []
    for i, modelo in enumerate(modelos):
        row = [modelo]
        for metric in metrics_data.keys():
            row.append(f'{metrics_data[metric][i]:.2f}%')
        cell_text.append(row)
    
    # Crear tabla
    table = ax.table(
        cellText=cell_text,
        colLabels=['Modelo'] + list(metrics_data.keys()),
        cellLoc='center',
        loc='center',
        colWidths=[0.20, 0.16, 0.16, 0.16, 0.16, 0.16]
    )
    
    # Estilo de la tabla
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2.5)
    
    # Colores del header
    for i in range(6):
        table[(0, i)].set_facecolor('#2E86AB')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Colores alternados para filas
    colors = ['#E8F4F8', '#D4E9F7']
    for i in range(1, 3):
        for j in range(6):
            table[(i, j)].set_facecolor(colors[i-1])
            
    # Destacar mejores valores
    # F1-Score de LR
    table[(1, 4)].set_facecolor('#90EE90')
    table[(1, 4)].set_text_props(weight='bold')
    
    # Precision de RF
    table[(2, 2)].set_facecolor('#FFE4B5')
    table[(2, 2)].set_text_props(weight='bold')
    
    # ROC-AUC de RF
    table[(2, 5)].set_facecolor('#FFE4B5')
    table[(2, 5)].set_text_props(weight='bold')
    
    # Título
    ax.set_title('Comparación de Métricas de Rendimiento\nEvaluación Holdout (80/20)', 
                 fontsize=16, fontweight='bold', pad=20)
    
    # Ocultar ejes
    ax.axis('off')
    
    # Añadir leyenda
    legend_elements = [
        mpatches.Patch(facecolor='#90EE90', label='Mejor F1-Score (Regresión Logística)'),
        mpatches.Patch(facecolor='#FFE4B5', label='Mejor Precision/AUC (Random Forest)')
    ]
    ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.05), 
             ncol=2, frameon=False, fontsize=10)
    
    # Guardar
    output_dir = Path('/workspaces/mineriadatos/results/visualizaciones')
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / 'tabla_metricas_comparativa.png'
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    return output_path


def generar_grafico_barras_metricas():
    """Genera gráfico de barras agrupadas con las métricas."""
    
    # Datos
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC']
    lr_values = [85.26, 73.82, 60.08, 66.24, 90.24]
    rf_values = [85.67, 79.59, 54.46, 64.67, 90.70]
    
    x = np.arange(len(metrics))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Barras
    bars1 = ax.bar(x - width/2, lr_values, width, label='Regresión Logística', 
                   color='#2E86AB', alpha=0.8, edgecolor='black', linewidth=1.5)
    bars2 = ax.bar(x + width/2, rf_values, width, label='Random Forest', 
                   color='#A23B72', alpha=0.8, edgecolor='black', linewidth=1.5)
    
    # Añadir valores en las barras
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                   f'{height:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Configuración
    ax.set_xlabel('Métricas', fontsize=14, fontweight='bold')
    ax.set_ylabel('Porcentaje (%)', fontsize=14, fontweight='bold')
    ax.set_title('Comparación de Rendimiento: Regresión Logística vs Random Forest', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=12)
    ax.legend(loc='upper right', fontsize=12, frameon=True, shadow=True)
    ax.set_ylim(0, 100)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Línea de referencia
    ax.axhline(y=50, color='red', linestyle='--', linewidth=1, alpha=0.5, label='Baseline 50%')
    
    plt.tight_layout()
    
    # Guardar
    output_dir = Path('/workspaces/mineriadatos/results/visualizaciones')
    output_path = output_dir / 'grafico_barras_metricas.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    return output_path


def generar_tabla_validacion_cruzada():
    """Genera imagen PNG con tabla de validación cruzada."""
    
    fig, ax = plt.subplots(figsize=(12, 5))
    
    # Datos
    cell_text = [
        ['Regresión Logística', 'Holdout', '66.24%', 'Valor puntual'],
        ['Regresión Logística', 'CV 5-fold', '66.09% ± 1.00%', 'Media ± Desv. Est.'],
        ['Random Forest', 'Holdout', '64.67%', 'Valor puntual'],
        ['Random Forest', 'CV 5-fold', '64.86% ± 0.94%', 'Media ± Desv. Est.']
    ]
    
    # Crear tabla
    table = ax.table(
        cellText=cell_text,
        colLabels=['Modelo', 'Método', 'F1-Score', 'Tipo'],
        cellLoc='center',
        loc='center',
        colWidths=[0.30, 0.20, 0.25, 0.25]
    )
    
    # Estilo
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2.5)
    
    # Colores del header
    for i in range(4):
        table[(0, i)].set_facecolor('#2E86AB')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Colores alternados
    colors = ['#E8F4F8', '#D4E9F7']
    for i in range(1, 5):
        color_idx = 0 if i <= 2 else 1
        for j in range(4):
            table[(i, j)].set_facecolor(colors[color_idx])
    
    # Destacar CV
    for i in [2, 4]:
        table[(i, 2)].set_facecolor('#90EE90')
        table[(i, 2)].set_text_props(weight='bold')
    
    # Título
    ax.set_title('Validación Cruzada: Comparación Holdout vs CV 5-fold\nConsistencia y Robustez de los Modelos', 
                 fontsize=16, fontweight='bold', pad=20)
    
    ax.axis('off')
    
    # Nota al pie
    fig.text(0.5, 0.05, 'Diferencia < 0.5% indica excelente consistencia | Desv. Est. < 1% indica baja varianza', 
             ha='center', fontsize=10, style='italic', color='#555555')
    
    plt.tight_layout()
    
    # Guardar
    output_dir = Path('/workspaces/mineriadatos/results/visualizaciones')
    output_path = output_dir / 'tabla_validacion_cruzada.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    return output_path


def generar_radar_chart_metricas():
    """Genera gráfico de radar comparando métricas."""
    
    categories = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC']
    lr_values = [85.26, 73.82, 60.08, 66.24, 90.24]
    rf_values = [85.67, 79.59, 54.46, 64.67, 90.70]
    
    # Número de variables
    N = len(categories)
    
    # Ángulos para cada eje
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    lr_values += lr_values[:1]
    rf_values += rf_values[:1]
    angles += angles[:1]
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    
    # Dibujar gráficos
    ax.plot(angles, lr_values, 'o-', linewidth=2, label='Regresión Logística', color='#2E86AB')
    ax.fill(angles, lr_values, alpha=0.25, color='#2E86AB')
    
    ax.plot(angles, rf_values, 'o-', linewidth=2, label='Random Forest', color='#A23B72')
    ax.fill(angles, rf_values, alpha=0.25, color='#A23B72')
    
    # Configurar etiquetas
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12, fontweight='bold')
    
    # Configurar límites
    ax.set_ylim(0, 100)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], fontsize=10)
    
    # Título y leyenda
    ax.set_title('Perfil de Rendimiento: Radar Chart de Métricas', 
                 fontsize=16, fontweight='bold', pad=20, y=1.08)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=12, frameon=True, shadow=True)
    
    # Grid
    ax.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    
    # Guardar
    output_dir = Path('/workspaces/mineriadatos/results/visualizaciones')
    output_path = output_dir / 'radar_chart_metricas.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    return output_path


def main():
    """Genera todas las visualizaciones de métricas."""
    print("=" * 80)
    print("GENERANDO VISUALIZACIONES PNG DE MÉTRICAS")
    print("=" * 80)
    
    visualizaciones = []
    
    # 1. Tabla comparativa
    print("\n1. Generando tabla comparativa de métricas...")
    path1 = generar_tabla_metricas_comparativa()
    visualizaciones.append(('Tabla Comparativa', path1))
    print(f"   ✓ Creado: {path1.name}")
    
    # 2. Gráfico de barras
    print("\n2. Generando gráfico de barras agrupadas...")
    path2 = generar_grafico_barras_metricas()
    visualizaciones.append(('Gráfico de Barras', path2))
    print(f"   ✓ Creado: {path2.name}")
    
    # 3. Tabla de validación cruzada
    print("\n3. Generando tabla de validación cruzada...")
    path3 = generar_tabla_validacion_cruzada()
    visualizaciones.append(('Tabla CV', path3))
    print(f"   ✓ Creado: {path3.name}")
    
    # 4. Radar chart
    print("\n4. Generando radar chart de métricas...")
    path4 = generar_radar_chart_metricas()
    visualizaciones.append(('Radar Chart', path4))
    print(f"   ✓ Creado: {path4.name}")
    
    print("\n" + "=" * 80)
    print("✅ TODAS LAS VISUALIZACIONES GENERADAS EXITOSAMENTE")
    print("=" * 80)
    
    print("\n📊 ARCHIVOS CREADOS:")
    for nombre, path in visualizaciones:
        print(f"   • {nombre}: {path}")
    
    print("\n📁 Ubicación: /workspaces/mineriadatos/results/visualizaciones/")
    print("\n💡 Uso: Puedes incluir estas imágenes en tu presentación o informe")
    print("=" * 80)


if __name__ == "__main__":
    main()
