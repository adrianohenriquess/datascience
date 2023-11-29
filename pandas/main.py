import pandas as pd
import matplotlib.pyplot as plt

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

#parte 2
#analise exploratória dos dados
print(dados.head())

media = dados['Valor'].mean()
print(media)

media_agrupada = dados.groupby('Tipo').mean(numeric_only=True)
print(media_agrupada)

media_agrupada_por_tipo = dados.groupby('Tipo')['Valor'].mean()
print(media_agrupada_por_tipo)

#transformar em dataframe e ordenar
media_agrupada_data_frame = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
print(media_agrupada_data_frame)

#media_agrupada_data_frame.plot(kind ='barh', figsize=(14, 10), color = 'purple')
#media_agrupada_data_frame.plot.barh(figsize=(14, 10), color = 'purple')
#plt.show()

#removendo os imoveis comerciais
print(dados.Tipo.unique)

imoveis_comerciais = ['Conjunto Comercial/Sala',
                      'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

df_imoveis_nao_comerciais = dados.query('@imoveis_comerciais not in Tipo')
print(df_imoveis_nao_comerciais)
print(df_imoveis_nao_comerciais.Tipo.unique())

media_df_imoveis_nao_comerciais = df_imoveis_nao_comerciais.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
print(media_df_imoveis_nao_comerciais)

#media_df_imoveis_nao_comerciais.plot.barh(figsize=(14, 10), color = 'purple')
#plt.show()
print(df_imoveis_nao_comerciais.Tipo.unique())
#contar os tipos de imoveis
print(df_imoveis_nao_comerciais.Tipo.value_counts(normalize=True))

#converter a series em um data_frame
print(df_imoveis_nao_comerciais.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo'))

df_percentual_tipo = df_imoveis_nao_comerciais.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo')
#df_percentual_tipo.plot.bar(figsize=(14, 10), color = 'green',
#                             xlabel = 'Tipos', ylabel = 'Percentual')
#plt.show()

#selecionar apenas os apartamentos que representam 84% dos dados
df_apartamentos = df_imoveis_nao_comerciais.query('Tipo == "Apartamento"')
print(df_apartamentos)

#3ª parte tratar dados nulos
print(df_apartamentos.isnull().sum())

print(df_apartamentos.fillna(0))
df_apartamentos = df_apartamentos.fillna(0)
print(df_apartamentos.isnull().sum())

#remover registros inconsistentes
print(df_apartamentos.query('Valor == 0 | Condominio == 0'))
registros_a_remover = df_apartamentos.query('Valor == 0 | Condominio == 0').index
#remover linhas com o parametro axis = 0
#inplace aplica as alterações sem precisar reatribuir a mesma
#variavel
df_apartamentos.drop(registros_a_remover, axis=0, inplace=True)
print(df_apartamentos.query('Valor == 0 | Condominio == 0'))


print(df_apartamentos.head())
#removendo a coluna tipo que só tem um valor
df_apartamentos.drop('Tipo', axis=1, inplace=True)
print(df_apartamentos.head())

#aplicar filtros
print(df_apartamentos['Quartos'] == 1)
selecao1 = df_apartamentos['Quartos'] == 1
selecao2 = df_apartamentos['Valor'] < 1200
print(df_apartamentos[selecao1])
print(df_apartamentos[selecao2])

selecao_final = (selecao1) & (selecao2)

df_1 = df_apartamentos[selecao_final]

selecao = ((df_apartamentos['Quartos'] >= 2)
           & (df_apartamentos['Valor'] < 3000)
           & (df_apartamentos['Area']  >   70))
df_2 = df_apartamentos[selecao]
print(df_1)
print(df_2)

#salvar os dados
df_apartamentos.to_csv('dados_apartamentos.csv', index=False, sep=';')

print(pd.read_csv('dados_apartamentos.csv', sep=';'))
