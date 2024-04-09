from data_reader import leer_datos, filtrar_calcular_media

def main():
    # Ruta del archivo
    ruta_archivo = 'C:\\Users\\Daniel.LAPTOP-6MDMV2S4\\Desktop\\examen_evaluacion3\\data\\datos_examen.csv'

    # Nombre del alumno
    nombre_alumno = 'Daniel'  # Modifiqué el nombre para que coincida con el formato que estás utilizando en la función filtrar_por_nombre_alumno_y_calcular_promedio()

    # Convertir la columna 'TS' a datetime
    df = leer_datos(ruta_archivo)

    # Filtrar los datos y calcular la media para el alumno especificado
    df_filtrado = filtrar_calcular_media(df, nombre_alumno)

    # Se imprime la media solo si se desea
    # print("La media de 'Value' para el alumno", nombre_alumno, "es:", media)

if __name__ == "__main__":
    main()

