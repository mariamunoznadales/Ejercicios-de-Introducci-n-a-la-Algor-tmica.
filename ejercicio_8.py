class CalculadoraFinanciera:
    def calcular_precio_con_impuestos(self, precio_sin_impuestos, porcentaje_iva):
        """
        Calcula el precio con todos los impuestos incluidos (TII).

        Args:
        precio_sin_impuestos (float): Precio sin impuestos.
        porcentaje_iva (float): Porcentaje de IVA.

        Returns:
        float: Precio con todos los impuestos incluidos (TII).
        """
        impuestos = precio_sin_impuestos * (porcentaje_iva / 100)
        precio_con_impuestos = precio_sin_impuestos + impuestos
        return precio_con_impuestos

    def calcular_intereses(self, capital, interes_anual, tiempo_meses):
        """
        Calcula el importe de los intereses generados por un capital invertido.

        Args:
        capital (float): Capital invertido.
        interes_anual (float): Interés anual expresado en porcentaje.
        tiempo_meses (int): Tiempo en meses.

        Returns:
        float: Importe de los intereses generados.
        """
        interes_mensual = interes_anual / 12 / 100  # Convertir interés anual a mensual
        intereses_generados = capital * interes_mensual * tiempo_meses
        return intereses_generados

# Ejemplo:
calculadora = CalculadoraFinanciera()

# Calcular precio con impuestos
precio_sin_impuestos = 100
porcentaje_iva = 16  # Porcentaje de IVA del 16%
precio_con_impuestos = calculadora.calcular_precio_con_impuestos(precio_sin_impuestos, porcentaje_iva)
print("Precio con impuestos incluidos:", precio_con_impuestos)

# Calcular intereses generados
capital_invertido = 1000
interes_anual = 5  # Interés anual del 5%
tiempo_meses = 12
intereses_generados = calculadora.calcular_intereses(capital_invertido, interes_anual, tiempo_meses)
print("Intereses generados:", intereses_generados)
