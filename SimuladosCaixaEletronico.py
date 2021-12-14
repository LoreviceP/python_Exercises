#SIMULADOR CAIXA ELETRÔNICO

valor = int(input('Qual o valor será sacado? '))
cedula = 50
total = valor
qtdeced = 0


while True:
    if total >= cedula:
        total = total - cedula
        qtdeced = qtdeced + 1
    else:
        if qtdeced > 0:
            print(f'Você receberá o valor em {qtdeced:.0f} cédulas de R$ {cedula:.2f}. ')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        qtdeced = 0
        if total == 0:
            break