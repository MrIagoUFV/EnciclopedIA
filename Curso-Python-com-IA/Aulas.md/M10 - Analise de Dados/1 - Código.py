# Analise de Dados - Gastos

# Criar um gráfico de pizza para visualizar os gastos por categoria
# Dentro de cada categoria:
    # - Exibir o nome da categoria
    # - Exibir o total gasto em formato de Real
    # - Exibir a porcentagem sobre o total
    # - Exibir a quantidade de transações

# Ao passar o mouse por cima de um pedaço da pizza:
    # Exibir mais detalhes sobre a categoria:
        # - O nome da categoria
        # - O total gasto em formato de Real
        # - A porcentagem sobre o total
        # - A quantidade de transações
        # - Lista de todas as transações dentro da categoria, detalhadamente

import pandas as pd
import plotly.graph_objects as go
from locale import setlocale, LC_ALL
import webbrowser
import os

# Configurar locale para formato brasileiro
setlocale(LC_ALL, 'pt_BR.UTF-8')

# Ler o arquivo CSV
df = pd.read_csv('C:/Users/iagol/Desktop/Curso Python/Aulas.md/M10 - Analise de Dados/gastos.csv')

# Função para limpar e converter valores monetários
def limpar_valor(valor):
    if pd.isna(valor):
        return 0
    return float(valor.replace('R$ ', '').replace('.', '').replace(',', '.'))

# Aplicar a função de limpeza em todas as colunas
for coluna in df.columns:
    df[coluna] = df[coluna].apply(limpar_valor)

# Calcular totais por categoria
totais = df.sum()
total_geral = totais.sum()

# Calcular quantidade de transações por categoria
qtd_transacoes = df.apply(lambda x: x[x > 0].count())

# Criar listas para o texto de hover
hover_text = []
for categoria in df.columns:
    # Calcular porcentagem
    porcentagem = (totais[categoria] / total_geral) * 100
    
    # Criar lista de transações
    transacoes = df[categoria][df[categoria] > 0].tolist()
    transacoes_texto = '<br>'.join([f'R$ {t:.2f}'.replace('.', ',') for t in transacoes])
    
    # Formatar texto do hover
    texto = (
        f'<b>{categoria}</b><br>'
        f'Total: R$ {totais[categoria]:.2f}<br>'
        f'Porcentagem: {porcentagem:.1f}%<br>'
        f'Quantidade de transações: {qtd_transacoes[categoria]}<br>'
        f'<br>Lista de transações:<br>{transacoes_texto}'
    ).replace('.', ',')
    
    hover_text.append(texto)

# Criar textos para as fatias do gráfico
text_info = []
for categoria in df.columns:
    porcentagem = (totais[categoria] / total_geral) * 100
    texto = (
        f'{categoria}<br>'
        f'R$ {totais[categoria]:.2f}<br>'
        f'{porcentagem:.1f}%<br>'
        f'{qtd_transacoes[categoria]} transações'
    ).replace('.', ',')
    text_info.append(texto)

# Criar gráfico de pizza
fig = go.Figure(data=[go.Pie(
    labels=df.columns,
    values=totais,
    hovertemplate="%{customdata}<extra></extra>",
    customdata=hover_text,
    text=text_info,
    textinfo='text',
    textposition='inside',
    insidetextorientation='radial'
)])

# Configurar layout
fig.update_layout(
    title='Análise de Gastos por Categoria',
    width=900,  # Aumentei um pouco para melhor visualização
    height=900,
    showlegend=False  # Removendo a legenda já que as informações estão nas fatias
)

# Salvar e abrir o gráfico
caminho_html = os.path.abspath('analise_gastos.html')
fig.write_html(caminho_html)
webbrowser.open('file://' + caminho_html)
