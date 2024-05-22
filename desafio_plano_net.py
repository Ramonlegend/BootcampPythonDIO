def recomendar_plano(consumo_medio):

  if consumo_medio <= 10:
    plano_ideal = "Plano Essencial Fibra - 50Mbps"
  elif consumo_medio <= 20:
    plano_ideal = "Plano Prata Fibra - 100Mbps"
  else:
    plano_ideal = "Plano Premium Fibra - 300Mbps"

  return plano_ideal

# Solicita o consumo médio mensal de dados ao cliente
consumo_medio = float(input("Informe seu consumo médio mensal de dados em GB: "))

# Chama a função recomendar_plano para obter o plano ideal
plano_ideal = recomendar_plano(consumo_medio)

# Exibe o plano ideal para o cliente
print(f"O plano ideal para você é o {plano_ideal}.")
