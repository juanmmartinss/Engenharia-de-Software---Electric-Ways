from flet import *
from cadastro import Cadastro
from login import Login
from home import Home
from perfil import Perfil
from modules.UI import *

def change_page(e, page):
  if e.control.selected_index == 0:
    page.go('/home')
  elif e.control.selected_index == 1:
    pass
    # page.go('/rotas')
  elif e.control.selected_index == 2:
    pass
    # page.go('/carregamento')
  elif e.control.selected_index == 3:
    page.go('/perfil')
  elif e.control.selected_index == 4: 
    pass
    #page.go('/configuracoes')

def views_handler(page):
  return {

    '/login':View(
        route='/login',
        controls=[
          Login(page)
        ],
        bgcolor = colorBackground,
      ),


    '/cadastro':View(
        route='/cadastro',
        controls=[
          Cadastro(page)
        ],
        bgcolor = colorBackground
      ),


      '/home':View(
        route='/home',
        controls=[
          NavigationBar(
              selected_index=0,
              destinations=[
                
                  NavigationDestination(
                      icon = icons.HOUSE_ROUNDED, 
                      ),

                  NavigationDestination(
                      icon = icons.EXPLORE, 
                      ),

                  NavigationDestination(
                      icon = icons.BATTERY_CHARGING_FULL_ROUNDED, 
                      ),
                  
                  NavigationDestination(
                      icon = icons.PERSON_ROUNDED,
                  ),

                  NavigationDestination(
                      icon = icons.SETTINGS_ROUNDED,
                  ),
              ],
              on_change=lambda e: change_page(e, page),
              bgcolor = colorBackgroundClaro,
            ),
          Home(page),
        ],
        bgcolor = colorBackground
      ),
      
      '/perfil':View(
        route='/perfil',
        controls=[
          Perfil(page)
        ],
        bgcolor = colorBackgroundClaro
      ),
  }