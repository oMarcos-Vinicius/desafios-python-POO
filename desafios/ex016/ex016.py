'''
Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo.
Crie também um método que permita ao funcionário se apresentar.
'''
from rich import print
from rich import inspect

class Funcionario:
    #Atributos de Classe
    empresa = "Curso em vídeo"

    def __init__(self, nome, setor, cargo):
        #Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} no setor de {self.setor} da empresa {__class__.empresa}"


#Funcionario.empresa = "Cielo"

cargo1 = Funcionario(nome="Maria", setor="Administração", cargo="Diretora")
cargo2 = Funcionario(nome="Pedro", setor="TI", cargo="Programador")

print(cargo1.apresentacao())
print(cargo2.apresentacao())
inspect(Funcionario)
inspect(cargo1, methods=True)
inspect(cargo2, methods=True)