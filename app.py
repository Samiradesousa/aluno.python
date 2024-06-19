from modelos.jogos import Jogo

Jogo_zelda = Jogo('Lol', 'Rpg')
jogo_sonic = Jogo('Sonic', 'Plataforma')

jogo_sonic.alterar_status()

jogo_sonic.recebe_nota('Annya', 10)
jogo_sonic.recebe_nota('Samira', 8)
Jogo_zelda.recebe_nota('Pedro',9)
Jogo_zelda.recebe_nota('Sarah', 5)

def main():
    Jogo.listar_jogos()

if __name__ == '__main__':
    main()
