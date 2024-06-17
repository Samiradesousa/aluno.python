from modelos.jogos import Jogo

Jogo_zelda = Jogo('Lol', 'Rpg')
jogo_sonic = Jogo('Sonic', 'Plataforma')

def main():
    Jogo.listar_jogos()

if __name__ == '__main__':
    main()