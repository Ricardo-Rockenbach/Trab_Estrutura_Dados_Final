import os
import webbrowser
from database import conexao
from services.graficos import dashboard_livros_categoria



cursor, conexao = conexao()

def gerar_pagina():
    # Atualiza o gráfico
    dashboard_livros_categoria()
    
    sql = """
        SELECT
            l.id,
            l.titulo,
            l.autor,
            l.ano,
            c.nome as categoria

        FROM livros l
        JOIN categoria c ON c.id = l.categoriaid
        ORDER BY l.titulo
    """

    cursor.execute(sql)
    livros = cursor.fetchall()

    linhas = ""

    for livro in livros:
        linhas += f"""
        <tr>
            <td>{livro[0]}</td>
            <td>{livro[1]}</td>
            <td>{livro[2]}</td>
            <td>{livro[3]}</td>
            <td>{livro[4]}</td>
            
        </tr>
        """

        html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">

    <head>

    <meta charset="UTF-8">

    <title>Biblioteca</title>

    <link rel="stylesheet" href="style.css">

    </head>

    <body>

    <h1>Sistema Biblioteca</h1>

    <table>

    <thead>
    <tr>
    <th>ID</th>
    <th>Título</th>
    <th>Autor</th>
    <th>Ano</th>
    <th>Categoria</th>
    </tr>
    </thead>

    <tbody>

    {linhas}

    </tbody>

    </table>

    <h2>Dashboard</h2>

    <iframe
        src="../graficos/dashboard_livros_categoria.html"
        width="100%"
        height="650"
        frameborder="0">
    </iframe>

    </body>
    </html>
    """
        
    os.makedirs("web", exist_ok=True)

    with open("web/index.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(html)

    webbrowser.open(os.path.abspath("web/index.html"))