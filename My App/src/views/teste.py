from flet import *

body = Container(
    
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