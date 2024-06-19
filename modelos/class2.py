# class
class Loja:
# a lista 
    lojas = []

# função para listra chave e valor 
    def __init__(self,nome , categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = True
        Loja.lojas.append(self)

# função para retorna os valores 
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._ativo} '
    
# função para imprimir na tela     
    @classmethod
    def lista_lojas(cls):
        print(f"{'Nome: '.ljust(15)} | {'categoria: '.ljust(15)} | {'Status: '.ljust(15)}")
        for loja in cls.lojas:
            print(f'{loja._nome.ljust(15)} | {loja._categoria.ljust(15)} | {loja._ativo.ljust(15)}')

# função para altera o ativo
    def alterar_status(self):
        self._ativo = not self._ativo

# Para retorna o ativo personalizado 
    @property
    def ativo(self):
        return '''(👍 ͡❛ ͜ʖ ͡❛)👍''' if self._ativo else '''( ͡❛ ͜ʖ ͡❛)👎'''
    
# função para istância         
def nome(): 
    nome = input('Digite o nome: ')
    return nome
def categoria():
    categoria = input('Digite a categoria: ')
    return categoria

# instânciando o objeto 
loja = Loja(nome(),categoria())
# imprimindo na tela 
Loja.lista_lojas()