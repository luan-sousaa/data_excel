import dcc
from dash import dash_table, dcc
import pandas as pd

from dash import Dash, html
import plotly.express as px


# caminho para o arquivo do excel
caminho_arquivo = "C:/Users/Luan/Desktop/dados_vendas_git.csv"

# Leitura do Excel para DataFrame
data_frame = pd.read_csv(caminho_arquivo, delimiter=';')

def quantidade():
    if "Quantidade" in data_frame.columns:
        quantidade_produto =  data_frame["Quantidade"].sum().astype(int)
        print(f"Quantidade de produtos vendidos = {quantidade_produto}")
    else:
        print('Coluna "Quantidade" não encontrada')
quantidade()

def valor_total():
    if "Total_Venda" in data_frame.columns:
        valor_total_vendido = data_frame["Total_Venda"].sum().astype(float)
        print(f"Valor total dos produtos vendidos = R$ {valor_total_vendido:.2f}")
valor_total()

def produtos_vendido():
    if "Produto" in data_frame.columns and "Quantidade" in data_frame.columns:
        # Agrupar por produto e sumarizar a quantidade vendida
        vendas_por_produto = data_frame.groupby('Produto')['Quantidade'].sum().reset_index()

        # Ordenar os produtos pela quantidade vendida em ordem decrescente
        vendas_por_produto = vendas_por_produto.sort_values(by="Quantidade", ascending=False)
        print("Quantidade vendida por produto (em ordem decrescente):")
        print(vendas_por_produto)

        #funçao que mostra o produto mais vendido
        produto_mais_vendido = vendas_por_produto.iloc[0, 0]
        print(f"Produto mais vendido: {produto_mais_vendido}")

        quantidade_produto_mais_vendido = vendas_por_produto.iloc[0, 1]
        print(f"Quantidade de produtos vendidos: {quantidade_produto_mais_vendido}")
    else:
        print('As colunas "Produto" e/ou "Quantidade" não foram encontradas.')


produtos_vendido()


#inicialização do app
app = Dash()

#adiciona cores de fundo e do texto
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
#adiciona cores de fundo e do texto
colors = {
    'background': '#000000',
    'text': '#A9A9A9'}

app.layout = html.Div([
    html.Div(["Gráfico das vendas"]),
    #dash_table.DataTable(data=data_frame.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(data_frame, x='Produto', y='Quantidade', histfunc='avg')),
    #dcc.Graph(figure=px.density_heatmap(data_frame, x="Região", y="Total_Venda")),
    dcc.Graph(figure=px.histogram(data_frame, x='Cliente', y='Quantidade', histfunc='avg'))
])

if __name__ == '__main__':
    app.run(debug=True)
