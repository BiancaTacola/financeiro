import matplotlib.pyplot as plt

# Dados para o gráfico de receita e lucro
anos = [1, 2, 3, 4, 5]
receita_bruta = [49176, 98352, 162281, 202851, 212994]
lucro_liquido = [-50978, -31879, 7764, 30614, 36529]

# Criando o gráfico
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

# Exibir o gráfico
plt.tight_layout()
plt.show()
