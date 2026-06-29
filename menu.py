import interface as ui
from crud import categorias as cat
from crud import livros as liv
from services import backup as bkp
from services import graficos as grf
from services.html import gerar_pagina

from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
import time

console = Console()

# menu principal
def menu():
    while True:
        ui.limpar()
        ui.titulo("Sistema Biblioteca")
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
            ui.sucesso(" Acessando página web...")
            time.sleep(1)
            gerar_pagina()
            ui.pausa()
        elif opcao == "5":
            ui.sucesso(" Exibindo gráficos...")
            grf.exibir_dashboard()
            ui.pausa()
        elif opcao == "6":
            console.print("Realizando backup da base de dados...", style="italic magenta")
            bkp.backup_json()
            time.sleep(2) 
            ui.sucesso(" Backup realizado com sucesso!")
            ui.pausa()
        elif opcao == "7":
            #console.print("Saindo...", style="bold red")
            ui.aviso(" Saindo do sistema...")
            time.sleep(1)
            exit()  
        else:
            ui.erro(" Opção inválida!")

# submenu de categorias
def menu_categorias():

    while True:
        ui.limpar()
        ui.titulo("Sistema Biblioteca")
        console.print("Menu Categorias:", style="bold blue")
        console.print("1. Cadastrar categoria", style="bold green")
        console.print("2. Listar categorias", style="bold green")
        console.print("3. Alterar categoria", style="bold green")
        console.print("4. Excluir categoria", style="bold green")
        console.print("5. Voltar", style="red")

        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2", "3", "4", "5"])

        if opcao == "1":
            cat.cadastrar()
            ui.sucesso(" Categoria cadastrada com sucesso.")
            ui.pausa()       
        elif opcao == "2":
            cat.listar()
            ui.pausa()
        elif opcao == "3":
            cat.alterar()
            ui.sucesso(" Categoria alterada com sucesso.")
            ui.pausa()
        elif opcao == "4":
            cat.excluir()
            ui.sucesso(" Categoria excluída com sucesso.")
            ui.pausa()
        elif opcao == "5":
            break
        else:
            ui.erro(" Opção inválida!")

# submenu de livros
def menu_livros():
    while True:
        ui.limpar()
        ui.titulo("Sistema Biblioteca")
        console.print("Menu Livros:", style="bold blue")
        console.print("1. Cadastrar livro", style="bold green")
        console.print("2. Listar livros", style="bold green")
        console.print("3. Alterar livro", style="bold green")
        console.print("4. Excluir livro", style="bold green")
        console.print("5. Voltar", style="red")

        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2", "3", "4", "5"])

        if opcao == "1":
            console.print("Cadastrar livro", style="bold blue")
            liv.cadastrar()
        elif opcao == "2":
            console.print("Listar livros", style="bold blue")
            liv.listar()
            ui.pausa()
        elif opcao == "3":
            console.print("Alterar livro", style="bold blue")
            liv.alterar()
            ui.sucesso(" Livro alterado com sucesso.")
            ui.pausa()
        elif opcao == "4":
            console.print("Excluir livro", style="bold blue")
            liv.excluir()
            ui.sucesso(" Livro excluído com sucesso.")
            ui.pausa()
        elif opcao == "5":
            break
        else:
            ui.erro(" Opção inválida!")



# submenu de pesquisa
def menu_pesquisa():
    while True:
        ui.limpar()
        ui.titulo("Sistema Biblioteca")
        console.print("Menu Pesquisa:", style="bold blue")
        console.print("1. Pesquisar livro por título", style="bold green")
        console.print("2. Pesquisar livro por autor", style="bold green")
        console.print("3. Pesquisar livro por categoria", style="bold green")
        console.print("4. Pesquisar categoria por nome", style="bold green")
        console.print("5. Pesquisa avançada", style="bold blue")
        console.print("6. Voltar", style="red")

        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2", "3", "4", "5", "6"])

        if opcao == "1":
            liv.pesquisar_livro_por_titulo()
            ui.pausa()
        elif opcao == "2":
            liv.pesquisar_livro_por_autor()
            ui.pausa()
        elif opcao == "3":
            liv.pesquisar_livro_por_categoria()
            ui.pausa()
        elif opcao == "4":
            cat.pesquisar_categoria_por_nome()
            ui.pausa()
        elif opcao == "5":
            liv.pesquisa_avancada()
            ui.pausa()
        elif opcao == "6":
            break
        else:
            ui.erro(" Opção inválida!")