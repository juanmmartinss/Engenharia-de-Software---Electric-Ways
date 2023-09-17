from flet import *

colorBackground = '#00001E'
colorBackground2 = '#1e19a8'
colorBackground3 = '#F0F0FF'

infoButton = Container(
    IconButton(
        icon = icons.INFO_ROUNDED,
        icon_color = colorBackground,
        icon_size = 40,
        tooltip = "Ajuda e Informações"
    ),

    alignment = alignment.top_right
)

def main(page: Page):

    page.window_max_height = 800
    page.window_width = 500
    page. window_max_width = 500
    page.window_height = 800


    page.navigation_bar = NavigationBar(
        destinations=[

            NavigationDestination(
                icon = icons.EXPLORE, 
                label = "Rotas",
                ),

            NavigationDestination(
                icon = icons.BATTERY_CHARGING_FULL_ROUNDED, 
                label = "Carregamento"
                ),

            NavigationDestination(
                icon = icons.PERSON_ROUNDED,
                label = "Perfil",
            ),

            NavigationDestination(
                icon = icons.SETTINGS_ROUNDED,
                label = "Configurações",
            ),

        ],

        bgcolor = colorBackground3,
    )

    page.add(infoButton)



app(target=main)