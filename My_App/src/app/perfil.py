from flet import *
from modules.SQLiteDB import *
from modules.FacadeBD import *
from modules.UI import *


icone_perfil = CircleAvatar(
                foreground_image_url = "My_App/assets/images/logo.png",
                content = Text("VOCÊ"),
                radius = 100,
            )

txt_name = Text(
                "Lorem Ipsum",
                color = colorBackground,
                size = 25,
                weight = FontWeight.BOLD,
            )

txt_email = Text(
                "palceholder@email.com",
                color = colorBackground,
                size = 25
            )

txt_veiculos = Text(
                "0 veículo(s)",
                color = colorBackground,
                size = 20
            )

btn_editar_perfil = ElevatedButton(
    content = Row(
        [
            Icon(name = icons.EDIT_ROUNDED, color = colorBackground, size =20),
            Text("EDITAR PERFIL", color = colorBackground, size = 20),
        ],
    ),
    style = botaoPadraoPerfil,
    bgcolor = colors.TRANSPARENT,
)

btn_editar_veiculos = ElevatedButton(
    content = Row(
        [
            Icon(name = icons.ELECTRIC_CAR_ROUNDED, color = colorBackground, size =20),
            Text("MEUS VEÍCULOS", color = colorBackground, size =20),
        ],
    ),
    style = botaoPadraoPerfil,        
    bgcolor = colors.TRANSPARENT,
)

btn_editar_rotas = ElevatedButton(
    content = Row(
        [
            Icon(name = icons.CHECKLIST_ROUNDED, color = colorBackground, size =20),
            Text("PREFERÊNCIAS DE ROTAS", color = colorBackground, size =20),
        ],
    ),                    
    style = botaoPadraoPerfil,
    bgcolor = colors.TRANSPARENT,
)

btn_logout = ElevatedButton(
    content = Row(
        [
            Icon(name = icons.EXIT_TO_APP_ROUNDED, color = colorBackground, size =20),
            Text("SAIR", color = colorBackground, size =20),
        ],
    ),                       
    style = botaoPadraoPerfil,
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
        back_button.on_click = self.btn_back
        btn_editar_perfil.on_click = self.btn_editar_perfil
        btn_editar_rotas.on_click = self.btn_editar_rotas
        btn_editar_veiculos.on_click = self.btn_editar_veiculos
        btn_logout.on_click = self.btn_logout_clicked
        self.setup_perfil()
        tela = telaPerfil(self)
        return tela
    
    
    def setup_perfil(self):
        id = self.page.session.get('user_id')
        
        results = get_profile(id[0][0])
        user_name, user_email = results[0]
        txt_email.value = user_email
        txt_name.value = user_name
        
        results = get_vehicle_count(id[0][0])
        veiculos = results[0][0]
        txt_veiculos.value = f"{veiculos} veículo"
        if veiculos != 1:
            txt_veiculos.value += 's'
    
    def btn_back(self, e):
        self.page.go('/home')
    
    def btn_editar_perfil(self, e):
        pass
    
    
    def btn_editar_veiculos(self, e):
        self.page.go('/meusVeiculos')
    
    
    def btn_editar_rotas(self, e):
        pass
    
    
    def btn_logout_clicked(self, e):
        self.page.go('/login')