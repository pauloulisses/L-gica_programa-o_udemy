# função recursiva - É uma função que recorre a ela mesmo
# ela chama ela mesmo


print('-----PROGRAMA QUE CALCULA O FATORIAL------\n')


def fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * fatorial(numero -1)
    
num = int(input('Digite um número:'))

print(f'O resultado do fatorial é: {fatorial(num)}')

