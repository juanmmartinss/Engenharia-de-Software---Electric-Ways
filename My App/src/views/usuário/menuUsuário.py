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
        bgcolor = colors.TRANSPARENT, 
        padding = {MaterialState.DEFAULT: 30}, #Tamanho
        overlay_color = colors.BLUE_200, #Cor quando seleciona
        shape = {MaterialState.DEFAULT: RoundedRectangleBorder(radius=20)},
        
    )


body = Container(
    
    Column(
        [
        # MenuDetail(),
        
        Container(

            IconButton(
                icon = icons.ARROW_BACK_IOS_NEW_ROUNDED,
                icon_color = colors.WHITE,
                icon_size = 40,
                tooltip = "Voltar"
            ),
            margin = margin.only(top = 15)
        ),

        Container(

            CircleAvatar(
                foreground_image_url = "https://i.ibb.co/mSBPMYc/avatar.png",
                content = Text("VOCÊ"),
                radius = 90,
            ),

            alignment = alignment.center,
        ),

                Container(

            Text(
                "FULANO DE TAL",
                color = colors.WHITE,
                size = 23,
                weight = FontWeight.BOLD,
            ),

            alignment = alignment.center,
        ),

        Container(

            Text(
                "email@email.com - 1 veículos",
                color = colors.WHITE,
                size = 16
            
            ),

            alignment = alignment.center,
        ),

        Container(
            Column([
                ElevatedButton(

                    text = "EDITAR PERFIL                                                   ",

                    icon = "EDIT_ROUNDED",
                    style = botaoPadrao,


                ),

                ElevatedButton(

                    text = "MEUS VEÍCULOS                                                ",

                    icon = "ELECTRIC_CAR_ROUNDED",
                    style = botaoPadrao,


                ),

                ElevatedButton(

                    text = "PREFERÊNCIAS DE ROTAS                              ",

                    icon = "CHECKLIST_ROUNDED",
                    style = botaoPadrao,


                ),


                ElevatedButton(

                    text = "SAIR                                                                        ",

                    icon = "EXIT_TO_APP_ROUNDED",
                    style = botaoPadrao,


                ),


            ]),


            margin = margin.symmetric(vertical = 30, horizontal = 40),
            #alignment= alignment.center,
        
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