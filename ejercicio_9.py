class CalculadoraMedias:
    def calcular_media_aritmetica(self, num1, num2, num3):
        """
        Calcula la media aritmética de tres números dados.

        Args:
        num1 (float): Primer número.
        num2 (float): Segundo número.
        num3 (float): Tercer número.

        Returns:
        float: Media aritmética de los tres números.
        """
        # Suma los tres números y luego los divide entre 3 para obtener la media aritmética
        return (num1 + num2 + num3) / 3

    def calcular_media_ponderada(self, nums, pesos):
        """
        Calcula la media ponderada dadas las listas de números y pesos.

        Args:
        nums (list of float): Lista de números.
        pesos (list of float): Lista de pesos correspondientes a los números.

        Returns:
        float: Media ponderada de los números dados con los pesos dados.
        """
        # Verifica que las listas de números y pesos tengan la misma longitud
        if len(nums) != len(pesos):
            raise ValueError("Las listas de números y pesos deben tener la misma longitud")
        
        # Calcula la suma de los productos de cada número por su peso correspondiente
        suma_productos = sum(num * peso for num, peso in zip(nums, pesos))
        
        # Calcula la suma total de los pesos
        suma_pesos = sum(pesos)
        
        # Retorna el resultado de dividir la suma de productos entre la suma de pesos
        return suma_productos / suma_pesos

# Ejemplo:
calculadora_medias = CalculadoraMedias()

# Calcular media aritmética
num1 = 10
num2 = 20
num3 = 30
media_aritmetica = calculadora_medias.calcular_media_aritmetica(num1, num2, num3)
print("Media aritmética:", media_aritmetica)

# Calcular media ponderada
nums = [10, 20, 30]
pesos = [1, 2, 3]
media_ponderada = calculadora_medias.calcular_media_ponderada(nums, pesos)
print("Media ponderada:", media_ponderada)
