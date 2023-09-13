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
        padding = {MaterialState.DEFAULT: 25}, #Tamanho
        overlay_color = colors.BLUE_200, #Cor quando seleciona
        side = {MaterialState.DEFAULT: BorderSide(2, colors.WHITE)}, #Borda do botao
        shape = {MaterialState.DEFAULT: RoundedRectangleBorder(radius=20)},
        
    )


body = Container(
    
    Column([
        # MenuDetail(),
        Container(
            Image(
                src = "logomudado.png",
                scale=0.7,
                height = 350,
            )
        ), 

        Column([

            Container(
                ElevatedButton(
                    content = Container(
                        Text(value = "    Entrar     ", size = 35),
                        ),
                        style = botaoPadrao,
                    ),

                alignment = alignment.center
            ),

            Container(
                ElevatedButton(
                    content = Container(
                        Text(value = "  Cadastrar  ", size = 35),
                    ),
                    style = botaoPadrao
                ),

                alignment = alignment.center
            )



        ])
    ]),
    
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
    
    #butto
    

        
app(target=main, assets_dir="assets")