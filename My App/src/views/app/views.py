from flet import *
from cadastro import Cadastro
from login import Login

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
          Cadastro(page)
        ]
      ),
  }