# Importa a biblioteca de gráficos
import matplotlib.pyplot as plt
 
# Dados para o gráfico
categorias = ['uva', 'maçã', 'amora', 'abacaxí','framboesa', 'tomate', 'ameixa', 'abacate', 'laranja', 'limão']
quantidade = [80, 65, 40, 35, 52, 98, 89, 70, 20, 105]
 
# Cria o gráfico de barras
plt.bar(categorias, quantidade)
# Adiciona título e rótulos
plt.title("Frutas mais consumidas")
plt.xlabel("Frutas")
plt.ylabel("Quantidade")
 
# Mostra o gráfico na tela
plt.show()