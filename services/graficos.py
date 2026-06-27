import os
import plotly.express as px
from database import conexao

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
            "x": "Categorias",
            "y": "Quantidade de livros"
        },
        color=quantidades,
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        title = {
            "x": 0.5,
            "xanchor": "center",
        },
        
        xaxis_title="Categorias",
        yaxis_title="Quantidade de Livros",
        template="plotly_white",
        
        font=dict(
                family="Arial",
                size=14,
                color="black"
            )
        )   

    fig.update_traces(
        marker_color='blue',
        hovertemplate='Categoria: %{x}<br>Quantidade: %{y}<extra></extra>'
    )

    fig.write_html("graficos/livros_categoria.html")
    fig.show()
