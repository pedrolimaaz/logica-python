Cadastro = {'Nome':[], 'Sexo':[], 'Ano':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para sim ou N para não.')
        continue

    nome = input('Qual o nome?')
    sexo = input('Qual o sexo?')
    ano = input('Qual o ano de nascimento?')
    Cadastro['Nome'].append(nome)
    Cadastro['Sexo'].append(sexo.upper())
    Cadastro['Ano'].append(ano)

print(Cadastro)

# Não Finalizado