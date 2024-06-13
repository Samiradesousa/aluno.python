class Cliente:
    clientes = []
    def __init__(self, nome, idade, email, telefone):
        self._nome = nome.title()
        self._idade = idade
        self._email = email
        self._telefone = telefone
        self._ativo = True
        Cliente.clientes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._idade} | {self._email} | {self._telefone}'
    
    @classmethod
    def lista_cliente(cls):
        print(f"{'Nome: '.ljust(15)} | {'Idade: '.ljust(15)} | {'Email: '.ljust(15)} | {'Telefone: '.ljust(15)} | {'Status: '.ljust(15)}")
        for cliente in Cliente.clientes:
            print(f'{cliente._nome.ljust(15)} | {cliente._idade.ljust(15)} | {cliente._email.ljust(15)} | {cliente._telefone.ljust(15)} | {cliente.ativo.ljust(15)}')
    
    def alterar_status(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return '''(👍 ͡❛ ͜ʖ ͡❛)👍''' if self._ativo else '''( ͡❛ ͜ʖ ͡❛)👎'''
    
def nome(): 
    nome = input('Digite o nome: ')
    return nome
def idade():
    idade = input('Digite a idade : ')
    return idade
def email():
    email = input('Digite o email: ')
    return email
def telefone(): 
    telefone = input('Digite o telefone: ')
    return telefone

cliente = Cliente(nome(), idade(), email(), telefone())
Cliente.lista_cliente()