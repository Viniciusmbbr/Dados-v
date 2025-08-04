import matplotlib.pyplot as plt
import numpy as np

# Dados sobre a importância da área de dados
aspectos = [
    'Tomada de Decisão',
    'Otimização de Processos',
    'Previsão de Tendências',
    'Experiência do Cliente',
    'Vantagem Competitiva'
]

importancia = [30, 25, 20, 15, 10]  # Valores em porcentagem
cores = ['#2ecc71', '#3498db', '#9b59b6', '#e74c3c', '#f1c40f']

# Criar figura com tamanho personalizado
plt.figure(figsize=(10, 8))

# Criar gráfico de pizza
plt.pie(importancia,
        labels=aspectos,
        colors=cores,
        autopct='%1.1f%%',
        startangle=90,
        shadow=True,
        explode=(0.1, 0, 0, 0, 0))

# Adicionar título
plt.title('Importância da Área de Dados para Empresas', pad=20, size=14)

# Adicionar legenda
plt.legend(aspectos,
          title="Aspectos Importantes",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Garantir que o gráfico seja circular
plt.axis('equal')

# Salvar o gráfico em vez de mostrá-lo
plt.savefig('importancia_chart.png', bbox_inches='tight')

print("Gráfico 'importancia_chart.png' foi gerado com sucesso.")
