from flet import *
import flet as ft

colorBackground = '#00001E'
colorBackground2 = '#1e19a8'
colorBackgroundClaro = '#F0F0FF'

botaoPadrao = ButtonStyle(
        color = {MaterialState.DEFAULT: colors.WHITE}, #Estado(clicando, default, selecionando, etc),
        bgcolor = colorBackground, 
        padding = {MaterialState.DEFAULT: 6}, #Tamanho
        overlay_color = colors.BLUE_200, #Cor quando seleciona
        side = {MaterialState.DEFAULT: BorderSide(2, colors.WHITE)}, #Borda do botao
        shape = {MaterialState.DEFAULT: RoundedRectangleBorder(radius=20)},
        
    )

back_button = IconButton(
                        icon = icons.ARROW_BACK_IOS_NEW_ROUNDED,
                        icon_color = colorBackground,
                        icon_size = 20,
                        tooltip = "Voltar",
                    )

card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.LOCATION_ON_ROUNDED),
                            title=ft.Text("Posto BR"),
                            subtitle=ft.Text(
                                "avenida cidade jardim, 1000"
                            ),
                            trailing=ft.PopupMenuButton(
                                icon=icons.MORE_VERT,
                                items=[
                                    ft.PopupMenuItem(
                                        content=ft.Text("Ver no mapa"),
                                    ),
                                    ft.PopupMenuItem(
                                        content=ft.Text("Mais informações"),
                                    ),
                                    ],
                                    
                                ),
                            #alignment=ft.MainAxisAlignment.END,
                        ),
                        ft.Row(
                            [ft.Text("Distancia: 15km"), ft.Text("Vagas: 3") ,ft.TextButton("Start", icon=icons.PLAY_ARROW_ROUNDED)],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        ),
                    ],
                    scroll = 'auto'
                ),
                width=400,
                padding=10,
            )
        )

# card_postos = Container(
#     #Column(
#         Row([
#             Text("Nome Posto", color = colorBackgroundClaro, size = 25),
#         ],
#             alignment = MainAxisAlignment.CENTER
#         ),
        
#         Row([
#             Text("Dist", color = colorBackgroundClaro, size = 20),
#             Text("Pot", color = colorBackgroundClaro, size = 20),
#             Text("Vagas", color = colorBackgroundClaro, size = 20),
            
#             IconButton(
#                 icon = icons.LOCATION_ON_ROUNDED,
#                 icon_color = colorBackgroundClaro,
#                 icon_size = 20,
#                 tooltip = "Ver no mapa",
#             )
#         ]),
        
#     #),
#     bgcolor = colorBackground,
# )




# cardmenu = Row()

# for x in 5:
# 	cardmenu.controls.append(
# 		Card(
# 		elevation=20,
# 		content=Container(
# 		bgcolor="white",
# 		width=150,
# 		border_radius = border_radius.all(30),
# 		content=Column([
# 			Image(
# 			src=x['image'],
# 			border_radius = border_radius.all(30),
# 			width=150,
# 			height=110,
# 			fit=ImageFit.CONTAIN
# 				),
# 			Container(
# 			padding = padding.all(10),
# 			content=Column([
# 			Text(x['title'],size=16,weight="bold"),
# 			Text(x['desc'],size=13),

# 			# FOR PRICE AND BUTTON
# 			Row([
# 			Text(x['price'],size=23,weight="bold"),
# 			IconButton(icon="add")
# 				],alignment="spaceBetween")
# 			])
# 			)

# 			])	

# 		)

# 		)

# 		)

# sectioncard = Container(
# 	padding = padding.only(top=20),
# 	bgcolor= "#E3002A",
# 	content=Column([
# 	Container(
# 	margin = margin.only(left=10),
# 	content=Text("In Restaurant",
# 		color="white",
# 		size=30,weight="bold"
# 		)
# 	),
# 	Row([
#        cardmenu

# 		],scroll="auto")

# 		])

# 	)