class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo
    
    def verificar_saldo(self):
        if self.__saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
    
    def mensagem_personalizada(self):
        return f"Plano: {self.__nome}, Saldo: {self.__saldo}"

class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.__nome = nome
        self.__plano = plano
    
    def verificar_saldo_plano(self):
        return self.__plano.verificar_saldo()
    
    def mensagem_plano(self):
        return self.__plano.mensagem_personalizada()

# Solicitação dos dados de entrada
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criação do objeto PlanoTelefone
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)

# Criação do objeto UsuarioTelefone
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Verificando e exibindo o saldo do plano
print(usuario.verificar_saldo_plano())
