#importa a biblioteca de graficos 
import matplotlib.pyplot as plt

#dados para o grafico
categorias = ['Python', 'javaScript', 'java']
quantidade = [80, 65, 40]

#cria o grafico de barras
plt.bar(categorias, quantidade)

#adiciona titulos e rotulos
plt.title("linguagens mais usadas")
plt.xlabel("linguagem")
plt.ylabel("quantidade")

#mostra o grafico na tela
plt.show()