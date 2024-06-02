def minha_cenoura ():
    yield 'cenoura virus'

for i in minha_cenoura():
    print(i)

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador([1, 2, 3, 4, 5]):
    print(i)
    