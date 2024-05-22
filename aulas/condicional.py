MAIOR_IDADE = 18

idade = int(input('informe sua idade:'))

if idade >= MAIOR_IDADE:
    print('Você é maior de idade, pode ter CNH')
elif idade == 17:
    print('Você tem 17 anos, pode tirar a PPD')
else:
    print('Você é menor de idade, não pode ter CNH')
