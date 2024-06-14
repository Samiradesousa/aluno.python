class Motocicleta:
    motos = []
    def __init__(self, modelo, cor, ano):
        self._modelo = modelo
        self._cor = cor
        self._ano = ano
        self._ativo = True
        Motocicleta.motos.append(self)

    def __str__(self):
        return f'{self._modelo} | {self._cor} | {self._ano} '
    
    @classmethod
    def lista_motos(cls):
        print(f"{'Modelo: '.ljust(15)} | {'Cor: '.ljust(15)} | {'Ano: '.ljust(15)} | {'Status: '.ljust(15)}")
        for moto in Motocicleta.motos:
            print(f'{moto._modelo.ljust(15)} | {moto._cor.ljust(15)} | {moto._ano.ljust(15)} | {moto.ativo.ljust(15)}')
    
    def alterar_status(self):
        self._ativo = not self._ativo

    @property 
    def ativo(self):
        return '''(👍 ͡❛ ͜ʖ ͡❛)👍''' if self._ativo else '''( ͡❛ ͜ʖ ͡❛)👎'''
        
def modelo(): 
    modelo = input('Qual o modelo da moto: ')
    return modelo
def cor():
    cor = input('Qual a cor da moto: ')
    return cor
def ano():
    ano = input('Qual é o ano da moto: ')
    return ano


motos = Motocicleta(modelo(), cor(), ano())
Motocicleta.lista_motos()
