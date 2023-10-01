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

cardmenu = Row()

menu_veiculos = [
{
	"image":"/home/marco/unifesp/engenharia de software/Engenharia-de-Software---Electric-Ways/My_App/assets/images/carro.png",
	"title":"Autonomia: 470km",
	"battery":"Bateria: 69%",
	"desc":"Tempo de regarga: 23min - carga rápida"
},
{
	"image":"/home/marco/unifesp/engenharia de software/Engenharia-de-Software---Electric-Ways/My_App/assets/images/carro.png",
	"title":"Autonomia: 470km",
	"battery":"Bateria: 69%",
	"desc":"Tempo de regarga: 23min - carga rápida"
},
{
	"image":"/home/marco/unifesp/engenharia de software/Engenharia-de-Software---Electric-Ways/My_App/assets/images/carro.png",
	"title":"Autonomia: 470km",
	"battery":"Bateria: 69%",
	"desc":"Tempo de regarga: 23min - carga rápida"
},
]

for x in menu_veiculos:
	cardmenu.controls.append(
		Card(
		elevation=20,
		content=Container(
		bgcolor="white",
		width=300,
		border_radius = border_radius.all(30),
		content=Column([
            ListTile(
                            leading = Icon(icons.ELECTRIC_CAR_ROUNDED, size = 50),
                            title = Text("Audi RS", size = 25),
                            subtitle = Text("Placa: ABC-1234", size = 20),
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
			Image(
                    src=x['image'],
                    border_radius = border_radius.all(30),
                    width=150,
                    height=110,
                    fit=ImageFit.CONTAIN
				),
			Container(
			padding = padding.all(10),
			content=Column([
			Text(x['title'],size=16,weight="bold"),
			Text(x['desc'],size=13),

			# FOR battery AND BUTTON
			Row([
			Text(x['battery'],size=23,weight="bold"),
				],alignment="spaceBetween"
            ),
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

		)

sectioncard = Container(
	padding = padding.only(top=20),
	content=Column([
	Container(
	margin = margin.only(left=10),
	#content=txt_name,
	),
	Row([
       cardmenu

		],scroll="auto")

		])
	)
# -------------------------------------------------------------------------------------------------------


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
            sectioncard, #new card added
            # Row(
            #     [
            #     ],
            #     alignment=MainAxisAlignment.CENTER,
            # ),            
        ]
    )



class MeusVeiculos(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        
    def build(self):
        back_button.on_click = self.btn_back
        tela = telaPerfil(self)
        
        # id = self.page.session.get('user_id')
        # results = get_vehicles(id[0][0])
        # for veic in results:
        #     nome, modelo, placa, cor, range = veic
        #     new_card = self.criar_card(nome, modelo, placa, cor, range)
        #     tela.controls[2].controls.append(new_card)
        
        return tela
            
    
    def btn_back(self, e):
        self.page.go('/perfil')
        
        
    def criar_card(self, nome, modelo, placa, cor, range):
        return Card(
            content = Container(
                content = Column(
                    [
                        ListTile(
                            leading = Icon(icons.ELECTRIC_CAR_ROUNDED, size = 50),
                            title = Text(nome, size = 25),
                            subtitle = Text(placa, size = 20),
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

                        Row(
                            [
                            Text(f"Modelo: {modelo}", size = 20)
                            ],
                            alignment = MainAxisAlignment.START,
                        ),

                        Row(
                            [
                            Text(f"Cor: {cor}", size = 20)
                            ],
                            alignment = MainAxisAlignment.START,
                        ),

                        Row(
                            [
                            Text(f"Range: {range}Km", size = 20)
                            ],
                            alignment = MainAxisAlignment.START,
                        ),

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
                        )                            
                    ],
                ),
                width = 400,
                padding = 10,
            ),
            color = colors.WHITE,
        )
        
""" Row(
        [
        Text("Carga: 90%", size = 20, weight = FontWeight.BOLD),
        IconButton(icon = icons.EDIT_ROUNDED, icon_size = 20)
        ],
        alignment = MainAxisAlignment.CENTER,
    ), """