import numpy as np
import matplotlib.pyplot as plt

dado = np.loadtxt('numpy-dados/apples_ts.csv', delimiter=',', usecols=np.arange(1, 88, 1))
print(dado)

print(dado.ndim)
print(dado.size)
print(dado.shape)

dado_transposto = dado.T
print(dado_transposto)
print(dado_transposto.shape)

print("Datas:............")
#pegando todas as linhas e somente a coluna 0
datas = dado_transposto[:,0]
datas = np.arange(1, 88, 1)
print(datas)

print("Preços:............")
#pegando todas as linhas primeiro arg antes do :
#segundo argumento colunas de 1 até 5, o 6 não entra
precos = dado_transposto[:,1:6]
print(precos)

#plt.plot(datas, precos[:,0])
#plt.show()

Moscow = precos[:, 0]
Kaliningrad = precos[:, 1]
Petersburg = precos[:, 2]
Krasnodar = precos[:, 3]
Ekaterinburg = precos[:, 4]

print(Moscow)
moscou_ano1 = Moscow[0:12]
moscou_ano2 = Moscow[13:25]
moscou_ano3 = Moscow[25:37]
moscou_ano4 = Moscow[37:49]

'''
plt.plot(np.arange(1, 13, 1), moscou_ano1)
plt.plot(np.arange(1, 13, 1), moscou_ano2)
plt.plot(np.arange(1, 13, 1), moscou_ano3)
plt.plot(np.arange(1, 13, 1), moscou_ano4)
plt.legend(['Ano 1', 'Ano 2', 'Ano 3', 'Ano 4'])
plt.show()
'''

#compara se os arrays são iguais
print(np.array_equal(moscou_ano3, moscou_ano4))
#mostra o quão próximo um array está do outro
#colocando um valor como parametro para calculo
#da proximidade dos valores
#A allclose() irá retornar True se a diferença
# entre os elementos do array for menor que o valor
# de fornecido 10.
print(np.allclose(moscou_ano3, moscou_ano4, 10))


print('Valores de kaliningrado')
print(Kaliningrad)
#somando os valores para saber quantos NANs exitem no array
print(sum(np.isnan(Kaliningrad)))
print((Kaliningrad[3] + Kaliningrad[5])/2)
#ou obter a media de duas posições
#fazendo a media do valor anterior ao NAN e o posterior
#e substituindo o NAN da tabela pelo valor da media calculado
Kaliningrad[4] = np.mean([Kaliningrad[3], Kaliningrad[5]])
#plt.plot(datas, Kaliningrad)
#plt.show()

print(np.mean(Moscow))
print(np.mean(Kaliningrad))

#plotando uma reta ajustada aos dados
'''
x = datas
y = 0.52 * x + 80

Note que nos é retornado o gráfico com a linha de variação 
dos preços e uma reta laranja que parece não corresponder 
com os dados do gráfico. Podemos, então, pensar em como fazer 
para que ela se mantenha próxima aos dados.

O primeiro passo pode ser verificar a diferença entre a reta 
e os dados, ou seja, analisar se a reta se ajusta aos dados. 
Para isso, podemos fazer uma subtração entre os dados de ambos

print(Moscow-y)


Para lidar com este problema de valores negativos e positivos, 
podemos elevá-los ao quadrado utilizando a função power(), 
que eleva valores a uma potência. Basta passarmos o valor 
a ser elevando e a potência desejada.

print(np.power(Moscow-y, 2))

Como retorno, temos um array com os valores elevados ao quadrado. 
Mas note que são valores muito grandes, com várias casas decimais, 
dificultando a análise deste ajuste.

O ideal, portanto, é conseguir resumi-los em um único número, 
somando-os, por exemplo. Para isso, utilizaremos a função sum(), 
envolvendo o cálculo como parâmetro:

print(np.sum(np.power(Moscow-y,2)))
#Um artifício final que podemos utilizar é calcular a raiz utilizando
# a função sqrt():
print(np.sqrt(np.sum(np.power(Moscow-y,2))))
'''
#tudo isso acima kkkk pode ser resumido com a função linalg.norm
#print(np.linalg.norm(Moscow-y))


#Processo de calculo de regressão linear para calcular
#o coeficiente linear e angular do eixo y da reta sobre os dados
#calculo do coeficiente angular
Y = Moscow
X = datas
#numero de elementos
n = np.size(Moscow)
#coeficiente_angular estimado â
a = ((n*np.sum(X*Y) - np.sum(X)*np.sum(Y))
     /(n*np.sum(X**2) - np.sum(X)**2))
print(a)

#coeficiente linear ^b
b = np.mean(Y) - a * np.mean(X)
print(b)

y = a * X + b

print(np.linalg.norm(Moscow-y))

plt.plot(datas, Moscow)
plt.plot(X, y)
#plotar um ponto na reta usando o calculo da regressão linear
#*b é para plotar um * blue na reta
plt.plot(41.5, 41.5 * a+b, '*b')
#estimar valores para o futuro com a projeção da reta no mes 100
plt.plot(100, 100 * a+b, '*r')
plt.show()

#gera valores inteiros aleatórios
print(np.random.randint(low=40, high=100, size=100))

#gerando valores de ponto flutuante aleatorios
print(np.random.uniform(low=0.10, high=0.90, size=100))

np.random.seed(84)
coeficientes_angulares = np.random.uniform(low=0.10, high=0.90, size=100)

norma2 = np.array([])
for i in range(100):
    norma2 = np.append(norma2, np.linalg.norm(Moscow-(coeficientes_angulares[i]*X+b)))

#print(norma2)
#print(coeficientes_angulares[1])

dados = np.column_stack([norma2, coeficientes_angulares])
print(dados)
print(dados.shape)

np.savetxt('dados.csv', dados, delimiter=',')