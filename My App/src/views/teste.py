from flet import *
# class MenuDetail(UserControl):
#     def  build(self):
#         return self.menu


body = Container(
    
    Column([
        # MenuDetail(),
        Container(
            Image(
                src = "logomudado.png",
                scale=0.8,
                #abaixar a imagem
                height = 400,
            )
        ), 
        Row([
            #BOTAO ENTRAR
            Container(
                
                
                #CreateButton("Entrar", )
            ),

        ])
    ]),
    
    gradient= LinearGradient(
        begin=alignment.top_left,
        end=alignment.bottom_right,
        colors=['#00001E', '#1e19a8'],
    ), 
    
    width=500,
    height=800,
)

def main(page: Page):

    page.window_max_height = 800
    page.window_width = 500
    page. window_max_width = 500
    page.window_height = 800
    
    page.padding = 0
    
    page.add(
        body
    )
    

        
app(target=main, assets_dir="assets")