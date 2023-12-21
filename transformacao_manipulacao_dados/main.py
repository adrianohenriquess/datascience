import pandas as pd
import numpy  as np

url_dados_hospedagem = 'https://caelum-online-public.s3.amazonaws.com/2928-transformacao-manipulacao-dados/dados_hospedagem.json'
url_dados_imoveis_disponiveis = 'https://caelum-online-public.s3.amazonaws.com/2928-transformacao-manipulacao-dados/moveis_disponiveis.json'

dados = pd.read_json(url_dados_hospedagem)

dados = pd.json_normalize(dados['info_moveis'])

colunas = list(dados.columns)

#passar para o explode da coluna de indice 3 para frente
dados = dados.explode(colunas[3:])

dados.reset_index(inplace=True, drop=True)

#tratamento manual das colunas
dados['max_hospedes'] = dados['max_hospedes'].astype(np.int64)

col_numericas = ['quantidade_banheiros', 'quantidade_quartos', 'quantidade_camas']
dados[col_numericas] = dados[col_numericas].astype(np.int64)
dados['avaliacao_geral'] = dados['avaliacao_geral'].astype(np.float64)

dados['preco'] = dados['preco'].apply(lambda x: x.replace('$', '').replace(',', '').strip())
dados['preco'] = dados['preco'].astype(np.float64)
dados[['taxa_deposito', 'taxa_limpeza']] = dados[['taxa_deposito', 'taxa_limpeza']].map(lambda x: x.replace('$', '').replace(',', '').strip())

print(dados.head())