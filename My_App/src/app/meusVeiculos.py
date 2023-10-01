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
            Row(
                [
                    cardVeiculos, cardVeiculos,
                ],
                alignment=MainAxisAlignment.CENTER,
            ),            
        ]
    )



class MeusVeiculos(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        
    def build(self):
        back_button.on_click = self.btn_back
        tela = telaPerfil(self)
        return tela
    
    def btn_back(self, e):
        self.page.go('/perfil')