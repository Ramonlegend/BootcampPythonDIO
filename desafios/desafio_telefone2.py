class UsuarioTelefone:
    def __init__(self, nome, telefone, plano):
        self.__nome = nome
        self.__telefone = telefone
        self.__plano = plano
    
    def __str__(self):
        return f'Usuário {self.__nome} criado com sucesso.'

# Solicitação dos dados de entrada
nome = input()
numero = input()
plano = input()

# Criação do objeto UsuarioTelefone
usuario = UsuarioTelefone(nome, numero, plano)

# Exibindo a mensagem de saída
print(usuario)
