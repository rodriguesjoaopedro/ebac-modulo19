import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV em um dataframe
dados_gasolina = pd.read_csv('gasolina.csv')

# Gerar o gráfico de linha utilizando o Seaborn
sns.lineplot(x='dia', y='venda', data=dados_gasolina)

# Salvar o gráfico em um arquivo PNG
plt.savefig('gasolina.png')
