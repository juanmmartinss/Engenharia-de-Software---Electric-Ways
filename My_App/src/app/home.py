from flet import *
from modules.UI import *

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
        ElevatedButton(
            #width = 350,
            height = 50,
            content = Row(
                [
                    Icon(name = icons.SEARCH_ROUNDED, color = '#ffffff'),
                    Text("PESQUISAR", color = '#ffffff'),
                ],
                alignment = alignment.center,
            ),
            bgcolor = colorBackground
        ),

        ],
           
    ),
    margin = margin.only(top = 30)
)


def telaHome(self):
    return Column([
                searchBar,
                infoButton,
            ],
            horizontal_alignment = CrossAxisAlignment.STRETCH
            )


class Home(UserControl):

    def __init__(self,page):
        super().__init__()
        self.page = page

    def search_bar_clicked(self, e):
        self.page.go('/searchDestination')

    def build(self):
        searchBar.content.controls[0].on_click = self.search_bar_clicked
        tela = telaHome(self)
        return tela
        




