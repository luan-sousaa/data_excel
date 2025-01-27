import pandas as pd

# Substitua 'arquivo.xlsx' pelo caminho do seu arquivo Excel
caminho_arquivo = 'arquivo.xlsx'

# Leitura do Excel para DataFrame
# Selecione a aba do Excel que deseja ler passando o nome da aba em `sheet_name`
data_frame = pd.read_excel(caminho_arquivo)

# Exibe os dados lidos no prompt
print(data_frame)
