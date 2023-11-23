import random
import matplotlib.pyplot as plt
from random import choice

estudantes = ["João", "Maria", "José"]
notas = [8.5, 9, 6.5]

#plt.bar(x = estudantes, height = notas)
#plt.show()

estudantes_2 = ["João", "Maria", "José", "Ana"]
estudante = choice(estudantes_2)
print(estudante)

notas = {'1º Trimestre': 8.5, '2º Trimestre': 9.5, '3º Trimestre': 7}
print(notas)

soma = 0
for nota in notas.values():
    soma += nota

print(soma)

somatorio = sum(notas.values())
print(somatorio)

qtd_notas = len(notas)
print(qtd_notas)
media = somatorio/qtd_notas
print(round(media, 1))

def media():
    calculo = (10+9+8)/3
    print(calculo)

media()

def media2(nota_1, nota_2, nota_3):
    calculo = (nota_1+nota_2+nota_3)/3
    print(calculo)

media2(4, 5, 8)

notas = [8.5, 9.0, 6.0, 10.0]

def media(lista):
    calculo = sum(lista)/ len(lista)
    return calculo

resultado = media(notas)
print(resultado)

notas = [6.0, 7.0, 9.0, 5.0]

def boletim(lista):
    media = sum(lista)/ len(lista)
    if media >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    return (media, situacao)

media, situacao = boletim(notas)
print(media, situacao)
print(f'O estudante antigiu a média de {media} e foi {situacao}.')


#nota = float(input("Digite a nota do estudante:  "))

#def qualitativo(x):
#   return x + 0.5

#print(qualitativo(nota))
#funcoes lambda
#qualitativo = lambda x: x + 0.5
#print(qualitativo(nota))
'''
nota1 = float(input("Digite a 1º nota do estudante:  "))
nota2 = float(input("Digite a 2º nota do estudante:  "))
nota3 = float(input("Digite a 3º nota do estudante:  "))

media_ponderada = lambda x, y, z: (x * 3 + y * 2 + z * 5)/10
media_estudante = media_ponderada(nota1, nota2, nota3)
print(media_estudante)
print(f'O estudante antigiu a média de {media_estudante}')
'''
#utilizando o map
#map recebe uma funcao e uma lista
notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5

notas_atualizadas = map(lambda x: x + qualitativo, notas)
print(list(notas_atualizadas))