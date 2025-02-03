import style
from dash import dash_table, dcc
import pandas as pd

from dash import Dash, html
import plotly.express as px


# caminho para o arquivo do excel
caminho_arquivo = "dados_vendas_git.csv"

# Leitura do Excel para DataFrame
data_frame = pd.read_csv(caminho_arquivo, delimiter=';')

def quantidade():
    if "Quantidade" in data_frame.columns:
        quantidade_produto =  data_frame["Quantidade"].sum().astype(int)
        return f"Quantidade de produtos vendidos = {quantidade_produto}"
    else:
        return 'Coluna "Quantidade" não encontrada'

def valor_total():
    if "Total_Venda" in data_frame.columns:
        valor_total_vendido = data_frame["Total_Venda"].sum().astype(float)
        return f"Valor total dos produtos vendidos = R$ {valor_total_vendido:.2f}"

def produtos_vendido():
    if "Produto" in data_frame.columns and "Quantidade" in data_frame.columns:
        # Agrupar por produto e sumarizar a quantidade vendida
        vendas_por_produto = data_frame.groupby('Produto')['Quantidade'].sum().reset_index()


        # Ordenar os produtos pela quantidade vendida em ordem decrescente
        vendas_por_produto = vendas_por_produto.sort_values(by="Quantidade", ascending=False)

        # Converter os dados para uma lista
        lista_vendas = [f"{row['Produto']}: {row['Quantidade']}" for _, row in vendas_por_produto.iterrows()]

        # Função que mostra o produto mais vendido
        produto_mais_vendido = vendas_por_produto.iloc[0, 0]
        quantidade_produto_mais_vendido = vendas_por_produto.iloc[0, 1]

        # Criar a saída como uma única string
        resultado = (
            f"Quantidade vendida por produto (em ordem decrescente): {lista_vendas}",
            html.Br(),
            f"Produto mais vendido: {produto_mais_vendido}",
            html.Br(),
            f"Quantidade de produtos vendidos: {quantidade_produto_mais_vendido}"
        )
        return resultado
    else:
        return 'As colunas "Produto" e/ou "Quantidade" não foram encontradas.'


#inicialização do app
app = Dash()


#adiciona cores de fundo e do texto
colors = {
    'background': '#A9A9A9',
    'text': '#000000'}

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.H1(
            "Gráfico das vendas",
            style={'textAlign': 'center', 'color': colors['text']}  # Cor e alinhamento do texto
        ),


        html.Div([
            html.H3("Resumo das Vendas", style={'color': colors['text']}),
            html.P(quantidade(), style={'color': colors['text']}),
            html.P(valor_total(), style={'color': colors['text']}),
            html.P(produtos_vendido(), style={'color': colors['text']})
        ]),

        html.Div([
            html.H3("Tabela de Dados", style={'color': colors['text']}),
            dash_table.DataTable(
                data=data_frame.to_dict('records'),
                page_size=10,
                style_table={'overflowX': 'auto'},
                style_header={
                    'backgroundColor': colors['background'],
                    'color': colors['text']
                },
                style_data={
                    'backgroundColor': colors['background'],
                    'color': colors['text']
                }
            ),

        dcc.Graph(
        figure=px.histogram(data_frame, x='Produto', y='Quantidade', histfunc='avg',title="Quantidade de vendas por produto")
        .update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font=dict(color=colors['text'])
        )
        ),

        dcc.Graph(
        figure=px.histogram(data_frame, x="Total_Venda", y="Região", color="Produto",histfunc="avg",title="Vendas Por Região" )

        .update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font=dict(color=colors['text'])
        )
        ),
        dcc.Graph(
        figure=px.histogram(data_frame, x='Cliente', y='Quantidade' ,histfunc='avg',title="Quantidade de vendas por cliente")
        .update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font=dict(color=colors['text'])
        )
        )
    ])
    ]
)

if __name__ == '__main__':
    app.run(debug=True)