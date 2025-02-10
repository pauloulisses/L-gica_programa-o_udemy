
print("------------- Programa que soma valores v1.0 -------------\n")

numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))

soma = numero1 + numero2

print(f"A soma de {numero1} e {numero2} é: {soma}")

import math

print("------------ Programa que calcula a área de um círculo ---------------\n")

raio = float(input("Digite o valor do raio do círculo: "))

area = math.pi * (raio ** 2)  # Usa math.pi para maior precisão

print(f"A área de um círculo com {raio:.2f} cm de raio é {area:.2f} cm²")
