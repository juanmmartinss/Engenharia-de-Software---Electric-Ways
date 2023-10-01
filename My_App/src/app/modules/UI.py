from flet import *

colorBackground = '#00001E'
colorBackground2 = '#1e19a8'
colorBackgroundClaro = '#F0F0FF'

carro = Image(src="My_App/assets/images/carro.png", scale=0.2, fit = ImageFit.FIT_HEIGHT)

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

cardPontos = Card(
            content = Container(
                content = Column(
                    [
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
                        Row(
                            [
                                Text("Distancia: 15km"), 
                                Text("Vagas: 3"),
                                TextButton("Start", icon = icons.PLAY_ARROW_ROUNDED)
                            ],
                            alignment = MainAxisAlignment.SPACE_EVENLY,
                        ),
                        
                    ],
                ),
                width=400,
                padding=10,
            )
        )


cardRecentes = Card(
            content = Container(
            content = Column(
                [       
                    ListTile(
                        leading = Icon(icons.LOCATION_ON_ROUNDED),
                        title = Text("Araras", color = colors.BLACK),
                        subtitle = Text(
                            "São Paulo, Brasil"
                        ),
                        trailing = IconButton(tooltip="Start", icon = icons.PLAY_ARROW_ROUNDED
                                    
                                ),
                    ),
                ],
            ),
            width=400,
            padding=5,
            bgcolor=colors.WHITE,
            border_radius=30,
        )
)


