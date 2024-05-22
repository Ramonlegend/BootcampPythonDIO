class Bicicleta:
  def __init__(self, cor, modelo, ano, valor):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor
  
  def buzinar(self):
    print('BIBI')
  def parar(self):
    print('Freando a bicicleta')
    print('Bicicleta parada')
  def correr(self):
    print('Pedalando a bicicleta')

b1 = Bicicleta('azul', 'caloi', 2020, 500)
b1.buzinar()
b1.parar()
b1.correr()

b2 = Bicicleta('vermelha', 'monark', 2021, 700)
b2.buzinar()