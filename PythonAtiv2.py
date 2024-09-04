# nota1 = int(input('Digite a primeira nota: '))
# nota2 = int(input('Digite a segunda nota: '))
# nota3 = int(input('Digite a terceira nota: '))

# media = (nota1 + nota2 + nota3) / 3

# print(media)

# base = int(input('Digite a base do retângulo: '))
# altura = int(input('Digite a altura do retângulo: '))

# area = base * altura

# print(f'\nA área do terreno é {area}')

while True:
    nome = input('Digite seu nome: ')
    sobrenome = input('Digite seu sobrenome: ')

    if nome != sobrenome:
        print('Não repetido')

    elif nome == sobrenome:
        print('Repetido')