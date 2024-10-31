# nombre_formatos.py
def main():
    nombre_completo = input("Introduce tu nombre completo: ")
    
    # Versión en minúsculas
    print(nombre_completo.lower())
    # Versión en mayúsculas
    print(nombre_completo.upper())
    # Versión tipo título (primera letra de cada palabra en mayúscula)
    print(nombre_completo.title())

if __name__ == "__main__":
    main()