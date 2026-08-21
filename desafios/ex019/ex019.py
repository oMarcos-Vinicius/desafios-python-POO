'''
Crie a classe Livro, que vai simular a passagem de páginas de um livro,
considerando também se o usuário chegou ao fim da leitura
'''
from time import sleep
from rich import print

class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f":book:[blue] Você acabou de abrir o livro [red]'{self.titulo}[/]' que tem [green]{self.paginas} paginas[/] no total. Você agora está na [yellow]pagina {self.pagina_atual}[/]")

    def __str__(self):
        print(f":book: Você acabou de abrir o livro [red]'{self.titulo}[/]' que tem [green]{self.paginas} paginas[/] no total. Você agora está na [yellow]pagina {self.pagina_atual}[/]")

    def avancar_paginas(self, quantidade):
        contador = 0
        for pagina in range(0,quantidade,1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :fast_forward: ", end=" ")
                sleep(0.3)
                contador += 1
        print(f"[blue]Você avançou {contador} páginas e agora está na [yellow]página {self.pagina_atual}[/]")

        if self.fim_do_livro():
            print(f":red_square: [red]Você chegou ao final do livro '{self.titulo}'[/]")

    def fim_do_livro(self):
        if self.pagina_atual == self.paginas:
            return True
        else:
            return False

l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(20)
l1.avancar_paginas(20)