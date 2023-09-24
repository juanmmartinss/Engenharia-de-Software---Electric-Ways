from flet import *
from modules.SQLiteDB import *
from modules.ManageDB import *
from modules.UI import *


logo = Image(src = "My_App/assets/images/logo.png", scale=0.8, col={"md": 4})


txt_field_username = TextField(
                            hint_text="Username",
                            hint_style=TextStyle(color=colors.WHITE),
                            bgcolor = colors.TRANSPARENT, 
                            border_color = colors.WHITE, 
                            border_width = 1,
                            prefix_icon = "person_outline_rounded",
                            border_radius = 20,
                            text_size= 15,
                            color = colors.WHITE,
                            col={"md": 4}
                            )


txt_field_email = TextField(
                            hint_text="Email",
                            hint_style=TextStyle(color=colors.WHITE),
                            bgcolor = colors.TRANSPARENT, 
                            border_color = colors.WHITE, 
                            border_width = 1,
                            prefix_icon = "person_outline_rounded",
                            border_radius = 20,
                            text_size= 15,
                            color = colors.WHITE,
                            col={"md": 4}
                            )


txt_field_password = TextField(
                            hint_text="Senha",
                            hint_style=TextStyle(color=colors.WHITE),
                            bgcolor = colors.TRANSPARENT,
                            border_color = colors.WHITE, 
                            border_width = 1,
                            password = True,
                            can_reveal_password = True,
                            prefix_icon = "lock_outline_rounded",
                            border_radius = 20,
                            text_size= 15,
                            color = colors.WHITE, 
                            col={"md": 4}
                            )


txt_field_password_confirm = TextField(
                            hint_text="Confirmar senha",
                            hint_style=TextStyle(color=colors.WHITE),
                            bgcolor = colors.TRANSPARENT,
                            border_color = colors.WHITE, 
                            border_width = 1,
                            password = True,
                            can_reveal_password = True,
                            prefix_icon = "lock_outline_rounded",
                            border_radius = 20,
                            text_size= 15,
                            color = colors.WHITE, 
                            col={"md": 4}
                            )


def telaCadastro(self):  
    return ResponsiveRow(
                [
                    Column(
                        [
                            logo,

                            txt_field_username, 

                            txt_field_email,

                            txt_field_password, 

                            txt_field_password_confirm,

                            ElevatedButton(
                                content = Container(
                                    Text(value = "Cadastrar", size = 30),
                                ),
                                col = {"md": 4}, 
                                on_click = self.btn_sign_up_clicked, 
                                style = botaoPadrao,
                                width = 200,
                            ),

                            TextButton(
                                content = Container(
                                    Text(value = "Entrar", 
                                        size = 20, 
                                        color = colors.WHITE,
                                ), 
                                col={"md": 4}, 
                                on_click=lambda _: self.page.go('/login'), 

                                ),
                            )
                        ],
                        horizontal_alignment = CrossAxisAlignment.CENTER,
                    ),
                ],
            )


class Cadastro(UserControl):
  
    def __init__(self,page):
        super().__init__()
        self.page = page
    

    def build(self):
        tela = telaCadastro(self)  
        return tela
  

    def validate_signup(self, username, email, password, password_confirm):

        valid = True

        if not username:
            txt_field_username.error_text = "please choose a username"
            valid = False
        else:
            txt_field_username.error_text = ""

        if not email:
            txt_field_email.error_text = "please enter your email"
            valid = False
        elif get_user(email):
            txt_field_email.error_text = "email already registered"
            valid = False
        else:
            txt_field_email.error_text = "" 

        if not password:
            txt_field_password.error_text = "please choose a password"
            valid = False
        else:
            txt_field_password.error_text = ""

        if not password_confirm:
            txt_field_password_confirm.error_text = "please confirm your password"
            valid = False
        elif txt_field_password.value != password_confirm:
            txt_field_password_confirm.error_text = "passwords do not match"
            valid = False
        else:
            txt_field_password_confirm.error_text = ""
 
        self.update()
        return valid


    def btn_sign_up_clicked(self, e):
        # obter campos de texto
        username = txt_field_username.value
        email = txt_field_email.value
        password = txt_field_password.value
        password_confirm = txt_field_password_confirm.value

        # verificar validade dos dados
        valid = self.validate_signup(username, email, password, password_confirm)
        if(valid):
            # cadastrar usuário
            add_user(username, email, password)
  