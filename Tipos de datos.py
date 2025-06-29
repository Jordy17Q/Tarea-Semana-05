# Programa para calcular el área de un rectángulo dado su ancho y alto.

def calcular_area_rectangulo(ancho: float, alto: float) -> float:
    """Devuelve el área de un rectángulo."""
    area = ancho * alto  # Cálculo del área
    return area

# Solicitar datos al usuario
nombre_usuario: str = input("Ingresa tu nombre: ")
ancho_ingresado: float = float(input("Ingresa el ancho del rectángulo (en metros): "))
alto_ingresado: float = float(input("Ingresa el alto del rectángulo (en metros): "))

# Validar si los valores son positivos (usando booleano)
valores_validos: bool = ancho_ingresado > 0 and alto_ingresado > 0

if valores_validos:
    area_resultado: float = calcular_area_rectangulo(ancho_ingresado, alto_ingresado)
    print(f"{nombre_usuario}, el área del rectángulo es: {area_resultado} m²")
else:
    print("Error: Las dimensiones deben ser mayores que cero.")