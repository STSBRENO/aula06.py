# Importa a biblioteca de gráficos
import matplotlib.pyplot as plt
 
# Dados para o gráfico
categorias = ['Apple', 'Motorola', 'LG', 'Samsung', 'Xiaomi', 'Lenovo', 'Sony', 'Nokia', 'Asus', 'Microsoft']
quantidade = [80, 65, 40, 100, 52, 60, 15, 70, 35, 125]
 
# Cria o gráfico de barras
plt.bar(categorias, quantidade)
# Adiciona título e rótulos
plt.title("Marcas de celulares mais vendidas no mês de Julho")
plt.xlabel("Marcas")
plt.ylabel("Quantidade de aprelhos vendidos")
 
# Mostra o gráfico na tela
plt.show()