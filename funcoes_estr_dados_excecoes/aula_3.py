from random import randint

notas_turma = ['João', 8.0, 9.0, 10.0,
               'Maria', 9.0, 7.0, 6.0,
               'José', 3.4, 7.0, 7.0,
               'Cláudia', 5.5, 6.6, 8.0,
               'Ana', 6.0, 10.0, 9.5]

nomes = []
notas_juntas = []

for i in range(len(notas_turma)):
    if i % 4 == 0:
        nomes.append(notas_turma[i])
    else:
        notas_juntas.append(notas_turma[i])

print(nomes)
print(notas_juntas)

notas = []

for i in range(0, len(notas_juntas), 3):
    notas.append([notas_juntas[i], notas_juntas[i+1], notas_juntas[i+2]])

print(notas)
print(notas[0])
print(notas[0][2])


estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]
def gera_codigo():
  return str(randint(0,999))

gera_codigo()

codigo_estudantes = []

for i in range(len(estudantes)):
    codigo_estudantes.append((estudantes[i], estudantes[i][0] + gera_codigo()))

print(codigo_estudantes)

#list comprehension
notas = [[8.0, 9.0, 10.0],
         [9.0, 7.0,  6.0],
         [3.4, 7.0,  7.0],
         [5.5, 6.6,  8.0],
         [6.0, 10.0, 9.5]]


def media(lista: list = [0]) -> float:
    ''' Função para calcular a média
    de notas passadas por uma lista
    lista: list, default [0]
      Lista com as notas para calcular a média
    return = calculo: float
      Média calculada
    '''
    calculo = sum(lista) / len(lista)
    return calculo

medias = [round(media(nota), 1) for nota in notas]
print(medias)


nomes = [('João',  'J720'),
         ('Maria', 'M205'),
         ('José',  'J371'),
         ('Cláudia', 'C546'),
         ('Ana', 'A347')]
#medias = [9.0, 7.3, 5.8, 6.7, 8.5]
nomes = [nome[0] for nome in nomes]
print(nomes)

estudantes = list(zip(nomes, medias))
print(estudantes)

candidatos = [estudante[0] for estudante in estudantes if estudante[1] >= 8.0]
print(candidatos)


nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

situacao = ["Aprovado" if media >= 6 else "Reprovado" for media in medias]
print(situacao)

cadastro = [x for x in [nomes, notas, medias, situacao]]
print(cadastro)

list_completa = [nomes, notas, medias, situacao]
print(list_completa)
lista_completa_compreensivel = list(zip(nomes, notas, medias, situacao))
print(lista_completa_compreensivel)

#dict comprehension
lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

# Colunas com os tipos dos dados (exceto nome)
coluna = ["Notas", "Média Final", "Situação"]

cadastro = {coluna[i]: lista_completa[i+1] for i in range(len(coluna))}
print(cadastro)

#extrair os nomes dos estudantes
cadastro["Estudantes"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]
print(cadastro)

lista_nova = list(zip(cadastro["Estudantes"], cadastro["Notas"], cadastro["Média Final"], cadastro["Situação"]))
print(lista_nova)

nomes_estudantes = [ "Enrico Monteiro", "Luna Pereira", "Anthony Silveira", "Letícia Fernandes",
                    "João Vitor Nascimento", "Maysa Caldeira", "Diana Carvalho", "Mariane da Rosa",
                    "Camila Fernandes", "Levi Alves", "Nicolas da Rocha", "Amanda Novaes",
                    "Laís Moraes", "Letícia Oliveira", "Lucca Novaes", "Lara Cunha",
                    "Beatriz Martins", "João Vitor Azevedo", "Stephany Rosa", "Gustavo Henrique Lima" ]

medias_estudantes = [5.4, 4.1, 9.1, 5.3, 6.9, 3.1, 10.0, 5.0, 8.2, 5.5,
                    8.1, 7.4, 5.0, 3.7, 8.1, 6.2, 6.1, 5.6, 6.7, 8.2]

bolsistas = {nome: media
             for nome, media in zip(nomes_estudantes, medias_estudantes)
             if media >= 9.0}
print(bolsistas)