import os
import plotly.express as px
from database import conexao
import webbrowser

from plotly.subplots import make_subplots
import plotly.graph_objects as go

cursor, conexao = conexao()

def dashboard_livros_categoria():
    os.makedirs("graficos", exist_ok=True)

    sql = """
    SELECT
        c.nome,
        COUNT(l.id) AS quantidade
    FROM categoria c
    LEFT JOIN livros l
        ON l.categoriaid = c.id
    GROUP BY c.nome
    ORDER BY c.nome;
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    categorias = []
    quantidades = []

    for categoria, quantidade in dados:
        categorias.append(categoria)
        quantidades.append(quantidade)

    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=("", ""),
        specs=[[{"type": "bar"}, {"type": "pie"}]]
    )

    fig.add_trace(
        go.Bar(
            x=categorias,
            y=quantidades,
            name="Quantidade de Livros",
            marker_color="#4F81BD"
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Pie(
            labels=categorias,
            values=quantidades,
            name="Distribuição de Livros",
            hole=0.4
        ),
        row=1, col=2
    )

    fig.update_layout(
        title_text="Dashboard: Quantidade de Livros por Categoria",
        width=1800,
        height=600,
        showlegend=True
    )

    fig.write_html("graficos/dashboard_livros_categoria.html")

    return fig

def exibir_dashboard():
    fig = dashboard_livros_categoria()  # Gera o dashboard atualizado
    fig.show()  # Exibe o dashboard em uma janela do navegador
