print('----------- Programa de Divisão ----------\n')

numero = float(input('Digite um número para dividir: '))
divisor = float(input('Digite um número divisor: '))

# tentar
try:
    resultado =  numero / divisor
    print(f'O resultado da divisão é: {resultado:.1f}')

# excessão
except:
    print('Ocorreu um erro de divisão por zero')




