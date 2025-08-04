import pandas as pd
import matplotlib.pyplot as plt

# Criar dados de exemplo para diferentes cargos na área de dados
dados = {
    'Cargo': ['Analista de Dados', 'Cientista de Dados', 'Engenheiro de Dados', 'Arquiteto de Dados'],
    'Salário Inicial': [4500, 6000, 7000, 9000],
    'Salário 2 anos': [6500, 8500, 9500, 12000],
    'Salário 5 anos': [8500, 12000, 13000, 15000]
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Configurar o estilo do gráfico (usando um estilo atualizado)
plt.style.use('seaborn-v0_8-darkgrid')
plt.figure(figsize=(12, 6))

# Criar linhas para cada cargo
for i in range(len(df)):
    plt.plot(['Inicial', '2 anos', '5 anos'],
             [df['Salário Inicial'][i], df['Salário 2 anos'][i], df['Salário 5 anos'][i]],
             marker='o',
             linewidth=2,
             label=df['Cargo'][i])

# Personalizar o gráfico
plt.title('Evolução Salarial na Área de Dados', fontsize=14, pad=20)
plt.xlabel('Tempo de Experiência', fontsize=12)
plt.ylabel('Salário (R$)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Cargos', bbox_to_anchor=(1.05, 1), loc='upper left')

# Formatar eixo y para mostrar valores em milhares
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {int(x):,}'))

# Salvar o gráfico em um arquivo
plt.savefig('linhas_chart.png', bbox_inches='tight')

print("Gráfico 'linhas_chart.png' gerado com sucesso.")
