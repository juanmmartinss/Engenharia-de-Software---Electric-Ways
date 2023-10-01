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

# class State:
#     i = 0

# s = State()
# sem = threading.Semaphore()

# def on_scroll(e: OnScrollEvent):
#     if e.pixels >= e.max_scroll_extent - 100:
#         if sem.acquire(blocking=False):
#             try:
#                 for i in range(0, 10):
#                     column_with_scroll.controls.append(Text(f"Text line {s.i}", key=str(s.i)))
#                     s.i += 1
#                 column_with_scroll.update()
#             finally:
#                 sem.release()
                
# column_with_scroll = Column(
#                 [
#                     card,card,card,card,card,card,card,card,card,card
#                 ],
#                 horizontal_alignment=CrossAxisAlignment.CENTER,
#                 scroll = ScrollMode.ALWAYS,
#                 on_scroll_interval=0,
#                 on_scroll=on_scroll,
#             ),

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

            Column([
                cardPontos,cardPontos,cardPontos,cardPontos
            ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
                scroll = ScrollMode.ALWAYS,
                on_scroll_interval=0,

            ),
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