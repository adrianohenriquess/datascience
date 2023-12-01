import pandas as pd
url = 'https://raw.githubusercontent.com/alura-cursos/pandas/main/superstore_data.csv'
dados_mercado = pd.read_csv(url)

print(dados_mercado.head())

url_2 = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data_ponto_virgula.csv'
dados_ponto_virgula = pd.read_csv(url_2, sep=';')
print(dados_ponto_virgula.head())

dados_primeiras_linhas = pd.read_csv(url, nrows=10)
print(dados_primeiras_linhas)

#dados_selecao = pd.read_csv(url, usecols=['Id', 'Year_Birth', 'Income'])
#print(dados_selecao)

#usando a posição das colunas
dados_selecao = pd.read_csv(url, usecols=[0, 1, 4])
print(dados_selecao)

dados_selecao.to_csv('clientes_mercado.csv', index=False)

clientes_mercado = pd.read_csv('clientes_mercado.csv')
print(clientes_mercado.head())