class Estudante:
  escola = "DIO"
  def __init__(self, nome, matricula):
    self.nome = nome
    self.matricula = matricula

  def __str__ (self) -> str:
    return f"{self.nome} - {self.matricula} - {self.escola}"
  
def mostrar_dados(*estudantes):
  for estudante in estudantes:
    print(estudante)

aluno1 = Estudante("João", 123)
aluno2 = Estudante("Maria", 456)
mostrar_dados(aluno1, aluno2)

aluno1.matricula = 789
mostrar_dados(aluno1, aluno2)