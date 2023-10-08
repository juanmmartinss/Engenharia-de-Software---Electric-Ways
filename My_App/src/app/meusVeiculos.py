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

imagem_carro = Image(src="My_App/assets/images/carro.png", scale=0.4)

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
            id_veic, nome, modelo, placa, cor, range = veic
            new_card = self.criar_card(id_veic, nome, modelo, placa, cor, range)
            card_row = tela.controls[2].content.controls[1]
            card_row.controls.append(new_card)
        return tela
            
    
    def btn_back(self, e):
        self.page.go('/perfil')
        
        
    def pick_car(self, e):
        self.page.session.set('veic_id', e.control.data)
        print(f"ID veículo selecionado: {self.page.session.get('veic_id')}")
        
        
    def criar_card(self, id_veic, nome, modelo, placa, cor, range):
        return Card(
            elevation=20,
            content=Container(
            bgcolor= '#5A5A5A',
            #bgcolor = colorBackground,
            width=300,
            border_radius = border_radius.all(30),
            content=Column([
                ListTile(
                        leading = Icon(icons.ELECTRIC_CAR_ROUNDED, size = 50),
                        title = Text(modelo, max_lines = 3, size = 25, weight = FontWeight.BOLD, selectable=True),
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
                            content_padding = padding.all(0),
                        ),
                imagem_carro,
                Container(
                        padding = padding.all(10),
                        content=Column([
                        Text(f"Autonomia: {range}Km",size=16,weight="bold"),
                        Text(f"Cor: {cor}",size=13),
                        Row(
                            [
                            TextButton(
                                data=id_veic,
                                content = Container(
                                    Text(value = "Selecionar", size = 20, color = colorBackgroundClaro),
                                    ),
                                col = {"md": 4}, 
                                on_click=self.pick_car
                            ),
                            ],
                            alignment = MainAxisAlignment.CENTER,
                            ),
                        
                        ])
                )

                ],
                spacing=0,
                ),
            
            )

            )