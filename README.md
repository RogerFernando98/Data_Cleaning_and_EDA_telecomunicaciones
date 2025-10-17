#  Limpieza y Análisis de Datos - Telco Customer Churn

##  Objetivo
El objetivo principal de este proyecto es **practicar los fundamentos de Python y Pandas aplicados a la limpieza y exploración de datos (EDA)**. Y probablemente el siguiente reto u objetivo sea predecir qué clientes se van a ir de la compañia en los próximos trimestres.

---

##  Contexto
Este proyecto utiliza un dataset ficticio de una compañía de telecomunicaciones que ofrece servicios de telefonía fija e internet a 7.043 clientes en EEUU. 
La fuga de clientes es un reto común en la industria de las telecomunicaciones.

---

##  Datos
El conjunto de datos contiene información sobre:

- **Demografía** → género, edad aproximada, dependientes, etc.  
- **Localización** → ciudad, código postal, latitud/longitud.  
- **Servicios contratados** → internet, telefonía, seguridad online, streaming, soporte técnico, etc.  
- **Condiciones contractuales** → tipo de contrato, facturación electrónica, método de pago.  
- **Tipos de cargos** → cargo mensual, cargos totales, CLTV (*Customer Lifetime Value*).  
- **Churn(abandono y motivo)** → indicador de baja (0/1), score de churn y motivo de cancelación (si aplica).  

---

##  Estructura del Repositorio
```bash
01_DATA_CLEANING_AND_EDA/
│── Data/
│   ├── raw/                # Datos originales
│   │   └── Telco_customer_churn.xlsx
│   └── processed/          # Datos limpios
│       └── cleaned_data.csv
│
│── src/                    # Código fuente (scripts y notebooks)
│   └── primera_aproximacion.ipynb
│
│── requirements.txt        # Dependencias del proyecto
│── README.md               # Este documento
│── LICENSE                 # Licencia
```

---

##  Librerías y entorno

Este proyecto fue desarrollado en **Python 3.13.0**, utilizando un entorno virtual creado con `venv` para asegurar la reproducibilidad.

 **Librerías principales**

	•   pandas  → Manejo y análisis de datos en formato tabular (DataFrames). Usada para limpieza, transformación y exploración.

	•	numpy → Librería de cálculo numérico eficiente. Soporte a arrays y operaciones matemáticas de base.

	•	matplotlib.pyplot → Visualización de datos. Permite crear gráficos básicos como histogramas, boxplots o scatterplots.

	•	seaborn → Librería de visualización estadística construida sobre matplotlib. Facilita gráficos más atractivos y con análisis exploratorios más rápidos.

	•	warnings → Usada para ignorar mensajes de advertencia y mantener las salidas limpias.

	•	Configuración de pandas (pd.options.display.max_columns = None) → Permite mostrar todas las columnas de un DataFrame sin cortes, facilitando el análisis.

Todas las dependencias se gestionan a través del archivo **`requirements.txt`**, lo que permite instalar el entorno completo con un solo comando:

```bash
pip install -r requirements.txt
```

---

##  Metodología

1. **Carga de datos** con ruta relativa → garantiza reproducibilidad del proyecto en cualquier entorno.  
2. **Exploración inicial** con funciones personalizadas (`data_resume`) para revisar tipos, nulos y valores únicos.  
3. **Limpieza estructurada**:
   - Normalización de nombres de columnas.  
   - Eliminación de columnas redundantes (`count`, `country`, `state`, `lat_long`, `churn_label`).  
   - Tratamiento de nulos (caso especial `churn_reason`).  
   - Conversión de tipos (`total_charges` a float, varias columnas binarias a 0/1).  
4. **EDA exhaustivo**:
   - Distribuciones de variables categóricas y numéricas.  
   - Boxplots y scatterplots para detectar outliers.  
   - Relación de variables con `churn_value`.  
   - Validación de coherencia entre `internet_service` y servicios dependientes (seguridad, backup, streaming).  
5. **Exportación de datos procesados** → `cleaned_data.csv` en `Data/processed/`.  

---

##  Resultados principales Finales del EDA

- Los principales factores asociados al churn son:
  - **Tipo de contrato** → los clientes *Month-to-month* presentan mayor fuga.  
  - **Método de pago** → *Electronic check* concentra el mayor churn.  
  - **Tipo de internet** → fibra óptica se asocia con más churn que DSL.  
  - **Características demográficas** → clientes seniors, sin pareja ni dependientes, tienen mayor probabilidad de irse.  
- Variables como **gender** no muestran impacto relevante.  50% hombres / 50% mujeres
- **Clientes más nuevos, con facturas más altas y menor valor acumulado son los más propensos a churn.**  
- Los datos presentan **coherencia interna** (ej: clientes sin internet nunca tienen add-ons).  

---

##  Next Steps

- Añadir un modelo predictivo (clasificación) para predecir la probabilidad de churn (abandono clientes de la compañia).
- Realizar una segmentación de clientes (clustering) para entender perfiles. Esto debido a que muchos de los clientes que no tienen `internet_service` carecen de casi todos los otros servicios.
- Crear un dashboard interactivo (ej. con Power BI o Streamlit) para comunicar hallazgos.
- Optimizar el preprocesamiento con pipelines en src/.

---

##  Autor

Proyecto desarrollado por Fernando Arroyo como práctica de limpieza y exploración de datos en Python. Todo esto no hubiese sido posible sin la supervición, guí y motivación de uno de los grandes prodijios de la Ciencia de datos, Jean Charles.
	
    •	 LinkedIn: www.linkedin.com/in/f-arroyo-herrera

