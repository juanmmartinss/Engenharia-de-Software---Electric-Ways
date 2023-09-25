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
                    Icon(name = icons.SEARCH_ROUNDED, color = colorBackground),
                    Text("PESQUISAR", color = colorBackground),
                ],
                alignment = alignment.center,
            ),
        ),

        ],
           
    ),
    margin = margin.only(top = 30)
)


class Home(UserControl):

    def __init__(self,page):
        super().__init__()
        self.page = page

    def search_bar_clicked(self):
        self.page.update()
        pass

    def build(self):
        
        return Column([

                Dropdown(
                    width=100,
                    options=[
                        dropdown.Option("PESQUISAR"),
                        dropdown.Option("HISTÓRICO"),
                        dropdown.Option("FAVORITOS"),
                    ],
                    bgcolor = colorBackground,
                    focused_bgcolor = colorBackground,
                    border_color = colorBackground,
                    color = colorBackground
                ),


                infoButton,

            ],
            horizontal_alignment = CrossAxisAlignment.STRETCH
            )




