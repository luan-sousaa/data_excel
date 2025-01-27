import pandas as pd

# caminho para o arquivo do excel
caminho_arquivo = "C:/Users/Luan/Desktop/dados_vendas_git.csv"

# Leitura do Excel para DataFrame
data_frame = pd.read_csv(caminho_arquivo, delimiter=';')

#funçao que verifica se existe a coluna quantidade no data_frame e mostra a quantia de produtos vendidos
def quantidade():
    if "Quantidade" in data_frame.columns:
        quantidae = data_frame["Quantidade"].sum().astype(int)
        print(f"quantidade de produtos vendidos  = {quantidae}")
    else:
        print("vazio")
