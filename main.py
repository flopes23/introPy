# - imports

# - classe

# - metodos e funcoes


def print_hi(name):
    print(f'Hi, {name}')
    print(f'Concatenar ' + name)  # concat anterior v3


def calcular_area_retamgulo(largura, comprimento):
    return largura * comprimento


def calcular_area_quadrado(lado):
    return lado * lado


def calcular_area_triangulo(largura, comprimento):
    return largura * comprimento / 2


def contagem_progressiva(fim):
    for numero in range (fim):
        print(numero)


def apoiar_candidato(nome,vezes):
    for numero in range (vezes):

        if numero < 9:
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1, '-', nome)


def brinca_de_plim(fim):
    for numero in range (fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero+1))


if __name__ == '__main__':
    print_hi('PyCharm')

    resultado = calcular_area_retamgulo(5, 2)
    print(f'Area do retangulo é de {resultado} m²')

    resultado = calcular_area_quadrado(5)
    print(f'Area do quadrado é de {resultado} m²')

    resultado = calcular_area_triangulo(5, 2)
    print(f'Area do triangulo é de {resultado} m²')

    contagem_progressiva(10)

    apoiar_candidato('Fabio',10)

    brinca_de_plim(25)