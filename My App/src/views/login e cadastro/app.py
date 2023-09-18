from flet import *
from views import views_handler

def main(page: Page):
  
  page.window_max_height = 800
  page.window_width = 500
  page. window_max_width = 500
  page.window_height = 800
        

  def route_change(route):
    print(page.route)
    page.views.clear()
    page.views.append(
      views_handler(page)[page.route]
    )


  page.on_route_change = route_change
  page.go('/login')



app(target=main)