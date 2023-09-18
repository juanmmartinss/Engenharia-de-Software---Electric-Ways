from flet import *


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



class Cadastro(UserControl):
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
                TextField(label = "E-mail", 
                        bgcolor = colors.TRANSPARENT, 
                        border_color = colors.WHITE, 
                        border_width = 1,
                        prefix_icon = "mail_outline_rounded",
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
                        prefix_icon = "lock_outline_rounded",
                        can_reveal_password = True,
                        border_radius = 20,
                        width = 320,
                        text_size= 9),
                alignment = alignment.center        
            
            ),

            Container(
                TextField(label = "Confirmar senha",
                        bgcolor = colors.TRANSPARENT,
                        border_color = colors.WHITE, 
                        border_width = 1,
                        password = True,
                        prefix_icon = "lock_outline_rounded",
                        can_reveal_password = True,
                        border_radius = 20,
                        width = 320,
                        text_size= 9),
                alignment = alignment.center        
            
            ),
            Container(
                Row(
                    [
                        
                    Checkbox(),

                    Text("Eu li e aceito os", size = 14, color = colors.WHITE),


                    Container(
                        TextButton(
                            content = Container(
                            Text(value = "Termos e Condições", size = 14, color = colors.WHITE)
                            )
                        ),
                    ),


                    ],
                    spacing = 0, 
                    alignment = MainAxisAlignment.START,
                    
                ),
                margin = margin.only(left = 30, top = 10)
            ),
        


            Container(
                ElevatedButton(
                    content = Container(
                        Text(value = "  Cadastrar  ", size = 30),
                        ),
                        style = botaoPadrao,
                    ),

                alignment = alignment.center,
                margin = margin.only(top = 10)
            ),
            
            Container(
                TextButton(
                    content = Container(
                    Text(value = "Entrar", 
                         size = 20, 
                         style = ButtonStyle('underline'),
                         color = colors.WHITE)
                    ),

                    on_click = lambda _: self.page.go('/login')
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
