from random import randint

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
    cnpj_user = randint(100000000000, 999999999999)
    cnpj = str(cnpj_user)

    if cnpj == None:
        continue
    else:
        resultado = verificando_digitos(cnpj)
    
    digitos = fazendo_os_digitos(cnpj,resultado)
    
    cnpj += digitos

    print(f'O CNPJ gerado foi {cnpj}')
    break