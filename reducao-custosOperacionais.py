import matplotlib.pyplot as plt

# Dados
anos = [1, 2, 3, 4, 5]
custos_operacionais = [90000, 85000, 80000, 75000, 70000]

# Criar gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(anos, custos_operacionais, color='r')

plt.title('Redução de Custos Operacionais', fontsize=14)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Custos Operacionais (R$)', fontsize=12)
plt.grid(True)

# Exibir gráfico
plt.tight_layout()
plt.show()
