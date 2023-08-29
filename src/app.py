import flet as ft

# fazendo teste

def main(app: ft.page):

    app.title = "Eletric Ways"
    app.vertical_alignment = ft.MainAxisAlignment.CENTER

    titulo = ft.Text(value = "Eletric Ways", size = 20,  color = ft.colors.BLUE_600, text_align = ft.TextAlign.CENTER)

    img = ft.Image(
        src=f"\nike.png",
        width=100,
        height=1000,
        fit=ft.ImageFit.CONTAIN,
    )

    #app.add(img)

    app.theme_mode = ft.ThemeMode.LIGHT
    
    app.controls.append(titulo)

    app.update()

ft.app(target=main)