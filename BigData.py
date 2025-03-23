import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def gerar_dados(n=10000):
    data = {
        'ID': np.arange(1, n + 1),
        'Idade': np.random.randint(18, 65, size=n),
        'Salario': np.random.randint(1500, 14000, size=n)
    }
    return pd.DataFrame(data)

categoria_ordem = ['A - Baixa Renda', 'B - Média Baixa Renda', 'C - Média Alta Renda', 'D - Alta Renda']
definir_categoria = lambda salario: (
    'A - Baixa Renda' if 1500 <= salario <= 5000 else
    'B - Média Baixa Renda' if 5001 <= salario <= 10000 else
    'C - Média Alta Renda' if 10001 <= salario <= 13000 else
    'D - Alta Renda'
)

df = gerar_dados()
df['Categoria'] = df['Salario'].apply(definir_categoria)

categoria_counts = df['Categoria'].value_counts()
categoria_counts = categoria_counts.reindex(categoria_ordem)

plt.figure(figsize=(10, 5))
categoria_counts.plot(kind='bar', color=['#990000', '#CCCC00', '#003366', '#006600'])
plt.title("Distribuição de Categorias por Salário")
plt.xlabel("Categoria")
plt.ylabel("Pessoas")
plt.xticks(rotation=0) 
plt.show()

print(df.head(20))