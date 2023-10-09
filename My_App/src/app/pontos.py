from flet import *
from modules.SQLiteDB import *
from modules.FacadeBD import *
from modules.UI import *
import threading


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


menu_veiculos = [
{
	"distance":"Distancia: 12km",
	"spots":"Vagas: 3"
},
{
	"distance":"Distancia: 12km",
	"spots":"Vagas: 3"
},
{
	"distance":"Distancia: 12km",
	"spots":"Vagas: 3"
},
{
	"distance":"Distancia: 12km",
	"spots":"Vagas: 3"
},
{
	"distance":"Distancia: 12km",
	"spots":"Vagas: 3"
},
{
	"distance":"Distancia: 12km",
	"spots":"Vagas: 3"
},
]



card_menu = Column(
    scroll='auto',
    horizontal_alignment= CrossAxisAlignment.CENTER
  ) 

for x in menu_veiculos:
    card_menu.controls.append(
		Card(
		elevation=20,
		content=Container(
		bgcolor="white",
		width=600,
		border_radius = border_radius.all(30),
		content=Column([
            ListTile(
                            leading = Icon(icons.LOCATION_ON_ROUNDED),
                            title = Text("Posto BR"),
                            subtitle = Text(
                                "avenida cidade jardim, 1000"
                            ),
                            trailing = PopupMenuButton(
                                icon = icons.MORE_VERT,
                                items = [
                                    PopupMenuItem(
                                        content = Text("Ver no mapa"),
                                    ),
                                    PopupMenuItem(
                                        content = Text("Mais informações"),
                                    ),
                                    ],
                                    
                                ),
                        ),
			Container(
			padding = padding.all(10),
			content=Column([
			Text(x['distance'],size=16,weight="bold"),
			Text(x['spots'],size=13),

            Row(
                            [
                                Text("Distancia: 15km"), 
                                Text("Vagas: 3"),
                                TextButton("Start", icon = icons.PLAY_ARROW_ROUNDED)
                            ],
                            alignment = MainAxisAlignment.SPACE_EVENLY,
                        ),
            
			])
			)

			])	

		)

		)
)



sectioncard = Container(
        card_menu,
        
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

            sectioncard,
            
            # Column([
            #     cardPontos,cardPontos,cardPontos,cardPontos
            # ],
            #     horizontal_alignment=CrossAxisAlignment.CENTER,
            #     scroll = ScrollMode.ALWAYS,
            #     on_scroll_interval=0,

            # ),
        ]
    )



class Pontos(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        
    def build(self):
        back_button.on_click = self.btn_back
        tela = telaPerfil(self)
        return tela
    
    def btn_back(self, e):
        self.page.go('/home')