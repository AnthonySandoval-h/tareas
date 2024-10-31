# separar_fecha.py
def main():
    fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
    
    # Dividir la fecha usando split
    dia, mes, anio = fecha.split('/')
    
    print(f"Día: {dia}")
    print(f"Mes: {mes}")
    print(f"Año: {anio}")

if __name__ == "__main__":
    main()