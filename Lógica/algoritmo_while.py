# Estrutura de repetição

print('Programa de repetição\n')

# para o contador a onde ele vai até 5 escreva na tela
for contador in range(5):
    print(contador)



print('##### programa que soma números#####\n')

soma = 0
for contar in range(5):
    numero = int(input('Digite um valor'))
    soma += numero # soma = 0 + soma + numero

print(f'A soma dos valores é:{soma} ')    



# estrutura while - Enquanto

print('----- Programa que soma com while-------')

soma = 0
contant = 1
while contant < 6:
    numero = int(input('Digite um valor'))
    soma += numero
    contant += 1

print(f'A soma dos valores é:{soma}')