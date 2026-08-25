'''
Crie a classe Caneta, que simule o funcionamento de uma caneta
colorida, podendo escrever frases na cor relativa.
'''
from rich import print

class Caneta:

    def __init__(self, cor="branco"):

        escolha = ""

        if cor.upper().strip() == "AZUL":
            escolha = "[blue]"
        elif (cor.upper().strip() == "VERMELHO") or (cor.upper().strip() == "VERMELHA"):
            escolha = "[red]"
        elif cor.upper().strip() == "AMARELO":
            escolha = "[yellow]"
        elif cor.upper().strip() == "PRETO":
            escolha = "[black]"
        elif cor.upper().strip() == "VERDE":
            escolha = "[green]"
        elif cor.upper().strip() == "BRANCO":
            escolha = "[white]"
        else:
            escolha = "[white]"

        self.cor = escolha
        self.tampada = True

    def destampar(self) -> bool:
        self.tampada = False

    def tampar(self) -> bool:
        self.tampada = True

    def escrever(self, txt):
        if not self.tampada:
            print(f"{self.cor}{txt}[/]", end=" ")
        else:
            print(f":no_entry: A [blue]caneta[/] está tampada!!")

    def quebrar_linha(self, linhas=1):
        print("\n" * linhas)

caneta1 = Caneta("verde")
caneta1.destampar()
caneta1.escrever("Testando a caneta verde")
caneta1.quebrar_linha(1)
caneta1.escrever("Finalizando o teste da caneta verde")
caneta1.quebrar_linha(1)

caneta2 = Caneta("vermelho")
caneta2.escrever("Testando a caneta vermelho")
caneta2.quebrar_linha(1)
caneta2.destampar()
caneta2.escrever("Finalizando o teste da caneta vermelho")
caneta2.quebrar_linha(1)

caneta3 = Caneta("AZul  ")
caneta3.destampar()
caneta3.escrever("Testando a caneta azul")
caneta3.quebrar_linha(1)
caneta3.escrever("Testando se a escrita será na mesma linha.")
caneta3.escrever("Finalizando o teste da caneta azul")
