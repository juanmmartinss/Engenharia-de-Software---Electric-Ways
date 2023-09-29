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
