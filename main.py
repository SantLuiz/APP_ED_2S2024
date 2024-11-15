import flet as ft
import sqlite3
import tempfile
import time
from algoritmos.Ordenadores import *
from algoritmos.manipulador import *

bubble = BubbleSort()
quick = QuickSort()
insertion = InsertionSort()
merge = MergeSort()
manipula = Manipulador()

def buscar_todas_imagens():
    conn = sqlite3.connect('Satelite.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM images")
    results = cursor.fetchall()
    conn.close()
    return [list(result) for result in results]

def main(page: ft.Page):
    page.title = "APS Estrutura de Dados - 2 Sem 2024"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  

    botao_limpar = ft.IconButton(
        icon=ft.icons.DELETE_SWEEP_ROUNDED,
        icon_color=ft.colors.RED,
        tooltip="Limpar Histórico",
        on_click=lambda e: limpar_texto_drawer()  # Chama a função para limpar o drawer
    )

    # Drawer para exibir as estatísticas e o algoritmo executado
    drawer = ft.NavigationDrawer(
        position=ft.NavigationDrawerPosition.END,
        controls=[
            ft.Container(height=12),
            ft.Container(
                content=ft.Text(
                    "ESTATÍSTICAS GERAIS DA ORDENAÇÃO",
                    text_align="center",
                    weight="bold"
                ),
                alignment=ft.alignment.center,
                padding=10,
                border=ft.border.all(1, ft.colors.GREY),
                border_radius=8,
            ),
            ft.Container(height=12),
            ft.Divider(thickness=2),
            botao_limpar,
            ft.Divider(thickness=2)
        ],  
    )


    def adicionar_algoritmo_executado(tempo):
        drawer.controls.append(
            ft.Text(
                f"""Algoritmo Executado: {lista.value}
Tempo para ordenação: {tempo}
""",
                text_align="center",
                weight="bold", selectable=True
            )
    )
    def limpar_texto_drawer():
        drawer.controls = drawer.controls[:6] 
        page.update()

    page.update()
    galeria = ft.GridView(
        expand=1,
        runs_count=10,
        child_aspect_ratio=1.0,
        spacing=0,
        run_spacing=0
    )

    dadoimagem = buscar_todas_imagens()
    dadoimagem = manipula.embaralhar(dadoimagem)

    def addimggrid():
        nonlocal dadoimagem
        galeria.controls.clear()
        
        if not dadoimagem:
            page.add(ft.Text("Nenhuma imagem encontrada no banco de dados."))
        else:
            for i in range(len(dadoimagem)):
                if dadoimagem[i][3]:
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
                        tmp_file.write(dadoimagem[i][3])
                        tmp_file_path = tmp_file.name
                    galeria.controls.append(
                        ft.Image(
                            src=tmp_file_path, 
                            width=50, 
                            height=50, 
                            tooltip=f"Lat:{dadoimagem[i][1]} | Long: {dadoimagem[i][2]} | ID: {dadoimagem[i][0]}",
                            fit=ft.ImageFit.FILL,
                        )
                    )
        page.update()

    def btnordena(e):
        nonlocal dadoimagem
        start_time = time.time()

        match (lista.value):
            case "BUBBLE SORT": 
                dadoimagem = bubble.OrdenarColunas(dadoimagem)
            case "QUICKSORT":
                dadoimagem = quick.Ordenar(dadoimagem)
            case "MERGE SORT":
                dadoimagem = merge.Ordenar(dadoimagem)
            case "INSERTION SORT":
                dadoimagem = insertion.Ordenar(dadoimagem)

        end_time = time.time()  
        execution_time = end_time - start_time

        adicionar_algoritmo_executado(execution_time)
        addimggrid()
        

    def btnembaralha(e):
        nonlocal dadoimagem
        dadoimagem = manipula.embaralhar(dadoimagem)
        addimggrid()

    toggle_button = ft.IconButton(
        icon=ft.icons.DASHBOARD,
        icon_color=ft.colors.BLUE,
        on_click=lambda e: page.open(drawer),
        tooltip="ESTATISTICAS"
    )

    ordena = ft.IconButton(
        icon=ft.icons.CHANGE_CIRCLE_OUTLINED,
        icon_color=ft.colors.GREEN_600,
        on_click=btnordena,
        tooltip="ORDENAR"
    )

    embaralha = ft.IconButton(
        icon=ft.icons.REFRESH_ROUNDED,
        icon_color=ft.colors.RED_600,
        on_click=btnembaralha,
        tooltip="EMBARALHAR"
    )

    lista = ft.Dropdown(
        label="Algoritmo",
        options=[
            ft.dropdown.Option("BUBBLE SORT"),
            ft.dropdown.Option("INSERTION SORT"),
            ft.dropdown.Option("MERGE SORT"),
            ft.dropdown.Option("QUICKSORT")
        ],
        width=180,
        value="BUBBLE SORT",
    )

    menu = ft.Column([
        ft.Row([toggle_button, ordena, embaralha, lista]),
        ft.Divider(height=1, thickness=1),
    ])

    imagens = ft.Column([
        ft.Row([galeria])
    ], scroll=True, expand=True)

    page.add(menu, imagens)
    addimggrid()
    
ft.app(target=main)
