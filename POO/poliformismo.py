class Smartphone:
    # Método construtor que inicializa os atributos da classe
    def __init__(self, marca, modelo, cor):
        self.marca = marca  # Armazena a marca do smartphone
        self.modelo = modelo  # Armazena o modelo do smartphone
        self.cor = cor  # Armazena a cor do smartphone

    # Método para simular uma chamada
    def ligar(self):
        print('Fazendo chamada...')  # Exibe a mensagem de chamada

    def despertar(self):
         print('Despertador do celular tocando') 



# Exibe o título do programa
print('-------------Programa de classes aula 2---------------------\n')


# Classe filha Smartwatch herda a estrutura da classe Smartphone
class Smartwatch(Smartphone):
    bussola = True  # Corrigido o nome do atributo

    def status(self):
        print('Exibindo status de atividade...')  # Melhorada a mensagem


    def despertar(self):
         print('Despertador do relógio tocando')     


# Objeto relogio1 é do tipo Smartwatch
relogio1 = Smartwatch('Xiaomi', 'Mi Band 7', 'Preto')

# Exibir informações corretamente
print(f'Marca: {relogio1.marca}')
print(f'Modelo: {relogio1.modelo}')
print(f'Cor: {relogio1.cor}')
print(f'Sensor de Bússola: {relogio1.bussola}\n')

# Chamar método status
relogio1.status()
relogio1.despertar()


print('-------------------------\n')
print('Informações do celular')

celular1 = Smartphone('sansung', 'A22', 'Azul')
celular1.despertar()