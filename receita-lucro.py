import matplotlib.pyplot as plt

# Dados
anos = [1, 2, 3, 4, 5]
receita_bruta = [80000, 160000, 260000, 350000, 450000]
lucro_liquido = [-10000, 30000, 90000, 150000, 200000]

# Criar gráfico de linha
plt.figure(figsize=(8, 6))
plt.plot(anos, receita_bruta, marker='o',
         color='b', label='Receita Bruta (R$)')
plt.plot(anos, lucro_liquido, marker='o',
         color='g', label='Lucro Líquido (R$)')

plt.title('Projeção de Receita e Lucro (5 anos)', fontsize=14)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Valor (R$)', fontsize=12)
plt.grid(True)
plt.legend()

# Exibir gráfico
plt.tight_layout()
plt.show()
