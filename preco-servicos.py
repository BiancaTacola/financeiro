import matplotlib.pyplot as plt

# Dados
servicos = ['Assinatura Básica', 'Assinatura Premium', 'Anúncios por Cliques']
precos_anteriores = [3.90, 6.90, 8.00]
novos_precos = [5.00, 9.00, 10.00]

# Criar gráfico de barras
plt.figure(figsize=(8, 6))
bar_width = 0.35
index = range(len(servicos))

plt.bar(index, precos_anteriores, bar_width, label='Preço Anterior', color='b')
plt.bar([i + bar_width for i in index], novos_precos,
        bar_width, label='Novo Preço', color='g')

plt.title('Aumento de Preços dos Serviços', fontsize=14)
plt.xlabel('Serviços', fontsize=12)
plt.ylabel('Preço (R$)', fontsize=12)
plt.xticks([i + bar_width / 2 for i in index], servicos)
plt.legend()

# Exibir gráfico
plt.tight_layout()
plt.show()
