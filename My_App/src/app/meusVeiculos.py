from flet import *
from modules.SQLiteDB import *
from modules.FacadeBD import *
from modules.UI import *

txt_name = Text(
                "Meus Veículos",
                color = colorBackground,
                size = 25,
                weight = FontWeight.BOLD,
            )

# --------------------------------------------------------------------- new cards for scroll
add_button = IconButton(
                icon = icons.ADD,
                icon_size = 20,
                icon_color = colorBackground,
                tooltip="Adicionar veículo",
            )
# -------------------------------------------------------------------------------------------------------


def telaPerfil(self):
    return ResponsiveRow(
        [
            Column(
                [
                     Row([
                          back_button,
                          add_button
                     ],
                     alignment=MainAxisAlignment.SPACE_BETWEEN
                     )
                ],
                horizontal_alignment=CrossAxisAlignment.START
            ),

            Column(
                [
                    txt_name,
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
            Container(
                padding = padding.only(top=20),
                content=Column([
                    Container(margin = margin.only(left=10)),
                    Row([], scroll="auto")
                    ])
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
        
        id = self.page.session.get('user_id')
        results = get_vehicles(id[0][0])
        for veic in results:
            nome, modelo, placa, cor, range = veic
            new_card = self.criar_card(nome, modelo, placa, cor, range)
            card_row = tela.controls[2].content.controls[1]
            card_row.controls.append(new_card)
        
        return tela
            
    
    def btn_back(self, e):
        self.page.go('/perfil')
        
        
    def criar_card(self, nome, modelo, placa, cor, range):
        return Card(
            elevation=20,
            content=Container(
            bgcolor="white",
            width=300,
            border_radius = border_radius.all(30),
            content=Column([
                ListTile(
                        leading = Icon(icons.ELECTRIC_CAR_ROUNDED, size = 50),
                        title = Text(modelo, size = 25),
                        subtitle = Text(f"Placa: {placa}", size = 20),
                        trailing = PopupMenuButton(
                            icon = icons.MORE_VERT,
                            items = [
                                PopupMenuItem(
                                    content = TextButton("Editar veículo"),
                                ),
                                PopupMenuItem(
                                    content = TextButton("Excluir veículo"),
                                ),
                                ],
                                
                            ),
                        ),
                Container(
                        padding = padding.all(10),
                        content=Column([
                        Text(f"Autonomia: {range}Km",size=16,weight="bold"),
                        Text(f"Cor: {cor}",size=13),
                        Row(
                            [
                            TextButton(
                                content = Container(
                                    Text(value = "Selecionar", size = 20, color = colors.BLACK),
                                    ),
                                col = {"md": 4}, 
                            ),
                            ],
                            alignment = MainAxisAlignment.CENTER,
                            ),
                        
                        ])
                )

                ])	

            )

            )
        
""" Row(
        [
        Text("Carga: 90%", size = 20, weight = FontWeight.BOLD),
        IconButton(icon = icons.EDIT_ROUNDED, icon_size = 20)
        ],
        alignment = MainAxisAlignment.CENTER,
    ), """