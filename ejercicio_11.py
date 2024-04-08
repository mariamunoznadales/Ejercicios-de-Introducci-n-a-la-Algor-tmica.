class CalculadoraNomina:
    def calcular_horas_extra(self, salario_mensual_bruto, horas_extra):
        """
        Calcula el importe de las horas extra que hay que pagar.

        Args:
        salario_mensual_bruto (float): Salario mensual bruto del empleado.
        horas_extra (int): Cantidad de horas extra trabajadas en el mes.

        Returns:
        float: Importe de las horas extra que hay que pagar.
        """
        # Calcular la tarifa por hora normal
        tarifa_hora_normal = salario_mensual_bruto / (52 * 35 / 12)

        # Inicializar el importe total de las horas extra
        importe_horas_extra = 0

        # Calcular el importe de las horas extra según las normas administrativas
        if horas_extra <= 7:
            importe_horas_extra = tarifa_hora_normal * 1.25 * horas_extra
        elif 8 <= horas_extra <= 43:
            importe_horas_extra = (tarifa_hora_normal * 1.25 * 7) + (tarifa_hora_normal * 1.5 * (horas_extra - 7))
        else:
            importe_horas_extra = (tarifa_hora_normal * 1.25 * 7) + (tarifa_hora_normal * 1.5 * 36) + (tarifa_hora_normal * 1.5 * 1.5 * (horas_extra - 43))

        return importe_horas_extra

# Ejemplo:
calculadora_nomina = CalculadoraNomina()

# Salario mensual bruto
salario_mensual_bruto = 3000

# Cantidad de horas extra trabajadas en el mes
horas_extra = 50

# Calcular el importe de las horas extra que hay que pagar
importe_horas_extra = calculadora_nomina.calcular_horas_extra(salario_mensual_bruto, horas_extra)
print("Importe de las horas extra que hay que pagar:", importe_horas_extra)
