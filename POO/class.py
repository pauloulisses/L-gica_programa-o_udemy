class Smartphone:
    # Características = Atributos
    marca = 'Apple'
    modelo = 'Iphone 15'
    cor = 'Branco'

    # Método = Ação que o smartphone pode fazer
    def email(self):
        print('Enviando um email... ')


print('-------Programa de Classes aula 1--------------\n')

# Criando o objeto
celular1 = Smartphone()  # celular1 é um objeto da classe Smartphone
print(f'Marca: {celular1.marca}')
print(f'Modelo: {celular1.modelo}')
print(f'Cor: {celular1.cor}')

# Chamando a ação
celular1.email()  

print('-----------------------------')

celular2 = Smartphone()
celular2.marca = input('Digite a marca: ')
celular2.modelo= input('Digite a modelo: ')
celular2.cor= input('Digite a cor: ')

print(f'Marca: {celular2.marca}')
print(f'Modelo: {celular2.modelo}')
print(f'Cor: {celular2.cor}')