'''
Crie a classe ControleRemoto, onde vamos simular o funcionamento
de um controle simples (Canal, volume e liga/desliga)
'''
from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_max = 5
    vol_max = 10

    def __init__(self, canal=1, vol=2):
        self.ligada = False
        self.canal = canal
        self.vol = vol

    def start(self):
        while True:
            self.display()
            acao = str(input())
            if acao == "@":
                self.liga_desliga()
            elif self.ligada:
                if acao == "+":
                    self.volume(acao)
                elif acao == "-":
                    self.volume(acao)
                elif acao == ">":
                    self.canais(acao)
                elif acao == "<":
                    self.canais(acao)
                elif acao == "0":
                    break
            elif acao == "0":
                break

    def display(self):
        if self.ligada:
            conteudo = f"CANAL   = "
            for canal in range(1,self.canal_max+1):
                if self.canal == canal:
                    conteudo += f"[white on yellow] {canal} [/]"
                else:
                    conteudo += f" {canal} "

            conteudo += f"\nVOLUME  = "
            for volume in range(1,self.vol_max+1):
                if volume <= self.vol:
                    conteudo += f"[on green] [/]"
                else:
                    conteudo += f"[on white] [/]"

        else:
            conteudo = f":no_entry: [red]A TV está desligada[/]"

        print("\n"*10)

        tela = Panel(conteudo, title="[ TV ]", width=31)
        print(tela, f"< CH{self.canal} >   - VOL{self.vol} +")

    def liga_desliga(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def volume(self, acao):
        if acao == "+":
            if self.vol < self.vol_max+1:
                self.vol += 1
        elif acao == "-":
            if self.vol > 1:
                self.vol -= 1

    def canais(self, acao):
        if acao == ">":
            if self.canal < self.canal_max:
                self.canal += 1
            else:
                self.canal = 1
        elif acao == "<":
            if self.canal > 1:
                self.canal -= 1
            else:
                self.canal = self.canal_max

c1 = ControleRemoto(3,5)
c1.start()