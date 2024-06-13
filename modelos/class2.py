class Loja:
    lojas = []
    def __init__(self,nome , categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = True
        Loja.lojas.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._ativo} '
    
    @classmethod
    def lista_lojas(cls):
        print(f"{'Nome: '.ljust(15)} | {'categoria: '.ljust(15)} | {'Status: '.ljust(15)}")
        for loja in Loja.lojas:
            print(f'{loja._nome.ljust(15)} | {loja._categoria.ljust(15)} | {loja._ativo.ljust(15)}')

    def alterar_status(self):
        self._ativo = not self._ativo

    property 
    def ativo(self):
        return '''(👍 ͡❛ ͜ʖ ͡❛)👍''' if self._ativo else '''( ͡❛ ͜ʖ ͡❛)👎'''
        
def nome(): 
    nome = input('Digite o nome: ')
    return nome
def categoria():
    categoria = input('Digite a categoria: ')
    return categoria

loja = Loja(nome(),categoria())
Loja.lista_lojas()