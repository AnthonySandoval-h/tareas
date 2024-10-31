def calcular_promedio(notas):
    """Calcula el promedio de una lista de notas"""
    notas_numericas = [float(nota) for nota in notas]
    return sum(notas_numericas) / len(notas_numericas)

def procesar_datos(entrada):
    """Procesa la cadena de entrada y devuelve un diccionario con los promedios"""
    # Separar los estudiantes (divididos por |)
    estudiantes = entrada.split('|')
    
    # Diccionario para almacenar los promedios
    promedios = {}
    
    # Procesar cada estudiante
    for estudiante in estudiantes:
        # Separar nombre y notas
        datos = estudiante.split(',')
        nombre = datos[0]
        notas = datos[1:]  # Todo después del nombre son notas
        
        # Calcular y guardar el promedio
        promedio = calcular_promedio(notas)
        promedios[nombre] = round(promedio, 2)
    
    return promedios

def guardar_promedios(promedios, nombre_archivo='promedios.txt'):
    """Guarda los promedios en un archivo de texto"""
    with open(nombre_archivo, 'w') as archivo:
        for nombre, promedio in promedios.items():
            archivo.write(f"{nombre}={promedio}\n")

def main():
    # Entrada de ejemplo
    entrada = "Juan,98,87,89,90|Jose,90,43,20,40|Pedro,70,80,89,90"
    
    # Procesar los datos
    promedios = procesar_datos(entrada)
    
    # Guardar en archivo
    guardar_promedios(promedios)
    
    # Mostrar mensaje de confirmación
    print("Los promedios han sido guardados en el archivo 'promedios.txt'")
    
    # Mostrar los promedios en consola
    print("\nPromedios calculados:")
    for nombre, promedio in promedios.items():
        print(f"{nombre}={promedio}")

if __name__ == "__main__":
    main()
