from util import limpar_tela
from crud import categorias as cat
from crud import livros as liv
from services import backup as bkp
from services import graficos as grf

from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
import time

console = Console()

# menu principal
def menu():
    while True:
        limpar_tela()
        console.print("Menu Principal:", style="bold blue")
        console.print("1. Categorias", style="bold green")
        console.print("2. Livros", style="bold green")
        console.print("3. Pesquisar", style="italic blue")
        console.print("4. Acessar Página Web", style="italic magenta")
        console.print("5. Exibir Gráficos", style="italic magenta")
        console.print("6. Realizar Backup da Base de Dados", style="italic magenta")
        console.print("7. Sair", style="bold red")
        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2", "3", "4", "5", "6", "7"])

        if opcao == "1":
            menu_categorias()
        elif opcao == "2":
            menu_livros()
        elif opcao == "3":
            menu_pesquisa()
        elif opcao == "4":
            console.print("Acessando página web...", style="italic magenta")
            break  # Aqui você pode adicionar a lógica para abrir a página web
        elif opcao == "5":
            console.print("Exibindo gráficos...", style="italic magenta")
            grf.grafico_livros_categoria()
            input("Pressione Enter para continuar...")
        elif opcao == "6":
            console.print("Realizando backup da base de dados...", style="italic magenta")
            bkp.backup_json()
            input("Pressione Enter para continuar...")
        elif opcao == "7":
            console.print("Saindo...", style="bold red")
            exit()  
        else:
            console.print("Opção inválida!", style="bold red")

# submenu de categorias
def menu_categorias():

    while True:
        limpar_tela()
        console.print("Menu Categorias:", style="bold blue")
        console.print("1. Cadastrar categoria", style="bold green")
        console.print("2. Listar categorias", style="bold green")
        console.print("3. Alterar categoria", style="bold green")
        console.print("4. Excluir categoria", style="bold green")
        console.print("5. Reordenar Categorias", style="bold red")
        console.print("6. Voltar", style="bold green")

        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2", "3", "4", "5", "6"])

        if opcao == "1":
            cat.cadastrar()
        elif opcao == "2":
            cat.listar()
            if input("Pressione Enter para continuar..."):
                pass
        elif opcao == "3":
            cat.alterar()
        elif opcao == "4":
            cat.excluir()
            input("Pressione Enter para continuar...")
            pass
        elif opcao == "5":
            console.print("Reordenando categorias...", style="bold red")
            cat.reorder()
            time.sleep(2)  # Pausa para mostrar a mensagem antes de limpar a tela
        elif opcao == "6":
            break
        else:
            console.print("Opção inválida!", style="bold red")

# submenu de livros
def menu_livros():
    while True:
        limpar_tela()
        console.print("Menu Livros:", style="bold blue")
        console.print("1. Cadastrar livro", style="bold green")
        console.print("2. Listar livros", style="bold green")
        console.print("3. Alterar livro", style="bold green")
        console.print("4. Excluir livro", style="bold green")
        console.print("5. Reordenar livros", style="bold red")
        console.print("6. Voltar", style="bold green")

        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2", "3", "4", "5", "6"])

        if opcao == "1":
            liv.cadastrar()
        elif opcao == "2":
            liv.listar()
            input("Pressione Enter para continuar...")
        elif opcao == "3":
            liv.alterar()
        elif opcao == "4":
            liv.excluir()
        elif opcao == "5":
            console.print("Reordenando livros...", style="bold red")
            liv.reorder()
            time.sleep(2)  # Pausa para mostrar a mensagem antes de limpar a tela
        elif opcao == "6":
            break
        else:
            console.print("Opção inválida!", style="bold red")



# submenu de pesquisa
def menu_pesquisa():
    while True:
        limpar_tela()
        console.print("Menu Pesquisa:", style="bold blue")
        console.print("1. Pesquisar livro por título", style="bold green")
        console.print("2. Pesquisar livro por autor", style="bold green")
        console.print("3. Pesquisar livro por categoria", style="bold green")
        console.print("4. Pesquisar categoria por nome", style="bold green")
        console.print("5. Voltar", style="bold green")

        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2", "3", "4", "5"])

        if opcao == "1":
            liv.pesquisar_livro_por_titulo()
            input("Pressione Enter para continuar...")
        elif opcao == "2":
            liv.pesquisar_livro_por_autor()
            input("Pressione Enter para continuar...")
        elif opcao == "3":
            liv.pesquisar_livro_por_categoria()
            input("Pressione Enter para continuar...")
        elif opcao == "4":
            cat.pesquisar_categoria_por_nome()
            input("Pressione Enter para continuar...")
        elif opcao == "5":
            break
        else:
            console.print("Opção inválida!", style="bold red")