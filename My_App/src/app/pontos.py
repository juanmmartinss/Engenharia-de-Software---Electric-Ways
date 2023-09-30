from flet import *
from modules.SQLiteDB import *
from modules.ManageDB import *
from modules.UI import *

txt_name = Text(
                "Pontos de Carregamento",
                color = colorBackground,
                size = 25,
                weight = FontWeight.BOLD,
            )

ordenar_button = PopupMenuButton(
    content = Row([
        Text("Ordenar por", color = colorBackground, size = 20),
        Icon(icons.CHANGE_CIRCLE_ROUNDED, color = colorBackground),
    ]),
    
    items = [
        PopupMenuItem(
            content = Text("Mais próximos"),
        ),
        PopupMenuItem(
            content = Text("Gratuito"),
        ),
        PopupMenuItem(
            content = Text("Vagas"),
        ),
    ],
)


def telaPerfil(self):
    return ResponsiveRow(
        [
            Column(
                [
                    back_button
                ],
                horizontal_alignment=CrossAxisAlignment.START
            ),

            Column(
                [
                    txt_name,
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
            
            Column(
                [
                    ordenar_button,
                    
                    #card_postos,
                ],
                horizontal_alignment=CrossAxisAlignment.START
            ),
            Column(
                [
                    card,card,card,card,
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
        ]
    )



class Pontos(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        
    def build(self):
        tela = telaPerfil(self)
        return tela