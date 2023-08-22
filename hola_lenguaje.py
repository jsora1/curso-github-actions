import os

def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} desde GitHub!")

    lenguaje = os.getenv("LENGUAJE")
    print(f"¡Lenguaje, {lenguaje} desde GitHub!")

if __name__ == "__main__":
    main()