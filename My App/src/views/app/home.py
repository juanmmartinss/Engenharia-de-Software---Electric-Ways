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

    def build(self):
        
        return Column([
                searchBar,
                infoButton,
            ],
            horizontal_alignment = CrossAxisAlignment.STRETCH)




