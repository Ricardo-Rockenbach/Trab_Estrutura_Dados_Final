from database import conexao
from crud import categorias as cat
from rich.console import Console

console = Console()

cursor, conexao = conexao()

def cadastrar():
    console.print("Função Cadastrar livro", style="bold blue")

    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação do livro (opcional): ") or None
    cat.listar()  # Exibe a lista de categorias
    categoria_id = int(input("Digite o ID da categoria: "))
    categoriaId = categoria_id if categoria_id else None  # Permite que categoriaId seja nulo

    console.print(f"Título: {titulo}", style="green")
    console.print(f"Autor: {autor}", style="green")
    console.print(f"Ano: {ano}", style="green")
    console.print(f"Categoria: {categoria_id} ({type(categoria_id)})", style="green")

    input("Pressione Enter para confirmar o cadastro...")

    sql = "INSERT INTO livros (titulo, autor, categoriaId) VALUES (%s, %s, %s)"
    cursor.execute(sql, (titulo, autor, categoriaId))
    conexao.commit()


def listar():
    sql = "SELECT * FROM livros"
    cursor.execute(sql)

    console.print("Listar livros", style="bold blue")
    for livro in cursor.fetchall():
        console.print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Categoria ID: {livro[4]}", style="green")


def alterar():
    console.print("Função Alterar livro", style="bold blue")
    listar()

    id_livro = input("Digite o ID do livro que deseja alterar: ")

    if id_livro == "":
        console.print("ID inválido. Operação cancelada.", style="bold red")
        return
    
    # Buscar dados atuais do livro selecionado
    sql_livro = "SELECT titulo, autor, ano FROM livros WHERE id = %s"
    cursor.execute(sql_livro, (id_livro,))
    livro_atual = cursor.fetchone()

    if livro_atual is None:
        console.print("Livro não encontrado.", style="bold red")
        return

    titulo_atual, autor_atual, ano_atual = livro_atual

    titulo = input(f"Digite o novo título do livro [{titulo_atual}]:  ") or livro_atual[0]
    autor = input(f"Digite o novo autor do livro [{autor_atual}]: ") or livro_atual[1]
    ano = input(f"Novo ano [{ano_atual if ano_atual else 'Sem ano'}]: ")
    ano = int(ano) if ano else ano_atual

    if titulo == "":
        sql = "SELECT titulo FROM livros WHERE id = %s"
        cursor.execute(sql, (id_livro,))
        titulo = cursor.fetchone()[0]

    sql_update = "UPDATE livros SET titulo = %s, autor = %s, ano = %s WHERE id = %s"
    cursor.execute(sql_update, (titulo, autor, ano, id_livro))
    conexao.commit()


def excluir():
    console.print("Excluir livros", style="bold blue")
    listar()

    id_livro = input("Digite o ID do livro que deseja excluir: ")
    livro_selecionado_sql = "SELECT titulo FROM livros WHERE id = %s"
    cursor.execute(livro_selecionado_sql, (id_livro,))

    sql = "DELETE FROM livros WHERE id = %s"

    if id_livro == "":
        console.print("ID inválido. Operação cancelada.", style="bold red")
        return
    
    livro_selecionado = cursor.fetchone()
    console.print(f"Confirma a exclusão do Livro {livro_selecionado[0]} de ID {id_livro}? (s/n)", style="bold yellow")
    confirmacao = input().lower()

    if confirmacao == "s":
        cursor.execute(sql, (id_livro,))
        conexao.commit()
        console.print("Livro excluído com sucesso.", style="bold green")
    else:
        console.print("Operação de exclusão cancelada.", style="bold red")


def reorder():
    sql = "SELECT * FROM livros ORDER BY id"
    cursor.execute(sql)
    livros = cursor.fetchall()

    for index, livro in enumerate(livros, start=1):
        sql_update = "UPDATE livros SET id = %s WHERE id = %s"
        cursor.execute(sql_update, (index, livro[0]))
    
    conexao.commit()


# Funções de Pesquisa Simples e Avançadas de livros

def pesquisar_livro_por_titulo():
    titulo = input("Digite o título do livro que deseja pesquisar: ")
    sql = "SELECT * FROM livros WHERE titulo ILIKE %s"
    cursor.execute(sql, (f"%{titulo}%",))
    resultados = cursor.fetchall()

    if resultados:
        console.print("Resultados da pesquisa por título:", style="bold blue")
        for livro in resultados:
            console.print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Categoria ID: {livro[4]}", style="green")
    else:
        console.print("Nenhum livro encontrado com esse título.", style="bold red")


def pesquisar_livro_por_autor():
    autor = input("Digite o autor do livro que deseja pesquisar: ").lower()
    sql = "SELECT * FROM livros WHERE autor ILIKE %s"
    cursor.execute(sql, (f"%{autor}%",))
    resultados = cursor.fetchall()

    if resultados:
        console.print("Resultados da pesquisa por autor:", style="bold blue")
        for livro in resultados:
            console.print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Categoria ID: {livro[4]}", style="green")
    else:
        console.print("Nenhum livro encontrado com esse autor.", style="bold red")


def pesquisar_livro_por_categoria():
    cat.listar()  # Exibe a lista de categorias
    categoria_id = input("Digite o ID da categoria que deseja pesquisar: ")
    sql = "SELECT * FROM livros WHERE categoriaId = %s"
    cursor.execute(sql, (categoria_id,))
    resultados = cursor.fetchall()

    if resultados:
        console.print("Resultados da pesquisa por categoria:", style="bold blue")
        for livro in resultados:
            console.print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Categoria ID: {livro[4]}", style="green")
    else:
        console.print("Nenhum livro encontrado nessa categoria.", style="bold red")