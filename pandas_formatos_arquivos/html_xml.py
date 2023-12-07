import pandas as pd

#percorre as tabelas internas do html
dados_html = pd.read_html('Filmes_Wikipedia.html')
print(dados_html)
print(type(dados_html))
print(len(dados_html))

top_filmes = dados_html[1]
print(top_filmes)
top_filmes.to_html('top_filmes.html')
top_filmes.to_csv('top_filmes_1998.csv', index=False)

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/imdb_top_1000.xml'
dados_xml = pd.read_xml(url)
print(dados_xml)
dados_xml.to_xml('filmes_imdb.xml')