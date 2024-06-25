class Motocicleta:
    motos = []  # Lista para armazenar as motocicletas
    
    def __init__(self, modelo, cor, ano):
        # Inicializa um objeto Motocicleta com modelo, cor, ano e define como ativo
        self._modelo = modelo
        self._cor = cor
        self._ano = ano
        self._ativo = True
        Motocicleta.motos.append(self)  # Adiciona a motocicleta à lista de motos
    
    def __str__(self):
        # Retorna uma representação em string da motocicleta com modelo, cor e ano
        return f'{self._modelo} | {self._cor} | {self._ano} '
    
    @classmethod
    def lista_motos(cls):
        # Imprime uma tabela formatada com os detalhes de todas as motocicletas cadastradas
        print(f"{'Modelo: '.ljust(15)} | {'Cor: '.ljust(15)} | {'Ano: '.ljust(15)} | {'Status: '.ljust(15)}")
        for moto in Motocicleta.motos:
            print(f'{moto._modelo.ljust(15)} | {moto._cor.ljust(15)} | {moto._ano.ljust(15)} | {moto.ativo.ljust(15)}')
    
    def alterar_status(self):
        # Alterna o status da motocicleta entre ativo e inativo
        self._ativo = not self._ativo

    @property 
    def ativo(self):
        # Retorna um emoji indicando se a motocicleta está ativa ou inativa
        return '(👍 ͡❛ ͜ʖ ͡❛)👍' if self._ativo else '( ͡❛ ͜ʖ ͡❛)👎'
        
def modelo(): 
    # Função para capturar o modelo da motocicleta através da entrada do usuário
    modelo = input('Qual o modelo da moto: ')
    return modelo

def cor():
    # Função para capturar a cor da motocicleta através da entrada do usuário
    cor = input('Qual a cor da moto: ')
    return cor

def ano():
    # Função para capturar o ano da motocicleta através da entrada do usuário
    ano = input('Qual é o ano da moto: ')
    return ano

# Cria uma nova motocicleta com os dados fornecidos pelo usuário e lista todas as motocicletas
motos = Motocicleta(modelo(), cor(), ano())
Motocicleta.lista_motos()
