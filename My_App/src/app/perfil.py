from flet import *
from modules.SQLiteDB import *
from modules.ManageDB import *
from modules.UI import *

icone_perfil = CircleAvatar(
                foreground_image_url = "My_App/assets/images/logo.png",
                content = Text("VOCÊ"),
                radius = 40,
            )

txt_name = Text(
                "fabio fagundes",
                color = colorBackground,
                size = 15,
                weight = FontWeight.BOLD,
            )

txt_email = Text(
                "fabio_fagundes@unifesp.br",
                color = colorBackground,
                size = 12
            )

txt_veiculos = Text(
                "69 veículos",
                color = colorBackground,
                size = 12
            )

btn_editar_perfil = ElevatedButton(
    content = Row(
        [
            Icon(name = icons.EDIT_ROUNDED, color = colorBackground),
            Text("EDITAR PERFIL", color = colorBackground),
        ],
    ),
    style = botaoPadrao,
    bgcolor = colors.TRANSPARENT,
)

btn_editar_veiculos = ElevatedButton(
    content = Row(
        [
            Icon(name = icons.ELECTRIC_CAR_ROUNDED, color = colorBackground),
            Text("MEUS VEÍCULOS", color = colorBackground),
        ],
    ),
    style = botaoPadrao,        
    bgcolor = colors.TRANSPARENT,            
)

btn_editar_rotas = ElevatedButton(
    content = Row(
        [
            Icon(name = icons.CHECKLIST_ROUNDED, color = colorBackground),
            Text("PREFERÊNCIAS DE ROTAS", color = colorBackground),
        ],
    ),                    
    style = botaoPadrao,
    bgcolor = colors.TRANSPARENT,
)

btn_sair = ElevatedButton(
    content = Row(
        [
            Icon(name = icons.EXIT_TO_APP_ROUNDED, color = colorBackground),
            Text("SAIR", color = colorBackground),
        ],
    ),                       
    style = botaoPadrao,
    bgcolor = colors.TRANSPARENT,
)

def telaPerfil(self):
    return ResponsiveRow(
        [
            Column(
                [
                    IconButton(
                        icon = icons.ARROW_BACK_IOS_NEW_ROUNDED,
                        icon_color = colorBackground,
                        icon_size = 20,
                        tooltip = "Voltar",
                        on_click = lambda _: self.page.go('/home'),
                    ),
                ],
                horizontal_alignment=CrossAxisAlignment.START
            ),

            Column(
                [
                    icone_perfil,
                    txt_name,
                    txt_email,
                    txt_veiculos,
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),

            Column([
                    btn_editar_perfil,
                    btn_editar_veiculos,
                    btn_editar_rotas,
                    btn_sair,
                ],
                horizontal_alignment=CrossAxisAlignment.STRETCH,
            ),
        ]
    )


class Perfil(UserControl):

    def __init__(self, page):
        super().__init__()
        self.page = page


    def build(self):
        tela = telaPerfil(self)
        return tela
    
