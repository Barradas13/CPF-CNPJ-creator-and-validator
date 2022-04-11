"""
04.252.011/0001-10

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0 + 16+ 6 + 10 +18+ 0 + 7 + 6 + 0 + 0 + 0 + 2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)
"""

def cnpj_criando(cnpj_user):
    if len(cnpj_user) == 14 or len(cnpj_user) == 18: 
        cnpj_user = formatando_cnpj(cnpj_user)
        return cnpj_user
    else:
        print('\nVerifique o CNPJ digitado')
        return None


def formatando_cnpj(cnpj_user):
    cnpj_retornar = ''
    for n in cnpj_user:
        if n.isnumeric():
            cnpj_retornar += str(n)
    return cnpj_retornar

def verificando_digitos(cnpj):
    cnpj_verificar = []
    resultado = 0
    for numero in cnpj:
        cnpj_verificar.append(numero)
    for indice, multiplica in enumerate(range(5,1,-1)):
        resultado += int(cnpj_verificar[indice]) * multiplica
    del cnpj_verificar[0:4]
    for indice, multiplica in enumerate(range(9,1,-1)):
        resultado += int(cnpj_verificar[indice]) * multiplica
    return resultado

def fazendo_os_digitos(cnpj,res):
    cnpj_temp = []
    for numero in cnpj:
        cnpj_temp.append(numero)
    formula_1 = 11 - (res % 11)
    if formula_1 > 9:
        digitos = 0
    else:
        digitos = formula_1
    cnpj_temp.append(str(digitos))
    res = 0
    for indice, multiplica in enumerate(range(6,1,-1)):
        res += int(cnpj_temp[indice]) * multiplica
    del cnpj_temp[0:5]
    for indice, multiplica in enumerate(range(9,1,-1)):
        valor_multiplicar = int(cnpj_temp[indice])
        res += valor_multiplicar *(multiplica)
    formula_2 = 11 - (res % 11)
    digitos = str(digitos)
    if formula_2 > 9:
        digitos += '0'
    else:
        digitos += str(formula_2)
    return digitos

while True:
    cnpj_user = input('\nDigite um CNPJ: ')
    cnpj_user_renovado = cnpj_criando(cnpj_user)
    cnpj = cnpj_user_renovado[:12]

    if cnpj.isnumeric():
        resultado = verificando_digitos(cnpj)
    else:
        print('Verifique o CNPJ digitado!')
        continue
    
    digitos = fazendo_os_digitos(cnpj,resultado)
    
    cnpj += digitos
    
    if cnpj == cnpj_user_renovado:
        print(f'Você digitou um CNPJ valido!')
    else:
        print('Você digitou um CNPJ inválido')
    if input('Deseja continuar([S]im [N]ão)? ').lower() == 'n':
        break
    else:
        continue
