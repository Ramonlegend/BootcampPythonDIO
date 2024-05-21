import re

def validate_numero_telefone(phone_number):

  # Expressão regular para validar o formato do número de telefone
  regex = r"^\((\d{2})\) 9\d{4}-\d{4}$"

  # Valida o número de telefone usando a expressão regular
  if re.search(regex, phone_number):
    return "Número de telefone válido!"
  else:
    return "Número de telefone inválido. Formato esperado: (XX) 9XXXX-XXXX."

# Solicita o número de telefone ao usuário
phone_number = input()

# Chama a função validate_numero_telefone para verificar o número
result = validate_numero_telefone(phone_number)

# Exibe o resultado da validação
print(result)
