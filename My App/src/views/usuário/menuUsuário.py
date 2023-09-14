from flet import *
import flet as ft
# class MenuDetail(UserControl):
#     def  build(self):
#         return self.menu

# def create_button(text, color):

colorBackground = '#00001E'
colorBackground2 = '#1e19a8'

botaoPadrao = ButtonStyle(
        color = {MaterialState.DEFAULT: colors.WHITE}, #Estado(clicando, default, selecionando, etc),
        bgcolor = colorBackground, 
        padding = {MaterialState.DEFAULT: 6}, #Tamanho
        overlay_color = colors.BLUE_200, #Cor quando seleciona
        side = {MaterialState.DEFAULT: BorderSide(2, colors.WHITE)}, #Borda do botao
        shape = {MaterialState.DEFAULT: RoundedRectangleBorder(radius=20)},
        
    )


body = Container(
    
    Column(
        [
        # MenuDetail(),

        IconButton(
            icon = icons.ARROW_BACK_IOS_NEW_ROUNDED,
            icon_color = colors.WHITE,
            icon_size = 40,
            tooltip = "Voltar"
        ),

        Container(
            CircleAvatar(
                foreground_image_url = "https://ibb.co/kMyPWrS",
                content = Text("VOCÊ"),
                radius = 90,

            ),
            alignment = alignment.center,
        ),
        
    ]
    ),
    
    gradient= LinearGradient(
        begin=alignment.top_left,
        end=alignment.bottom_right,
        colors=[colorBackground, colorBackground2],
    ), 
    
    width=500,
    height=800,
)


def main(page: Page):

    page.window_max_height = 800
    page.window_width = 500
    page. window_max_width = 500
    page.window_height = 800
    
    page.padding = 0
    
    page.add(
        body
    )
    
        
app(target=main, assets_dir="assets")