# Programa para convertir entre unidades básicas de longitud
# Unidades: kilómetros, metros, centímetros, milímetros, pulgadas, pies, millas y yardas
# El usuario selecciona la unidad de entrada y el programa realiza las conversiones
# Se utilizan tipos de datos: int, float, str, bool
# Los identificadores usan el estilo snake_case
# El código está documentado con comentarios explicativos

def mostrar_menu():
    """Muestra el menú de opciones disponibles."""
    print("\n" + "=" * 50)
    print("         Convertidor de Unidades de Longitud")
    print("=" * 50)
    print("Seleccione la unidad de entrada:")
    print("1. Kilómetros")
    print("2. Metros")
    print("3. Centímetros")
    print("4. Milímetros")
    print("5. Pulgadas")
    print("6. Pies")
    print("7. Millas")
    print("8. Yardas")
    print("=" * 50)


def convertir_longitud(opcion, cantidad):
    """Realiza las conversiones de longitud según la opción seleccionada."""

    # Diccionario de equivalencias a metros
    equivalencias_a_metros = {
        1: cantidad * 1000,             # Kilómetros a metros
        2: cantidad,                    # Metros a metros
        3: cantidad / 100,              # Centímetros a metros
        4: cantidad / 1000,             # Milímetros a metros
        5: cantidad / 39.3701,          # Pulgadas a metros
        6: cantidad / 3.28084,          # Pies a metros
        7: cantidad * 1609.34,          # Millas a metros
        8: cantidad / 1.09361           # Yardas a metros
    }

    # Calcular la cantidad en metros
    metros = equivalencias_a_metros.get(opcion, 0)

    # Realizar conversiones desde metros
    kilometros = metros / 1000
    centimetros = metros * 100
    milimetros = metros * 1000
    pulgadas = metros * 39.3701
    pies = metros * 3.28084
    millas = metros / 1609.34
    yardas = metros * 1.09361

    print("\n" + "=" * 50)
    print(f"Resultados de la conversión para {cantidad}:")
    print("=" * 50)
    print(f"- {kilometros} kilómetros")
    print(f"- {metros} metros")
    print(f"- {centimetros} centímetros")
    print(f"- {milimetros} milímetros")
    print(f"- {pulgadas} pulgadas")
    print(f"- {pies} pies")
    print(f"- {millas} millas")
    print(f"- {yardas} yardas")


def main():
    """Función principal del programa."""

    continuar = True

    while continuar:
        mostrar_menu()

        try:
            opcion = int(input("Ingrese el número de la opción: "))
            es_opcion_valida = 1 <= opcion <= 8  # bool

            if es_opcion_valida:
                cantidad = float(input("Ingrese la cantidad: "))
                es_cantidad_valida = cantidad >= 0  # bool

                if es_cantidad_valida:
                    convertir_longitud(opcion, cantidad)
                else:
                    print("Error: La cantidad debe ser un número positivo.")
            else:
                print("Error: Opción no válida. Debe seleccionar del 1 al 8.")

        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese solo números.")

        # Preguntar si desea realizar otra conversión
        respuesta = input("\n¿Desea convertir otra unidad? (s/n): ").strip().lower()
        if respuesta != 's':
            continuar = False
            print("\nGracias por usar el convertidor de unidades. ¡Hasta luego!")

# Inicia el programa
if __name__ == "__main__":
    main()
