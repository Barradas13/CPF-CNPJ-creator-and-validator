"""

Pegar os 9 primeiros digitos do CPF e fazer uma multiplicação do 10 ao 2 de cima paga baixo 1o numero x 10 ...
Guardar os valores dessas multiplicações e somá-los
Com o valor somado fazer a formula 11 - (valor % 11)
Se o resultado for maior do que 9 o valor é  0
Se o resultado for menor ou igual a 9 o valor é o resultado

Mesma coisa com o outro digito, porém a contagem regressiva começa por 11 e vai até 2
"""
from random import randint
numero = str(randint(100000000, 999999999))


while True:
    CPF = str(numero)

#Criando as variaveis da parte do primeiro digito

    cD1 = 0
    ListaD1 = [ ]
    ListaD1M = []
    TotalD1 = 0

#Colocando os valores do cpf em uma lista para usar índices

    for _ in CPF:
        ListaD1.append(CPF[cD1])
        cD1 += 1

#Multiplicando os valores por 10...

    for indiceD1, NMD1 in enumerate(range(10, 1, -1)):
        ListaD1M.append(int(ListaD1[indiceD1]) * NMD1)

#Somando os valores

    for nD1 in ListaD1M:
        TotalD1 += nD1

    TotalD1 = 11 - (TotalD1 % 11)

    if TotalD1 == 10:
        TotalD1 = 0

    numero += str(TotalD1)


    CPF = numero[:10]

#Criando as variaveis da parte do segundo digito
    
    cD2 = 0
    ListaD2 = [ ]
    ListaD2M = [ ]
    TotalD2 = 0

#Passando os valores do cpf para a lista

    for d2_ in CPF:
        ListaD2.append(CPF[cD2])
        cD2 += 1

#Multiplicando os valores para fazer a formula

    for indiceD2, NMD2 in enumerate(range(11, 1, -1)):
        ListaD2M.append(int(ListaD2[indiceD2]) * NMD2)

#Somando os valores 

    for nD2 in ListaD2M:
        TotalD2 += nD2

    TotalD2 = 11 - (TotalD2%11)

    if TotalD2 == 10:
        TotalD2 = 0

    numero += str(TotalD2)

    CPF = numero


#Mensagem final

    print(f'O CPF criado foi {CPF}')
    break
