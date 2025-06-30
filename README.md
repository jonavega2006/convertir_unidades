# Convertidor de Unidades de Longitud

Este proyecto es un programa en Python que permite convertir entre diferentes unidades básicas de longitud.  
El usuario puede realizar múltiples conversiones dentro de la misma ejecución del programa.

## Estructura del Proyecto

- Carpeta principal: `convertir_unidades`
- Archivo principal: `Convertidor_Unidades_Longitud.py`

## Descripción

El programa convierte entre las siguientes unidades de longitud por el momento:

```text
1: cantidad * 1000,             # Kilómetros a metros
2: cantidad,                    # Metros a metros
3: cantidad / 100,              # Centímetros a metros
4: cantidad / 1000,             # Milímetros a metros
5: cantidad / 39.3701,          # Pulgadas a metros
6: cantidad / 3.28084,          # Pies a metros
7: cantidad * 1609.34,          # Millas a metros
8: cantidad / 1.09361           # Yardas a metros
El usuario selecciona la unidad de entrada y el programa calcula automáticamente las equivalencias en las demás unidades.

Características del programa
Uso correcto de tipos de datos: int, float, str, bool

Identificadores descriptivos en formato snake_case

Menú interactivo con opciones claras

Validación de entradas

Opción para realizar múltiples conversiones en un solo uso

Documentación con comentarios explicativos

Listo para ser ejecutado en PyCharm y publicado en GitHub

Cómo ejecutar
Clona el repositorio:

bash
Copiar
Editar
git clone https://github.com/jonavega2006/convertir_unidades.git
Ingresa a la carpeta del proyecto:

bash
Copiar
Editar
cd convertir_unidades
Ejecuta el programa en PyCharm o directamente en la terminal con:

bash
Copiar
Editar
python Convertidor_Unidades_Longitud.py
Requisitos
Python 3 instalado

PyCharm (opcional, recomendado)

💻 Ejemplo de uso
text
Copiar
Editar
Convertidor de Unidades de Longitud
Seleccione la unidad de entrada:
1. Kilómetros
2. Metros
3. Centímetros
4. Milímetros
5. Pulgadas
6. Pies
7. Millas
8. Yardas

Ingrese el número de la opción: 2
Ingrese la cantidad: 1000

Resultados de la conversión para 1000:
- 1.0 kilómetros
- 1000.0 metros
- 100000.0 centímetros
- 1000000.0 milímetros
- 39370.1 pulgadas
- 3280.84 pies
- 0.6213727366498067 millas
- 1093.61 yardas

¿Desea convertir otra unidad? (s/n):
Enlace al repositorio
https://github.com/jonavega2006/convertir_unidades.git

Desarrollado por: jonavega2006
