"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    # Limpiar los datos
    # Convertir todas las cadenas a minúsculas
    df = df.apply(lambda x: x.astype(str).str.lower())

    # Convertir fechas al formato correcto
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], errors='coerce')

    # Remover caracteres especiales del monto del crédito y convertirlo a numérico
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('[^0-9]', '', regex=True).astype(float)

    # Eliminar filas con datos faltantes
    df = df.dropna()

    # Eliminar valores duplicados
    df = df.drop_duplicates()

    # Guardar el DataFrame limpio como un archivo CSV
    df.to_csv('solicitudes_credito_clean.csv', index=False)

    return df

clean_data()