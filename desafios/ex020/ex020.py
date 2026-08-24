'''
Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos
favoritos de uma pessoas. Crie também um método que permita mostrar
a ficha desse gamer.
'''

from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favoritos(self, jogo):
        self.favoritos.append(jogo)
        self.favoritos.sort()

    def ficha(self):
        conteiner_da_ficha = f"Nome Real: [black on blue]{self.nome}[/]"
        conteiner_da_ficha += f"\nJogos favoritos:"
        for jogo in self.favoritos:
            conteiner_da_ficha += f"\n:video_game: [blue]{jogo}[/]"
        ficha_gamer = Panel(conteiner_da_ficha, title=f"Jogador <{self.nick}>", width=50)
        print(ficha_gamer)

jogador1 = Gamer("Vinícius Silva", "VinilowProfile")
jogador1.add_favoritos("Zelda - Ocarina Of Time")
jogador1.add_favoritos("Assassin's Creed")
jogador1.add_favoritos("Gear of War")
jogador1.add_favoritos("Elden Ring")
jogador1.add_favoritos("Resident Evil 2 - Remake")

jogador1.ficha()