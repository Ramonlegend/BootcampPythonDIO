class Cachorro:
  def __init__(self, nome, cor, acordado=True):
    print('Construindo um cachorro')
    self.nome = nome
    self.cor = cor
    self.acordado = acordado
  
  def __del__(self):
    print('Destruindo um cachorro')

  def falar(self):
    print('Au au!')

def criar_cachorro():
  c = Cachorro('Rex', 'Marrom', False)
  c.falar()

criar_cachorro()
