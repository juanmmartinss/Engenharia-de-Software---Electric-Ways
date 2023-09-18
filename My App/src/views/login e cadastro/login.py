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


class Login(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page

  def build(self):
    return Container(
    
    Column([
        # MenuDetail(),
        Container(
            Image(
                src = "https://i.ibb.co/VtsLycp/logo-without-bg.png",
                scale=0.8,
                height = 300,
            ),
            margin = margin.only(top = 30)
        ), 

        Column([

            Container(
                TextField(label = "Usuário", 
                        bgcolor = colors.TRANSPARENT, 
                        border_color = colors.WHITE, 
                        border_width = 1,
                        prefix_icon = "person_outline_rounded",
                        border_radius = 20,
                        width = 320,
                        text_size= 9),
                alignment = alignment.center

            ),

            Container(
                TextField(label = "Senha",
                        bgcolor = colors.TRANSPARENT,
                        border_color = colors.WHITE, 
                        border_width = 1,
                        password = True,
                        can_reveal_password = True,
                        prefix_icon = "lock_outline_rounded",
                        border_radius = 20,
                        width = 320,
                        text_size= 9),
                alignment = alignment.center        
            
            ),

            Container(
                TextButton(
                    content = Container(
                    Text(value = "Esqueceu a senha?", size = 14, color = colors.WHITE)
                    )
                ),
                margin = margin.only(left = 30)
            ),


            Container(
                ElevatedButton(
                    content = Container(
                        Text(value = "    Entrar     ", size = 30),
                        ),
                        style = botaoPadrao,
                    ),

                alignment = alignment.center,
                margin = margin.only(top = 70)
            ),
            
            Container(
                TextButton(
                    content = Container(
                    Text(value = "Cadastre-se", size = 20, color = colors.WHITE)
                    ),
                    on_click = lambda _: self.page.go('/cadastro')
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
