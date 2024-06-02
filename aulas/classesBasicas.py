class veiculo:
  def __init__(self, cor, placa, numero_rodas):
    self.cor = cor
    self.placa = placa
    self.numero_rodas = numero_rodas
  
  def ligar_motor(self):
    print("Motor ligado")

class motocicleta(veiculo):
  pass 

class carro(veiculo):
  pass 

class caminhao(veiculo):
  def __init__(self, carregado, cor, placa, numero_rodas):
    super().__init__(cor, placa, numero_rodas)
    self.carregado = carregado
  def esta_ligado(self):
    print(f"{'sim' if self.carregado else 'não'} está carregado'")

motocicleta = motocicleta("preta", "ABC-1234", 2)
motocicleta.ligar_motor()
carro = carro("vermelho", "DEF-5678", 4)
carro.ligar_motor()
caminhao = caminhao(True, "azul", "GHI-9101", 6)
caminhao.ligar_motor()
print(motocicleta.cor, motocicleta.placa, motocicleta.numero_rodas) 