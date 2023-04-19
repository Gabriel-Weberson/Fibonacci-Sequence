valorDeVizualizacao = 0
primeiroValor = 0
segundoValor = 1
verificador = False

valorInformado = int(input('Informe um valor para verificar se faz parte da sequencia de Fibonacci: '))

print(f'{primeiroValor} -> {segundoValor}', end=' ')
while (valorDeVizualizacao <= valorInformado):
    valorDeVizualizacao = primeiroValor + segundoValor
    primeiroValor = segundoValor
    segundoValor = valorDeVizualizacao
    print(f'-> {valorDeVizualizacao}', end=' ')
    if (valorDeVizualizacao == valorInformado):
        verificador = True
if (verificador == True):
    print(f'\n{valorInformado} faz parte da sequencia de Fibonacci.')
else:
    print(f'\n{valorInformado} não faz parte da sequencia de Fibonacci.')
