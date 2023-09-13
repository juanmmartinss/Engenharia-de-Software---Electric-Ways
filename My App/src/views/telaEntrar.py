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
                scale=0.5,
                height = 250,
            )
        ), 

        Column([

            Container(
                TextField(label = "Usuário", 
                        bgcolor = colors.TRANSPARENT, 
                        border_color = colors.WHITE, 
                        border_width = 1,
                        prefix_icon = "person_rounded",
                        border_radius = 20,
                        width = 320),
                alignment = alignment.center

            ),

            Container(
                TextField(label = "Senha",
                        bgcolor = colors.TRANSPARENT,
                        border_color = colors.WHITE, 
                        border_width = 1,
                        password = True,
                        can_reveal_password = True,
                        prefix_icon = "lock_rounded",
                        border_radius = 20,
                        width = 320),
                alignment = alignment.center        
            
            ),

            Container(
                TextButton(
                    content = Container(
                    Text(value = "Esqueceu a senha?", size = 15, color = colors.WHITE)
                    )
                ),
                margin = margin.only(left = 35)
            ),


            Container(
                ElevatedButton(
                    content = Container(
                        Text(value = "    Entrar     ", size = 35),
                        ),
                        style = botaoPadrao,
                    ),

                alignment = alignment.center,
                margin = margin.only(top = 70)
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