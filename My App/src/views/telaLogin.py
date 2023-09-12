import flet as ft

def main(page: ft.page):

    background = ft.Container(
        bgcolor = '#020c2b',
        width = 500,
        height = 500
        )

    page.add(background)

ft.app(target=main)       