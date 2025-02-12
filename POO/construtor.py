# Definição da classe Smartphone
class Smartphone:
    # Método construtor que inicializa os atributos da classe
    def __init__(self, marca, modelo, cor):
        self.marca = marca  # Armazena a marca do smartphone
        self.modelo = modelo  # Armazena o modelo do smartphone
        self.cor = cor  # Armazena a cor do smartphone

    # Método para simular uma chamada
    def ligar(self):
        print('Fazendo chamada...')  # Exibe a mensagem de chamada

# Exibe o título do programa
print('-------------Programa de classes aula 2---------------------\n')

# Solicita ao usuário que informe a marca do smartphone
marca = input('Digite a marca: ')
# Solicita ao usuário que informe o modelo do smartphone
modelo = input('Digite o modelo: ')
# Solicita ao usuário que informe a cor do smartphone
cor = input('Digite a cor: ')
# Exibe uma linha separadora
print('------------------------------------------')

# Criação de um objeto da classe Smartphone com os dados fornecidos pelo usuário
celular1 = Smartphone(marca, modelo, cor)  

# Exibe os atributos do objeto criado
print(f'Marca: {celular1.marca}')
print(f'Modelo: {celular1.modelo}')
print(f'Cor: {celular1.cor}')

# Exibe uma linha separadora
print('---------------------------')

# Chama o método ligar do objeto celular1
celular1.ligar()

