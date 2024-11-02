Aquí tienes un `README.md` resumido pero completo:

---

# AlojamientosDataProcessing

**Repositorio para procesar datos de alojamientos y generar reservas aleatorias**

## Descripción

Este proyecto incluye dos scripts en Python:
- `alojamientos.py`: Procesa datos de alojamientos en un archivo CSV.
- `generadorDeReservas.py`: Genera reservas aleatorias para estos alojamientos y las guarda en un archivo Excel.

## Requisitos

- Python 3.x
- Librerías: `pandas`, `openpyxl`

Instala las dependencias ejecutando:
```bash
pip install pandas openpyxl
```

## Uso

### Procesamiento de Alojamientos (`alojamientos.py`)

1. **Funcionalidad**: Elimina columnas innecesarias, formatea valores numéricos y de texto, filtra registros, y añade una columna con la plataforma de publicación.
2. **Ejecución**:
   - Asegúrate de tener un archivo `alojamientos.csv` en la carpeta del script.
   - Ejecuta:
     ```bash
     python alojamientos.py
     ```
   - Resultado: Se genera `AlojamientosEditado.csv` con los datos procesados.

### Generación de Reservas (`generadorDeReservas.py`)

1. **Funcionalidad**: Crea reservas aleatorias cumpliendo las siguientes reglas:
   - Límite de 4 reservas por cliente y 20 por alojamiento.
   - Verificación de superposición de fechas para evitar conflictos.
2. **Ejecución**:
   - Coloca el archivo `Alojamientos 3.0.xlsx` en la carpeta `Dataset Alojamientos`.
   - Ejecuta:
     ```bash
     python generadorDeReservas.py
     ```
   - Resultado: Se genera `Hoja de Alquileres.xlsx` con las reservas.

## Contribución

Si deseas mejorar este proyecto, haz un fork y envía un pull request. Puedes ayudar a modularizar el código o añadir más opciones de procesamiento de datos.

---

Este `README.md` cubre todos los aspectos clave de ambos scripts de manera resumida.
