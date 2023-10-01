from flet import *
from modules.SQLiteDB import *
from modules.ManageDB import *
from modules.UI import *


txt_name = Text(
                "Meus Veículos",
                color = colorBackground,
                size = 25,
                weight = FontWeight.BOLD,
            )



def destino(self):
    return ResponsiveRow(
        [
            Column(
                [
                    back_button
                ],
                horizontal_alignment=CrossAxisAlignment.START
            ),           
        ]
    )



class SearchDestination(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        
    def build(self):
        tela = destino(self)
        return tela