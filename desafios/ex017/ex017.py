'''
Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também
um método que mostre uma etiqueta de preço do produto.
'''

from rich import print
from rich.panel import Panel

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, " ")}"
        conteudo += f"{"-"*30}"
        preco_formatado = (f"R${self.preco:,.2f}").replace(".",",")
        conteudo += f"{preco_formatado.center(30, ".")}"
        etiq = Panel(conteudo, title="Produto", width=34)
        print(etiq)
    

p1 = Produto("iPhone 17 Max", 25_000.85)
p2 = Produto("Mouse", 120)

p1.etiqueta()
p2.etiqueta()