# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 15:47:36 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

# Declaramos la variable numero
numero = 150

# Estructura de repetición (while) para imprimir todos los números entre 1 y 450 (450 para estar seguros)
while (numero >= 150 and numero <= 450):
    numero = numero + 1

    # Separamos los dígitos de cada número
    separa1 = (numero // 100) % 10  # Extraemos el primer dígito
    separa2 = (numero // 10) % 10  # Extraemos el segundo dígito
    separa3 = numero % 10  # Extraemos el tercer dígito

    # Con cada dígito extraido, usamos la función potencia para elevar al cubo cada dígito
    potencia1 = pow(separa1, 3)
    potencia2 = pow(separa2, 3)
    potencia3 = pow(separa3, 3)

    # Una vez elevado al cubo, se suman todos los resultados
    suma = potencia1 + potencia2 + potencia3

    # Comparamos si al sumar los resultados, es igual al número en cuestión
    if (suma == numero):
        print(numero)
