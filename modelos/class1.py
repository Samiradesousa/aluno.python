class Cliente:
    clientes = []  # Lista para armazenar os clientes
    
    def __init__(self, nome, idade, email, telefone):
        # Inicializa um objeto Cliente com nome, idade, email, telefone e define como ativo
        self._nome = nome.title()  # Armazena o nome do cliente em título
        self._idade = idade  # Armazena a idade do cliente
        self._email = email  # Armazena o email do cliente
        self._telefone = telefone  # Armazena o telefone do cliente
        self._ativo = True  # Define o cliente como ativo
        Cliente.clientes.append(self)  # Adiciona o cliente à lista de clientes
    
    def __str__(self):
        # Retorna uma representação em string do cliente com nome, idade, email e telefone
        return f'{self._nome} | {self._idade} | {self._email} | {self._telefone}'
    
    @classmethod
    def lista_cliente(cls):
        # Imprime uma tabela formatada com os detalhes de todos os clientes cadastrados
        print(f"{'Nome: '.ljust(15)} | {'Idade: '.ljust(15)} | {'Email: '.ljust(15)} | {'Telefone: '.ljust(15)} | {'Status: '.ljust(15)}")
        for cliente in Cliente.clientes:
            print(f'{cliente._nome.ljust(15)} | {cliente._idade.ljust(15)} | {cliente._email.ljust(15)} | {cliente._telefone.ljust(15)} | {cliente.ativo.ljust(15)}')
    
    def alterar_status(self):
        # Alterna o status do cliente entre ativo e inativo
        self._ativo = not self._ativo

    @property
    def ativo(self):
        # Retorna um emoji indicando se o cliente está ativo ou inativo
        return '(👍 ͡❛ ͜ʖ ͡❛)👍' if self._ativo else '( ͡❛ ͜ʖ ͡❛)👎'

def nome():
    # Função para capturar o nome do cliente através da entrada do usuário
    nome = input('Digite o nome: ')
    return nome

def idade():
    # Função para capturar a idade do cliente através da entrada do usuário
    idade = input('Digite a idade: ')
    return idade

def email():
    # Função para capturar o email do cliente através da entrada do usuário
    email = input('Digite o email: ')
    return email

def telefone():
    # Função para capturar o telefone do cliente através da entrada do usuário
    telefone = input('Digite o telefone: ')
    return telefone

# Cria um novo objeto Cliente com dados fornecidos pelo usuário e lista todos os clientes
cliente = Cliente(nome(), idade(), email(), telefone())
Cliente.lista_cliente()