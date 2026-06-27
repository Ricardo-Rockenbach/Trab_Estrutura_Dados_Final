import os
import plotly.express as px
from database import conexao

from plotly.subplots import make_subplots
import plotly.graph_objects as go

cursor, conexao = conexao()

def grafico_livros_categoria():

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

    # Separa os dados em duas listas
    for categoria, quantidade in dados:
        categorias.append(categoria)
        quantidades.append(quantidade)

    fig = px.bar(
        x=categorias,
        y=quantidades,
        title="Quantidade de livros por categoria",
        labels={
            "x": "",
            "y": "Quantidade"
        },
        width=1200,
        height=600
    )

    fig.update_layout(

        template="plotly_white",

        title={
            "text": "Quantidade de Livros por Categoria",
            "x": 0.5,
            "xanchor": "center",
            "font": {
                "size": 22
            }
        },

        width=1200,
        height=600,

        margin=dict(
            l=60,
            r=40,
            t=70,
            b=60
        ),

        font=dict(
            family="Segoe UI",
            size=14,
            color="#333333"
        ),

        plot_bgcolor="white",
        paper_bgcolor="white",

        bargap=0.35,

        showlegend=False,

        xaxis=dict(
            title="Categoria",
            showgrid=False,
            zeroline=False
        ),

        yaxis=dict(
            title="Quantidade de livros",
            gridcolor="#EAEAEA",
            zeroline=False
        )
    )

    fig.update_traces(

        marker=dict(
            color="#4F81BD",
            line=dict(
                color="#3A5F8A",
                width=1
            )
        ),

        text=quantidades,
        textposition="outside",

        hovertemplate="<b>%{x}</b><br>Livros: %{y}<extra></extra>"
    )

    fig.update_layout(barcornerradius=8)

    fig.write_html("graficos/livros_categoria.html")
    fig.show()


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
    fig.show()