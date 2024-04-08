class CalculadoraAreas:
    def calcular_area_triangulo(self, lado, altura):
        """
        Calcula el área de un triángulo dada la medida de un lado y la altura relativa a ese lado.

        Args:
        lado (float): Longitud del lado del triángulo.
        altura (float): Altura relativa al lado del triángulo.

        Returns:
        float: Área del triángulo.
        """
        return (lado * altura) / 2

# Ejemplo:
calculadora_areas = CalculadoraAreas()

# Calcular área de un triángulo con un lado y la altura relativa a ese lado
lado = 5
altura = 8
area_triangulo = calculadora_areas.calcular_area_triangulo(lado, altura)
print("Área del triángulo:", area_triangulo)

# ¿Se puede utilizar este algoritmo para un triángulo rectángulo si se dan las medidas de sus dos lados perpendiculares?
# Sí, sólo si se saben las medidas de sus dos lados perpendiculares,
# usando una de las fórmulas para calcular la altura en función de los lados a y b y el hipotenusa c:
# altura = (2 * área) / hipotenusa
# Área = (lado1 * lado2) / 2
