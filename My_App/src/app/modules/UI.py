from flet import *

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


cardVeiculos = Card(
            content = Container(
                content = Column(
                    [
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

                        Row(
                            [
                            Text("Audi", size = 20)
                            ],
                            alignment = MainAxisAlignment.START,
                        ),


                        Row(
                            [
                            Text("Cor: Vermelho", size = 20)
                            ],
                            alignment = MainAxisAlignment.START,
                        ),

                        Row(
                            [
                            Text("Potência: 0", size = 20)
                            ],
                            alignment = MainAxisAlignment.START,
                        ),

                        Row(
                            [
                            Text("Carga: 90%", size = 20, weight = FontWeight.BOLD),
                            IconButton(icon = icons.EDIT_ROUNDED, icon_size = 20)
                            ],
                            alignment = MainAxisAlignment.CENTER,
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
