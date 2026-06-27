from crud import categorias as cat
from crud import livros as liv
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table

console = Console()

# menu principal
def menu():
    while True:
        console.print("Menu Principal:", style="bold blue")
        console.print("1. Categorias", style="bold green")
        console.print("2. Livros", style="bold green")
        console.print("3. Sair", style="bold green")

        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2", "3"])

        if opcao == "1":
            menu_categorias()
        elif opcao == "2":
            menu_livros()
        elif opcao == "3":
            break
        else:
            console.print("Opção inválida!", style="bold red")

# submenu de categorias
def menu_categorias():

    while True:
        console.print("Menu Categorias:", style="bold blue")
        console.print("1. Cadastrar categoria", style="bold green")
        console.print("2. Listar categorias", style="bold green")
        console.print("3. Alterar categoria", style="bold green")
        console.print("4. Excluir categoria", style="bold green")
        console.print("5. Voltar", style="bold green")

        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2", "3", "4", "5"])

        if opcao == "1":
            cat.cadastrar()
        elif opcao == "2":
            cat.listar()
        elif opcao == "3":
            cat.alterar()
        elif opcao == "4":
            cat.excluir()
        elif opcao == "5":
            break
        else:
            console.print("Opção inválida!", style="bold red")

# submenu de livros
def menu_livros():
    while True:
        console.print("Menu Livros:", style="bold blue")
        console.print("1. Cadastrar livro", style="bold green")
        console.print("2. Listar livros", style="bold green")
        console.print("3. Alterar livro", style="bold green")
        console.print("4. Excluir livro", style="bold green")
        console.print("5. Voltar", style="bold green")

        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2", "3", "4", "5"])

        if opcao == "1":
            liv.cadastrar()
        elif opcao == "2":
            liv.listar()
        elif opcao == "3":
            liv.alterar()
        elif opcao == "4":
            liv.excluir()
        elif opcao == "5":
            break
        else:
            console.print("Opção inválida!", style="bold red")
