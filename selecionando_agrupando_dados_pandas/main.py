import pandas as pd

emissoes_gases = pd.read_excel('1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx', sheet_name='GEE Estados')
#print(emissoes_gases.info())

#mostra os valores que existem para essa coluna Emissão Remossão Bunker
#print(emissoes_gases['Emissão / Remoção / Bunker'].unique())

#(emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção NCI') | (emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção')

#filtragem dos dados da coluna de Emissão...
#apenas as linhas que tem os valores 'Remoção NCI', 'Remoção'
remocao_gases = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção'])]

#selecionar somente os dados numericos dos anos
remocao_dados_numericos = emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021]

#saber se os valores são realmente de remoção, nesse caso os valores devem ser
#zero pois são de remoção (negativos)
remocao_dados_numericos = emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021].max()
print(remocao_dados_numericos)

#verificar se algum valor do tipo bunker corresponde a alguma emissão feita por algum estado
print(emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'] == 'Bunker', 'Estado'].unique())

#removendo as linhas da coluna Emissão/Remoção.. que não sejam iguais a 'Emissão'
emissoes_gases = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'] == 'Emissão']

emissoes_gases = emissoes_gases.drop(columns = 'Emissão / Remoção / Bunker')
print(emissoes_gases)

colunas_info = list(emissoes_gases.loc[:,'Nível 1 - Setor':'Produto'].columns)
print(colunas_info)

colunas_emissao = list(emissoes_gases.loc[:,'1970':'2021'].columns)
print(colunas_emissao)

emissoes_gases_por_ano = emissoes_gases.melt(id_vars = colunas_info, value_vars = colunas_emissao, var_name = 'Ano', value_name = 'Emissão')
print(emissoes_gases_por_ano)

emissoes_gases_por_ano.groupby('Gás').groups
emissoes_gases_por_ano.groupby('Gás').get_group('CO2 (t)')

emissoes_gases_por_ano.groupby('Gás').sum(numeric_only = True)
emissoes_gases_por_ano.groupby('Gás')[['Emissão']].sum()

emissoes_gases_por_ano = emissoes_gases_por_ano.groupby('Gás')[['Emissão']].sum().sort_values('Emissão', ascending = False)
print(emissoes_gases_por_ano)
