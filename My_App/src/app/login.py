from flet import *
from modules.SQLiteDB import *
from modules.ManageDB import *
from modules.UI import *


logo = Image(src="My_App/assets/images/logo.png", scale=0.8, col={"md": 4})

txt_field_email = TextField(
                            #label="Email",
                            hint_text="Email",
                            hint_style=TextStyle(color=colors.WHITE),
                            bgcolor = colors.TRANSPARENT, 
                            border_color = colors.WHITE, 
                            border_width = 1,
                            prefix_icon = "person_outline_rounded",
                            border_radius = 20,
                            text_size = 15,
                            color = colors.WHITE,
                            col = {"md": 4}
                        
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

txt_field_fpass = Column([
                        TextButton(
                            content = Container(
                            Text(value = "Esqueceu a senha?", size = 14, color = colors.WHITE)
                            )
                        ),
                        ],

                        horizontal_alignment = CrossAxisAlignment.START
                    )


login_button = ElevatedButton(
                            content = Container(
                                Text(value = "Entrar", size = 30),
                                ),
                            col = {"md": 4}, 
                            style = botaoPadrao,
                            width = 200,
                            )

cadastrar_button = TextButton(
                            content = Container(
                                Text(value = "Cadastre-se", 
                                     size = 20, 
                                     color = colors.WHITE,),
                                ), 
                            col={"md": 4}, 
                            )

def telaLogin(self):
    return ResponsiveRow(
        [

            Column(
                [
                    logo,

                    txt_field_email,

                    txt_field_password,
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),

            Column(
                [
                    txt_field_fpass
                ],
                horizontal_alignment=CrossAxisAlignment.START
            ),

            Column([
                    login_button,

                    cadastrar_button
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
        ],

        vertical_alignment=CrossAxisAlignment.CENTER,
    )


class Login(UserControl):

    def __init__(self, page):
        super().__init__()
        self.page = page


    def build(self):
        tela = telaLogin(self)
        return tela
    

    def validate_signin(self, email, password):
        valid = True

        if not email:
            txt_field_email.error_text = "please enter your email"
            valid = False
        elif not get_user(email):
            txt_field_email.error_text = "email not registered"
            valid = False
        else:
            txt_field_email.error_text = "" 

        if not password:
            txt_field_password.error_text = "please enter your password"
            valid = False
        else:
            txt_field_password.error_text = ""

        if(valid):
            results = get_user(email)
            user_email, user_password = results[0]
            if(password != user_password):
                txt_field_password.error_text = "wrong password"
                valid = False

        self.update()
        return valid
    
    def signin_user(self, email):
        self.page.go('/home')

    def btn_sign_in_clicked(self, e):
        # obter campos de texto
        email = txt_field_email.value
        password = txt_field_password.value

        # verificar validade dos dados
        valid = self.validate_signin(email, password)
        if(valid):
            # entrar com usuário
            self.signin_user(email)