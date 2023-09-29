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

btn_logout = ElevatedButton(
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
                    back_button
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
                    btn_logout,
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
        btn_editar_perfil.on_click = self.btn_editar_perfil
        btn_editar_rotas.on_click = self.btn_editar_rotas
        btn_editar_veiculos.on_click = self.btn_editar_veiculos
        btn_logout.on_click = self.btn_logout_clicked
        tela = telaPerfil(self)
        return tela
    
    
    def btn_editar_perfil(self, e):
        pass
    
    
    def btn_editar_veiculos(self, e):
        pass
    
    
    def btn_editar_rotas(self, e):
        pass
    
    
    def btn_logout_clicked(self, e):
        self.page.go('/login')