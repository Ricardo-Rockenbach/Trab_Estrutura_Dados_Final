from database import conexao
from rich.console import Console

console = Console()

cursor, conexao = conexao()

def cadastrar():
    sql = "INSERT INTO categoria (nome) VALUES (%s)"
    nome = input("Digite o nome da categoria: ")
    cursor.execute(sql, (nome,))
    conexao.commit()

def listar():
    sql = "SELECT * FROM categoria ORDER BY id"
    cursor.execute(sql)

    for categoria in cursor.fetchall():
        console.print(f"ID: {categoria[0]}, Nome da Categoria: {categoria[1]}", style="green")

def alterar():
    console.print("Alterar categoria", style="bold blue")
    listar()

    id_categoria = input("Digite o ID da categoria que deseja alterar: ")
    nome = input("Digite o novo nome da categoria: ")
    
    if id_categoria == "":
        console.print("ID inválido. Operação cancelada.", style="bold red")
        return
    if nome == "":
        sql = "SELECT nome FROM categoria WHERE id = %s"
        cursor.execute(sql, (id_categoria,))
        nome = cursor.fetchone()[0]

    sql_update = "UPDATE categoria SET nome = %s WHERE id = %s"
    cursor.execute(sql_update, (nome, id_categoria))
    conexao.commit()

def excluir():
    console.print("Excluir categoria", style="bold blue")
    listar()

    id_categoria = input("Digite o ID da categoria que deseja excluir: ")
    quantidade_livros_sql = "SELECT COUNT(*) FROM livros WHERE categoriaId = %s"
    cursor.execute(quantidade_livros_sql, (id_categoria,))
    quantidade_livros = cursor.fetchone()[0]
    sql = "DELETE FROM categoria WHERE id = %s"

    if id_categoria == "":
        console.print("ID inválido. Operação cancelada.", style="bold red")
        return
    
    if quantidade_livros > 0:
        console.print("Não é possível excluir uma categoria que possui livros associados.", style="bold red")
        console.print(f"Existem {quantidade_livros} livro (s) associados a esta categoria.", style="bold red")
        return

    cursor.execute(sql, (id_categoria,))
    conexao.commit()


def reorder():
    sql = "SELECT * FROM categoria ORDER BY id"
    cursor.execute(sql)
    categorias = cursor.fetchall()

    for index, categoria in enumerate(categorias, start=1):
        sql_update = "UPDATE categoria SET id = %s WHERE id = %s"
        cursor.execute(sql_update, (index, categoria[0]))
    
    conexao.commit()


# Função para pesquisar categorias por nome:
def pesquisar_categoria_por_nome():
    nome = input("Digite o nome da categoria que deseja pesquisar: ")
    sql = "SELECT * FROM categoria WHERE nome ILIKE %s"
    cursor.execute(sql, (f"%{nome}%",))
    resultados = cursor.fetchall()

    if resultados:
        console.print("Resultados da pesquisa:", style="bold blue")
        for categoria in resultados:
            console.print(f"ID: {categoria[0]}, Nome da Categoria: {categoria[1]}", style="green")
    else:
        console.print("Nenhuma categoria encontrada com esse nome.", style="bold red")