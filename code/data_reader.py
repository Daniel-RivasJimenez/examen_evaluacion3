import pandas as pd

def leer_datos(ruta_archivo: str) -> pd.DataFrame:
    """
    Lee un archivo CSV y devuelve un DataFrame con la columna 'TS' convertida a datetime.

    Parameters:
    ruta_archivo (str): La ruta del archivo CSV a leer.

    Returns:
    pd.DataFrame: El DataFrame creado a partir del archivo CSV con la columna 'TS' convertida a datetime.
    """
    df = pd.read_csv(ruta_archivo)
    df['TS'] = pd.to_datetime(df['TS'])
    return df

def filtrar_calcular_media(df: pd.DataFrame, nombre_alumno: str) -> pd.DataFrame:
    """
    Filtra los datos por el nombre del alumno en el formato 'Examen_NOMBRE_ALUMNO' y calcula el promedio de la columna 'Value'.

    Parameters:
    df (pd.DataFrame): El DataFrame que se va a filtrar y calcular el promedio.
    nombre_alumno (str): El nombre del alumno que se utilizará para filtrar los datos.

    Returns:
    pd.DataFrame: El DataFrame filtrado por el nombre del alumno.
    """
    df_filtrado = df[df['Tag'] == 'Examen_' + nombre_alumno]
    promedio_value = df_filtrado['Value'].mean()
    print(f"El promedio de 'Value' para el alumno {nombre_alumno} es: {promedio_value}")
    return df_filtrado

