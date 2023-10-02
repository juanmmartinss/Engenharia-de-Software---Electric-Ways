from flet import *
from modules.SQLiteDB import *
from modules.FacadeBD import *
from modules.UI import *
from modules.crypto import *


logo = Image(src = "My_App/assets/images/logo.png", scale=0.8, col={"md": 4})


txt_name = TextField(
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


txt_email = TextField(
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


txt_password = TextField(
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


txt_password_confirm = TextField(
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


btn_signup = ElevatedButton(
                                content = Container(
                                    Text(value = "Cadastrar", size = 30),
                                ),
                                col = {"md": 4},  
                                style = botaoPadrao,
                                width = 200,
                            )

btn_signin = TextButton(
                            content = Container(
                                Text(value = "Entrar", 
                                    size = 20, 
                                    color = colors.WHITE,
                                ), 
                            ),
                            col={"md": 4}, 
                            )

def telaCadastro(self):  
    return ResponsiveRow(
                [
                    Column(
                        [
                            logo,

                            txt_name, 

                            txt_email,

                            txt_password, 

                            txt_password_confirm,

                            btn_signup,

                            btn_signin,
                            
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
        btn_signin.on_click = self.btn_signin_clicked
        btn_signup.on_click = self.btn_signup_clicked
        tela = telaCadastro(self)  
        return tela
  

    def validate_signup(self, username, email, password, password_confirm):

        valid = True

        if not username:
            txt_name.error_text = "Insira um nome"
            valid = False
        else:
            txt_name.error_text = ""

        if not email:
            txt_email.error_text = "Insira um email"
            valid = False
        elif get_user(email):
            txt_email.error_text = "Email já cadastrado"
            valid = False
        else:
            txt_email.error_text = "" 

        if not password:
            txt_password.error_text = "Insira uma senha"
            valid = False
        else:
            txt_password.error_text = ""

        if not password_confirm:
            txt_password_confirm.error_text = "Confirme a senha"
            valid = False
        elif txt_password.value != password_confirm:
            txt_password_confirm.error_text = "Senha incorreta"
            valid = False
        else:
            txt_password_confirm.error_text = ""
 
        self.update()
        return valid


    def btn_signup_clicked(self, e):
        # obter campos de texto
        username = txt_name.value
        email = txt_email.value
        password = txt_password.value
        password_confirm = txt_password_confirm.value

        # verificar validade dos dados
        valid = self.validate_signup(username, email, password, password_confirm)
        if(valid):
            # cadastrar usuário
            add_user(username, email, password)
            self.page.go('/login')
            
            
    def btn_signin_clicked(self, e):
        self.page.go('/login')