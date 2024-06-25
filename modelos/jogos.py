# Importando a classe Avaliacao do arquivo modelos/classnota.py
from modelos.classnota import Avaliacao

class Jogo:
    jogos = []
    
    # Método construtor
    def __init__(self, nome, categoria):  
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Jogo.jogos.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'  # Retorna o nome e a categoria do jogo
    
    @classmethod
    def listar_jogos(cls):
        print(f"{'Nome do jogo'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}")
        for jogo in cls.jogos:
            print(f'{jogo._nome.ljust(20)} | {jogo._categoria.ljust(20)} | {str(jogo.media_avaliacao).ljust(20)} | {jogo.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'  
      
    def alterar_status(self):
        self._ativo = not self._ativo  # Alterna o status do jogo entre ativo e inativo

    def recebe_nota(self, usuario, nota):
        avaliacao = Avaliacao(usuario, nota)  # Cria um objeto de Avaliacao
        self._avaliacao.append(avaliacao)     # Adiciona a avaliação à lista de avaliações

    @property   
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0  # Retorna 0 se não houver avaliações
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)  # Soma todas as notas das avaliações
        quantidade_de_notas = len(self._avaliacao)  # Conta quantas avaliações foram feitas
        media = round(soma_notas / quantidade_de_notas, 1)  # Calcula a média arredondada para uma casa decimal
        return media