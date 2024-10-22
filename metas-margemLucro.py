import matplotlib.pyplot as plt

# Dados
labels = ['Margem Bruta', 'Margem Líquida']
tamanhos = [65, 45]
cores = ['#66b3ff', '#99ff99']

# Criar gráfico de pizza
plt.figure(figsize=(6, 6))
plt.pie(tamanhos, labels=labels, colors=cores,
        autopct='%1.1f%%', startangle=90)

plt.title('Metas de Margem de Lucro', fontsize=14)

# Exibir gráfico
plt.tight_layout()
plt.show()
