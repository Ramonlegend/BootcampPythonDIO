def gerenciar_equipamentos():

  # Inicializa a lista vazia para armazenar os itens
  itens = []

  # Loop para solicitar ao usuário a entrada de até 3 itens
  for i in range(3):
    item = input("Insira o nome do item {}: ".format(i + 1))
    itens.append(item)

  # Exibe a lista de itens com marcação
  print("Lista de Equipamentos:")
  for item in itens:
    print(f"- {item}")

# Chama a função gerenciar_equipamentos para executar o programa
gerenciar_equipamentos()
