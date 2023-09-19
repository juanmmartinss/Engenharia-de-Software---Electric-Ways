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


body = Container(
    
    Column([
        Container(
            Image(
                src = "https://i.ibb.co/VtsLycp/logo-without-bg.png",
                scale=0.8,
                height = 300,
            ),
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
                        text_size= 15,
                        color = colors.WHITE,
                        
                    ),
                alignment = alignment.center,

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
                        text_size= 15,
                        color = colors.WHITE
                        ),
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
                padding = padding.only(top = 40),
            ),
            
            Container(
                TextButton(
                    content = Container(
                    Text(value = "Cadastre-se", size = 20, color = colors.WHITE)
                    )
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
    
    padding = 0,
)


def main(page: Page):

    page.padding = 0
    
    page.add(
       body
    )


        
app(target=main, assets_dir="assets")