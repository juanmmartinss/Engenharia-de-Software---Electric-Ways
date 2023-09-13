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
        padding = {MaterialState.DEFAULT: 20}, #Tamanho
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
                scale=0.8,
                height = 400,
            )
        ), 
        Column([
            #BOTAO ENTRAR


            ElevatedButton(
                content = Container(
                    Text(value = "  Entrar   ", size = 25),
                    ),
                    style = botaoPadrao,
                ),
            
            ElevatedButton(
                content = Container(
                    Text(value = "Cadastrar", size = 25),
                ),
                style = botaoPadrao
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