# Importamos las librerías que necesitamos

# Tratamiento de datos
# -----------------------------------------------------------------------
import pandas as pd #manejo de estructura de datos tabulares
import numpy as np # operaciones matematicas

# Visualización de datos
# -----------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns



def data_resume(df):
    """
    Devuelve un resumen de los datos del dataframe con el recuento de valores, valores nulos, porcentaje de valores nulos, tipo de dato y número de valores únicos por columna. 

    Args:
        df (pd.DataFrame): dataframe a resumir.

    Returns:
        pd.DataFrame: resumen de los datos del dataframe.
    """
    df_resume = pd.DataFrame(columns=["count", "null", "null_%", "dtype", "unique"])
    dict_resume = {}
    for i in df.columns:
        dict_resume["count"] = df[i].count()
        dict_resume["null"] = df[i].isnull().sum()
        dict_resume["null_%"] = round(df[i].isnull().sum()/len(df),4)
        dict_resume["dtype"] = df[i].dtype
        dict_resume["unique"] = df[i].nunique()
        df_aux = pd.DataFrame(dict_resume, index=[i])
        df_resume = pd.concat([df_resume, df_aux], axis=0)
    return df_resume.sort_values(by="null_%", ascending=False)



def plot_nulos(df):
    """
    Devuelve un heatmap con los valores nulos del dataframe.

    Args:
        df (pd.DataFrame): dataframe a visualizar.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=True, yticklabels=False, cmap='viridis', annot=False)
    plt.title('Valores Nulos en el Dataset')
    plt.show()

def categorize_cv(x):
    if not np.isfinite(x):
        return "no aplicable"
    if x < 10:
        return "muy baja"
    elif x < 20:
        return "baja"
    elif x < 40:
        return "moderada"
    elif x < 60:
        return "alta"
    else:
        return "muy alta"

def plot_distribution_with_stats(df, column, figsize=(10, 6), bins=30, kde=True, 
                                 show_mode=True, show_quartiles=True):
    """
    Crea un histograma con estadísticos descriptivos marcados con líneas verticales
    e incluye la evaluación del Coeficiente de Variación (CV).
    
    Parámetros:
    -----------
    df : pandas.DataFrame
        DataFrame que contiene los datos
    column : str
        Nombre de la columna a graficar
    figsize : tuple, default (10, 6)
        Tamaño de la figura (ancho, alto)
    bins : int, default 30
        Número de bins para el histograma
    kde : bool, default True
        Si mostrar la curva de densidad kernel
    show_mode : bool, default True
        Si mostrar la línea de la moda
    show_quartiles : bool, default True
        Si mostrar las líneas Q1 y Q3
    
    Returns:
    --------
    dict : Diccionario con todos los estadísticos calculados, incluyendo:
           'cv' (en %), 'cv_valid' (bool) y 'cv_category'
    """

    # --- Programacion defensiva --- 
    # Verificar que la columna existe
    if column not in df.columns:
        raise ValueError(f"La columna '{column}' no existe en el DataFrame")
    
    # Eliminar valores nulos para los cálculos
    data = df[column].dropna()
    
    # Verificar que tenemos datos
    if len(data) == 0:
        raise ValueError(f"La columna '{column}' no tiene valores válidos")
    

    # --- Calcular estadísticos básicos ---
    mean_ = data.mean()
    median_ = data.median()
    mode_ = data.mode()[0] if len(data.mode()) > 0 else np.nan
    q1_ = data.quantile(0.25)
    q3_ = data.quantile(0.75)
    std_ = data.std()
    min_ = data.min()
    max_ = data.max()
    count_ = len(data)
    iqr_ = q3_ - q1_

    # --- Coeficiente de Variación (CV) ---
    # Validez: CV es apropiado para variables en escala de razón y con media > 0
    # También evitamos inestabilidad cuando la media está demasiado cerca de 0
    eps = 1e-12
    cv_valid = bool(mean_ > 0 and abs(mean_) > eps and np.isfinite(std_))
    if cv_valid:
        cv = (std_ / mean_) * 100.0
    else:
        cv = np.nan
    cv_category = categorize_cv(cv)

    # Consolidar estadísticos
    stats = {
        'mean': mean_,
        'median': median_,
        'mode': mode_,
        'q1': q1_,
        'q3': q3_,
        'std': std_,
        'min': min_,
        'max': max_,
        'count': count_,
        'iqr': iqr_,
        'cv': cv,                 # porcentaje
        'cv_valid': cv_valid,     # bool
        'cv_category': cv_category
    }
    
    # Crear la figura
    plt.figure(figsize=figsize)
    
    # Crear el histograma con KDE
    sns.histplot(data, kde=kde, bins=bins, alpha=0.7, color='skyblue')
    
    # Añadir líneas verticales para estadísticos principales
    plt.axvline(stats['mean'], color='green', linestyle='dashed', 
                linewidth=2, label=f'Media: {stats["mean"]:.2f}')
    
    plt.axvline(stats['median'], color='orange', linestyle='dashed', 
                linewidth=2, label=f'Mediana: {stats["median"]:.2f}')
    
    # Añadir moda si se solicita y existe
    if show_mode and not pd.isna(stats['mode']):
        plt.axvline(stats['mode'], color='yellow', linestyle='dashed', 
                    linewidth=2, label=f'Moda: {stats["mode"]:.2f}')
    
    # Añadir cuartiles si se solicita
    if show_quartiles:
        plt.axvline(stats['q1'], color='purple', linestyle='dotted', 
                    linewidth=2, label=f'Q1: {stats["q1"]:.2f}')
        plt.axvline(stats['q3'], color='purple', linestyle='dotted', 
                    linewidth=2, label=f'Q3: {stats["q3"]:.2f}')
    
    # Configurar título y etiquetas
    plt.title(f'Distribución de {column}', fontsize=14, fontweight='bold')
    plt.xlabel(column, fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    
    # Añadir leyenda
    plt.legend(loc='best')
    
    # Añadir grid para mejor legibilidad
    plt.grid(True, alpha=0.3)

    # --- Anotación del CV en el gráfico ---
    if stats['cv_valid']:
        cv_text = f"CV: {stats['cv']:.2f}% ({stats['cv_category']})"
    else:
        cv_text = "CV: no aplicable (media ≤ 0 o ~0)"
    plt.gcf().text(0.99, 0.02, cv_text, ha='right', va='bottom',
                   fontsize=10, bbox=dict(boxstyle='round', facecolor='white', alpha=0.7, edgecolor='gray'))

    # Ajustar layout
    plt.tight_layout()
    
    # Mostrar gráfico
    plt.show()
    
    # Imprimir resumen estadístico
    print(f"\nRESUMEN ESTADÍSTICO DE '{column}':")
    print("=" * 40)
    print(f"Observaciones: {stats['count']:,}")
    print(f"Media:         {stats['mean']:.2f}")
    print(f"Mediana:       {stats['median']:.2f}")
    if not pd.isna(stats['mode']):
        print(f"Moda:          {stats['mode']:.2f}")
    print(f"Desv. Std:     {stats['std']:.2f}")
    print(f"Q1:            {stats['q1']:.2f}")
    print(f"Q3:            {stats['q3']:.2f}")
    print(f"Rango IQR:     {stats['iqr']:.2f}")
    print(f"Mínimo:        {stats['min']:.2f}")
    print(f"Máximo:        {stats['max']:.2f}")

    # CV en el resumen
    if stats['cv_valid']:
        print(f"Coef. Variación: {stats['cv']:.2f}% ({stats['cv_category']})")
    else:
        print("Coef. Variación: no aplicable (requiere media > 0 y alejada de 0)")

    # Análisis de la distribución
    print(f"\nANÁLISIS DE LA DISTRIBUCIÓN:")
    print("-" * 30)
    diff_mean_median = abs(stats['mean'] - stats['median'])
    print(f"Diferencia |Media - Mediana|: {diff_mean_median:.2f}")
    
    if diff_mean_median < stats['std'] * 0.1:
        print("→ Distribución SIMÉTRICA")
        print("→ Recomendación: MEDIA para imputación")
    elif stats['mean'] > stats['median']:
        print("→ Distribución con SESGO POSITIVO (cola derecha)")
        print("→ Recomendación: MEDIANA para imputación")
    else:
        print("→ Distribución con SESGO NEGATIVO (cola izquierda)")
        print("→ Recomendación: MEDIANA para imputación")
    
    # Nota interpretativa del CV
    if stats['cv_valid']:
        if stats['cv'] < 10:
            print("→ CV muy bajo: datos muy homogéneos respecto a la media.")
        elif stats['cv'] < 20:
            print("→ CV bajo: la media es representativa.")
        elif stats['cv'] < 40:
            print("→ CV moderado: variabilidad apreciable, la media aún es útil.")
        elif stats['cv'] < 60:
            print("→ CV alto: cautela al usar la media como resumen.")
        else:
            print("→ CV muy alto: la media es poco representativa; considerar transformaciones (p.ej., log).")
    else:
        print("→ CV no aplicable: variable no apta (media ≤ 0 o muy cercana a 0) para interpretar variabilidad relativa.")

    return stats
