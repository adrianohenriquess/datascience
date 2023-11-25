import pandas as pd

dados = pd.read_csv('aluguel.csv', sep=';')

print(dados.head(10))

#trazendo o final da tabela
print(dados.tail())

print(type(dados))

print(dados.shape)
print(dados.columns)

print(dados.info())

#vizualizando os tipos de dados
print(dados['Tipo'])
print(dados[['Quartos', 'Valor']])
