from flet import *
import flet as ft

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

searchBar = Container(
    Column([
        ft.ElevatedButton(
            width = 300,
            height = 50,
            content = ft.Row(
                [
                    ft.Icon(name = icons.SEARCH_ROUNDED, color = colorBackground),
                    ft.Text("PESQUISAR", color = colorBackground),
                ],

                alignment = alignment.center,
            ),
            # bgcolor = colorBackground2,
        ),
        
        ],
        #alignment = ft.MainAxisAlignment.CENTER, 
           
    ),
)

def main(page: Page):
    
    page.theme_mode = ThemeMode.LIGHT

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

    page.add(
        Row([
            searchBar,
            infoButton,
        ], vertical_alignment = CrossAxisAlignment.STRETCH),
    )

app(target=main)