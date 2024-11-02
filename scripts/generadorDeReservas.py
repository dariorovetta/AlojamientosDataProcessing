import os
import pandas as pd
import random
from datetime import datetime, timedelta

# Acceder a la ruta donde se encuentra el archivo Excel
ruta = os.getcwd()

# Leer las distintas hojas del archivo de Excel (Alojamientos y Clientes)
hojaAlojamientos = pd.read_excel(ruta + r"\Dataset Alojamientos\Alojamientos 3.0.xlsx", sheet_name='Alojamientos')
hojaClientes = pd.read_excel(ruta + r"\Dataset Alojamientos\Alojamientos 3.0.xlsx", sheet_name='Clientes')

def check_overlap(df, start_date, end_date):
    """
    Verifica si las fechas de la nueva reserva se superponen con reservas existentes
    para evitar conflictos de fechas en el mismo alojamiento o cliente.
    
    Parámetros:
    - df: DataFrame con las reservas existentes
    - start_date: fecha de inicio de la nueva reserva
    - end_date: fecha de finalización de la nueva reserva
    
    Retorna:
    - Booleano indicando si hay superposición de fechas
    """
    overlap = ((df['INICIO'] <= start_date) & (df['FIN'] > start_date)) | \
              ((df['INICIO'] < end_date) & (df['FIN'] >= end_date)) | \
              ((df['INICIO'] >= start_date) & (df['FIN'] <= end_date))
    return overlap.any()

def random_date_range(start, end, days):
    """
    Genera un rango de fechas aleatorio para una reserva.
    
    Parámetros:
    - start: fecha mínima de inicio
    - end: fecha máxima de inicio
    - days: duración de la reserva en días
    
    Retorna:
    - Tupla con la fecha de inicio y fin de la reserva
    """
    start_date = start + timedelta(days=random.randint(0, (end - start).days))
    end_date = start_date + timedelta(days=days)
    return start_date, end_date

# Crear el DataFrame con las columnas necesarias para las reservas
df = pd.DataFrame(columns=['ID_ALQUILER', 'ID_ALOJAMIENTO', 'ID_CLIENTE', 'INICIO', 'FIN'])

# Seleccionar los IDs de alojamientos y clientes
alojamientos = hojaAlojamientos["ID_ALOJAMIENTO"]
clientes = hojaClientes["ID_CLIENTE"]

# Bucle para generar 6000 reservas aleatorias
reservas = 0
while reservas < 6000:
    start = datetime(2023, 1, 1)
    end = datetime(2023, 5, 30)
    days = random.randint(2, 7)  # Duración de cada reserva entre 2 y 7 días
    start_date, end_date = random_date_range(start, end, days)
    clienteElegido = random.choice(clientes)
    alojamientoElegido = random.choice(alojamientos)

    # Filtrar reservas existentes para el cliente y alojamiento seleccionados
    dfReservasDeEseCliente = df[df["ID_CLIENTE"] == clienteElegido]
    dfReservasDeEseAlojamiento = df[df["ID_ALOJAMIENTO"] == alojamientoElegido]

    # Validación de condiciones: máximo 4 reservas por cliente y 20 por alojamiento, y sin superposición
    if df["ID_CLIENTE"].str.count(clienteElegido).sum() >= 4 or df["ID_ALOJAMIENTO"].str.count(alojamientoElegido).sum() >= 20:
        continue
    elif check_overlap(dfReservasDeEseCliente, start_date, end_date):
        continue
    elif check_overlap(dfReservasDeEseAlojamiento, start_date, end_date):
        continue
    else:
        # Si cumple todas las condiciones, agregar la reserva
        d = {'ID_ALQUILER': "", 'ID_ALOJAMIENTO': alojamientoElegido, 'ID_CLIENTE': clienteElegido, 'INICIO': start_date, 'FIN': end_date}
        df = pd.concat([df, pd.DataFrame(d, index=[0])], ignore_index=True)
        reservas += 1

# Exportar las reservas generadas a un archivo Excel
df.to_excel("Hoja de Alquileres.xlsx", encoding="utf-8", index=False)
