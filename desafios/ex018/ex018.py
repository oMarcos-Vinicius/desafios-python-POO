'''
Crie a classe Churrasco, onde seja possível informar quantas pessoas vão
participar e mostre quanto de carne deve ser comprado, o custo total
do churrasco e o preço por pessoa.
'''

from rich import print
from rich.panel import Panel

class Churrasco:
    """Classe calcula a quantia de carne e valor que deverá comprar para uma festa.
    Valores recebidos: titulo da festa e quantidade de pesssoas.
    """

    consumo_pessoa:float = 0.4
    precoKg:float = 82.4

    def __init__(self, titulo, pessoas):
        self.titulo = titulo
        self.pessoas = pessoas

    def analisar(self):
        """Método que exibirá um painel com: nome da festa, quantidados dos convidados, valor da carne,
        quantia por pessoa e o preço total/por pessoa.
        """
        quantia_comprar = self.pessoas * Churrasco.consumo_pessoa
        custo = quantia_comprar * Churrasco.precoKg
        divisao = custo / self.pessoas

        mensagem = f"Analisando [green]{self.titulo}[/] com [blue]{self.pessoas} convidados[/]\n"
        mensagem += f"Cada participante comerá {Churrasco.consumo_pessoa}Kg e cada Kg custará R${Churrasco.precoKg:.2f}\n"
        mensagem += f"Recomendo comprar [blue]{quantia_comprar:.2f}Kg[/] de carne\n"
        mensagem += f"O custo total será de [green]R${custo:.2f}[/]\n"
        mensagem += f"Cada pessoa pagará [yellow]R${divisao:.2f}[/] para participar"

        painel = Panel(mensagem, title=self.titulo, width=80)

        print(painel)

c1 = Churrasco("Churras dos amigos", 86)

c1.analisar()