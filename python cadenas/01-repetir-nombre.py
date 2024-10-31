# repetir_nombre.py
def main():
    nombre = input("Introduce tu nombre: ")
    numero = int(input("Introduce un número: "))
    
    for _ in range(numero):
        print(nombre)

if __name__ == "__main__":
    main()