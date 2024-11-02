# Importamos librerias necesarias
import pandas as pd
import os
import datetime 
import random

# Acceder a la ruta donde se encuentra los archivos
ruta = os.getcwd()

# Leemos el archivo .csv
df = pd.read_csv(ruta+r"\alojamientos.csv")
#print(df.columns)

# Columnas a borrar
columnasBorrar = ['apartment_id', 'md5', 'description', 'host_id',       
       'neighborhood_overview', 'neighbourhood_district', 'accommodates',
       'beds', 'amenities_list', 'minimum_nights',
       'maximum_nights', 'name', 'has_availability', 'availability_30',       
       'availability_60', 'availability_90', 'availability_365',      
       'number_of_reviews', 'first_review_date', 'review_scores_accuracy',
       'review_scores_cleanliness', 'review_scores_checkin',
       'review_scores_communication', 'review_scores_location',       
       'review_scores_value', 'license', 'is_instant_bookable',
       'reviews_per_month']

# Borrar columnas de la lista
for columna in columnasBorrar:
    df = df.drop(columna, axis=1)

#print(df.columns)

# Transformar los datos en "str"
df["latitude"] = df['latitude'].apply(lambda _: str(_))
df["longitude"] = df['longitude'].apply(lambda _: str(_))
df["review_scores_rating"] = df['review_scores_rating'].apply(lambda _: str(_))
df["bathrooms"] = df['bathrooms'].apply(lambda _: str(_))
df["bedrooms"] = df['bedrooms'].apply(lambda _: str(_))
df["price"] = df['price'].apply(lambda _: str(_))

# Reemplazar distintos datos
df["latitude"] = df["latitude"].apply(lambda x: x.replace(".",","))
df["longitude"] = df["longitude"].apply(lambda x: x.replace(".",","))
df["review_scores_rating"] = df["review_scores_rating"].apply(lambda x: x.replace(".",","))
df["bathrooms"] = df["bathrooms"].apply(lambda x: x.replace(".",","))
df["bedrooms"] = df["bedrooms"].apply(lambda x: x.replace(".",","))
df["price"] = df["price"].apply(lambda x: x.replace(".",","))
df["room_type"] = df["room_type"].apply(lambda x: x.replace("Entire home/apt","Casa o Departamento"))
df["room_type"] = df["room_type"].apply(lambda x: x.replace("Private room","Habitación privada"))
df["room_type"] = df["room_type"].apply(lambda x: x.replace("Shared room","Habitación compartida"))
df["room_type"] = df["room_type"].apply(lambda x: x.replace("Hotel room","Habitación de hotel"))
df["country"] = df["country"].apply(lambda x: x.replace("spain","España"))

# Que los barrios queden con su primer letra en mayuscula
df["neighbourhood_name"] = df['neighbourhood_name'].str.capitalize()
df["city"] = df['city'].str.capitalize()
#print(df["neighbourhood_name"].head(5))

# Eliminar filas segun algun criterio
df = df.drop(df.loc[df["review_scores_rating"] == "nan"].index)
df = df.drop(df.loc[df["city"] != "Valencia"].index)
print(df.head(10))

# Le damos formato de fecha a la columna "StockDate"
df['last_review_date'] = pd.to_datetime(df['last_review_date'])
df['insert_date'] = pd.to_datetime(df['insert_date'])

# Quitar la hora y dejar solo la fecha completa
df['last_review_date'] = df['last_review_date'].dt.strftime('%d-%m-%Y')
df['insert_date'] = df['-insert_date'].dt.strftime('%d-%m-%Y')
#print(df["StockDate"])

# Crear una columna de paginas de alquiler aleatorio
paginas = ["Airbnb", "Agoda", "Expedia", "Tripadvisor",
                "Kayak", "Flipkey", "Booking", "Homeaway"]

listadoDePaginas = []
alojamientos = 0
while alojamientos < 441:
    alojamientos +=1
    listadoDePaginas.append(random.choice(paginas))

df['PUBLICADO_POR'] = listadoDePaginas

# Exportamos el archivo .csv (con los datos modificados)
df.to_csv("AlojamientosEditado.csv",encoding="utf-8", index=False)
