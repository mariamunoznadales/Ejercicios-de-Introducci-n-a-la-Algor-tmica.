# Ejercicios de Introducción a la Algorítmica
## Ejercicio 8
Este código proporciona funciones para cálculos financieros básicos, implementado en la clase CalculadoraFinanciera.
**Funcionalidades:**
Calcular Precio con Impuestos Incluidos (TII):

*Método:* calcular_precio_con_impuestos(precio_sin_impuestos, porcentaje_iva)

*Descripción:* Calcula el precio con todos los impuestos incluidos (TII) dado el precio sin impuestos y el porcentaje de IVA.

Calcular Intereses Generados:

*Método:* calcular_intereses(capital, interes_anual, tiempo_meses)

*Descripción:* Calcula el importe de los intereses generados por un capital invertido durante un período de tiempo en meses.

## Ejercicio 9
Este código proporciona funciones para calcular la media aritmética y la media ponderada de una lista de números.
**Funcionalidades:**

Calcular Media Aritmética:

*Método:* calcular_media_aritmetica(num1, num2, num3)

*Descripción:* Calcula la media aritmética de tres números dados.

Calcular Media Ponderada:

*Método:* calcular_media_ponderada(nums, pesos)

*Descripción:* Calcula la media ponderada dadas las listas de números y pesos correspondientes.

## Ejercicio 10
Este código proporciona una función para calcular el área de un triángulo dado un lado y la altura relativa a ese lado.
**Funcionalidades:**

Calcular Área de un Triángulo:

*Método:* calcular_area_triangulo(lado, altura)

*Descripción:* Calcula el área de un triángulo dado la longitud de un lado y la altura relativa a ese lado.

## Ejercicio 11
Este código proporciona una función para calcular el importe de las horas extra que se deben pagar a un empleado.
**Funcionalidades:**

Calcular Horas Extra:

*Método:* calcular_horas_extra(salario_mensual_bruto, horas_extra)

*Descripción:* Calcula el importe de las horas extra que hay que pagar, dado el salario mensual bruto del empleado y la cantidad de horas extra trabajadas en el mes.

## Ejercicio 12
Este código proporciona dos clases relacionadas con cuentas bancarias: Cuenta y CuentaConDescubierto.

***Clase Cuenta***
La clase Cuenta representa una cuenta de depósito estándar en un banco.
*Inicialización:* Se inicializa con un saldo inicial.
*Métodos:*
depositar(cantidad): Permite depositar una cantidad en la cuenta.
retirar(cantidad): Permite retirar una cantidad de la cuenta, siempre y cuando no resulte en un saldo negativo. Devuelve True si la retirada fue exitosa, False en caso contrario.
obtener_saldo(): Obtiene el saldo actual de la cuenta.

***Clase CuentaConDescubierto***
La clase CuentaConDescubierto hereda de Cuenta y representa una cuenta de depósito con descubierto autorizado.
*Inicialización:* Se inicializa con un saldo inicial y un descubierto autorizado adicional.
*Métodos:*
retirar(cantidad): Permite retirar una cantidad de la cuenta, considerando el descubierto autorizado si es necesario. Devuelve True si la retirada fue exitosa, False en caso contrario.
