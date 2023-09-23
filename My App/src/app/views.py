from flet import *
from cadastro import Cadastro
from login import Login
from home import Home
from usuario import Usuario

colorBackground3 = '#F0F0FF'


def views_handler(page):
  return {

    '/login':View(
        route='/login',
        controls=[
          Login(page)
        ]
      ),


    '/cadastro':View(
        route='/cadastro',
        controls=[
          Cadastro(page)
        ]
      ),


      '/home':View(
        route='/home',
        controls=[
          NavigationBar(
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
            ),
          Home(page),
        ]
      ),

      '/usuario':View(
        route='/usuario',
        controls=[
          Usuario(page)
        ]
      ),
  }