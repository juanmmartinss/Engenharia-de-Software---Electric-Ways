from flet import *
from modules.SQLiteDB import *
from modules.FacadeBD import *
from modules.UI import *


txt_busca = TextField(
                hint_text="Pesquise aqui",
                hint_style=TextStyle(color=colors.GREY),
                bgcolor = colors.TRANSPARENT, 
                border_color = colors.GREY, 
                border_width = 1,
                prefix_icon = "search_rounded",
                border_radius = 20,
                text_size = 15,
                color = colors.GREY,
                col = {"md": 4}
            )

txt_recentes = Text(
                "Recentes",
                color = colorBackground,
                size = 18,
                weight = FontWeight.BOLD,
            )

infoButton = Container(
    IconButton(
        icon = icons.INFO_ROUNDED,
        icon_color = colorBackground,
        icon_size = 20,
        tooltip = "Ajuda e Informações"
    ),
)


def destino(self):
    return ResponsiveRow(
        [
            Column(
                [
                    back_button
                ],
            ),
            Column(
                [
                    txt_busca
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
            Row(
                [
                    txt_recentes,
                    infoButton
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            ),
            Column(
                [
                    cardRecentes, cardRecentes,cardRecentes,cardRecentes,cardRecentes, cardRecentes,cardRecentes
                ]
                
            ),
            
        ]
    )



class SearchDestination(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        
    def build(self):
        back_button.on_click = self.btn_back
        tela = destino(self)
        return tela
    
    def btn_back(self, e):
        self.page.go('/home')