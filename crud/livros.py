from database import conexao
from crud import categorias as cat
from rich.console import Console
import interface as ui

console = Console()

cursor, conexao = conexao()

def cadastrar():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação do livro (opcional): ") or None
    cat.listar()  # Exibe a lista de categorias
    categoria_id = int(input("Digite o ID da categoria: "))
    
    cursor.execute(
        "SELECT id FROM categoria WHERE id = %s",
        (categoria_id,)
    )

    if cursor.fetchone() is None:
        ui.erro(" ID de categoria inválido.")
        ui.aviso(" Operação de cadastro cancelada.")
        ui.pausa()
        return
    
    categoriaId = categoria_id if categoria_id else None  # Permite que categoriaId seja nulo

    console.print(f"Título: {titulo}", style="green")
    console.print(f"Autor: {autor}", style="green")
    console.print(f"Ano: {ano}", style="green")

    console.print(f"Categoria: {categoria_id} ({type(categoria_id)})", style="green")


    input("Pressione Enter para confirmar o cadastro...")

    sql = "INSERT INTO livros (titulo, autor, ano, categoriaId) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (titulo, autor, ano, categoriaId))
    conexao.commit()


def listar():
    sql = "SELECT * FROM livros"
    cursor.execute(sql)

    for livro in cursor.fetchall():
        console.print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Categoria ID: {livro[4]}", style="green")


def alterar():

    listar()

    id_livro = input("Digite o ID do livro que deseja alterar: ")

    if id_livro == "":
        ui.erro(" ID inválido. Operação cancelada.")
        return
    
    # Buscar dados atuais do livro selecionado
    sql_livro = "SELECT titulo, autor, ano FROM livros WHERE id = %s"
    cursor.execute(sql_livro, (id_livro,))
    livro_atual = cursor.fetchone()

    if livro_atual is None:
        ui.erro(" Livro não encontrado.")
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

    ui.sucesso(" Livro alterado com sucesso.")


def excluir():

    listar()

    id_livro = input("Digite o ID do livro que deseja excluir: ")
    livro_selecionado_sql = "SELECT titulo FROM livros WHERE id = %s"
    cursor.execute(livro_selecionado_sql, (id_livro,))

    sql = "DELETE FROM livros WHERE id = %s"

    if id_livro == "":
        ui.erro(" ID inválido. Operação cancelada.")
        return
    
    livro_selecionado = cursor.fetchone()
    ui.aviso(f"Confirma a exclusão do Livro {livro_selecionado[0]} de ID {id_livro}? (s/n)")
    confirmacao = input().lower()

    if confirmacao == "s":
        cursor.execute(sql, (id_livro,))
        conexao.commit()
        ui.sucesso(" Livro excluído com sucesso.")
    else:
        ui.aviso(" Operação de exclusão cancelada.")
        


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
        ui.erro(" Nenhum livro encontrado com esse título.")


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
        ui.erro(" Nenhum livro encontrado com esse autor.")


def pesquisar_livro_por_categoria():
    cat.listar()  # Exibe a lista de categorias
    
    categoria_id = input("Digite o ID da categoria que deseja pesquisar: ")
    
    try:   
        sql = "SELECT * FROM livros WHERE categoriaId = %s"
        cursor.execute(sql, (categoria_id,))
        resultados = cursor.fetchall()
    

        if resultados:
            console.print("Resultados da pesquisa por categoria:", style="bold blue")
            for livro in resultados:
                console.print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Categoria ID: {livro[4]}", style="green")
        else:
            ui.erro(" Nenhum livro encontrado nessa categoria.")
    
    except Exception as e:
        ui.erro(f" Erro ao pesquisar livros pela categoria. Verifique o ID da categoria e tente novamente.\nDetalhes do erro: {e}")


def pesquisa_avancada():
    console.print("Pesquisa Avançada de Livros", style="bold blue")
    console.print("Deixe o campo em branco se não quiser filtrar por esse critério.", style="green")

    titulo = input("Digite o título do livro (Enter para pular): ")
    autor = input("Digite o autor do livro (Enter para pular): ")
    ano = input("Digite o ano de publicação do livro (Enter para pular): ")
    cat.listar()  # Exibe a lista de categorias
    categoria_id = input("Digite o ID da categoria (Enter para pular): ")

    sql = "SELECT * FROM livros WHERE 1=1"
    params = []

    if titulo:
        sql += " AND titulo ILIKE %s"
        params.append(f"%{titulo}%")
    if autor:
        sql += " AND autor ILIKE %s"
        params.append(f"%{autor}%")
    if ano:
        sql += " AND ano = %s"
        params.append(ano)
    if categoria_id:
        sql += " AND categoriaId = %s"
        params.append(categoria_id)

    cursor.execute(sql, tuple(params))
    resultados = cursor.fetchall()

    if resultados:
        ui.sucesso(" Resultados da pesquisa avançada:")
        for livro in resultados:
            console.print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Categoria ID: {livro[4]}", style="green")
    else:
        ui.erro(" Nenhum livro encontrado com os critérios fornecidos.")