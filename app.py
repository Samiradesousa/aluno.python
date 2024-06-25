from modelos.jogos import Jogo 

# Criação de instâncias da classe Jogo com diferentes jogos e categorias
Jogo_zelda = Jogo('Lol', 'Rpg')  # Cria um jogo 
jogo_sonic = Jogo('Sonic', 'Plataforma')  # Cria um jogo 

jogo_sonic.alterar_status()  # Altera o status do jogo Sonic para ativo

# Recebe notas para os jogos criados
jogo_sonic.recebe_nota('Annya', 10)  
jogo_sonic.recebe_nota('Samira', 8)  
Jogo_zelda.recebe_nota('Pedro', 9)  
Jogo_zelda.recebe_nota('Sarah', 5)  

def main():
    Jogo.listar_jogos()  # Chama o método estático listar_jogos da classe Jogo para listar todos os jogos

if __name__ == '__main__':
    main()  # Executa a função main 