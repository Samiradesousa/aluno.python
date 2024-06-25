class Contabancaria:

# Metodo construtor com atributos
    def __init__(self, titular, saldo):

        self._titular = titular.title()
        self.saldo = saldo
        self._ativar_conta = False

# Retorna uma representação em string
    def __str__(self):
        return f'Nome: {self._titular} \nSaldo: {self.saldo} \nA conta estar: {self.ativa_conta}\n'
   
    @property
    def ativa_conta(self):
        return 'Ativa' if self._ativar_conta else 'Desativada'   
    def alterar_status(self):
        self._ativar_conta = not self._ativar_conta

# Exemplo de uso da classe Contabancaria
print('\n-------- Welcome --------\n')
titular_conta = Contabancaria('Annya', 500)
titular_conta.alterar_status()
print(titular_conta)

class Clientebanco:

# Listra para armazerna os clientes
    clientes = []

# Metodo construtor com atributos
    def __init__(self, nome, cpf, idade, email, telefone, endereco):

        self._nome = nome.title()
        self._cpf = cpf
        self._idade = idade
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        Clientebanco.clientes.append(self)

# Função para retornar os valores 
    def __str__(self):
        return f'{self._nome} | {self._cpf} | {self._idade} | {self.email} | {self.telefone} | {self.endereco}'
    
# Imprime uma tabela formatada com os detalhes de todos os clientes cadastrados
    @classmethod
    def lista_clientes(cls):
        print(f"{'Nome do cliente: '.ljust(20)} | {'CPF do cliente: '.ljust(20)} | {'Idade do cliente: '.ljust(20)} | {'E-mail do cliente: '.ljust(20)} | {'Telefone do cliente: '.ljust(20)} | {'Endereço do cliente: '.ljust(20)}")
        for cliente in cls.clientes:
            print(f'{cliente._nome.ljust(20)} | {cliente._cpf.ljust(20)} | {cliente._idade.ljust(20)} | {cliente.email.ljust(20)} | {cliente.telefone.ljust(21)} | {cliente.endereco.ljust(20)} ')

# Exemplo de uso da classe Clientebanco
cliente1 = Clientebanco('Annya', '02585697853', '18' , 'annya@gmail.com','11954875621','Rua Miguel Braga 79 - ap/101 - Boa Vista - Itajuba-MG')
Clientebanco.lista_clientes()
