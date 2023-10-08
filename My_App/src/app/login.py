from flet import *
from modules.SQLiteDB import *
from modules.FacadeBD import *
from modules.UI import *
from modules.crypto import *


logo = Image(src="My_App/assets/images/logo.png", scale=0.8, col={"md": 4})

txt_email = TextField(
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

txt_fpass = Column([
                        TextButton(
                            content = Container(
                            Text(value = "Esqueceu a senha?", size = 14, color = colors.WHITE)
                            )
                        ),
                        ],

                        horizontal_alignment = CrossAxisAlignment.START
                    )


btn_signin = ElevatedButton(
                            content = Container(
                                Text(value = "Entrar", size = 30),
                                ),
                            col = {"md": 4}, 
                            style = botaoPadrao,
                            width = 200,
                            )

btn_signup = TextButton(
                            content = Container(
                                Text(value = "Cadastre-se", 
                                     size = 20, 
                                     color = colors.WHITE,),
                                ), 
                            col={"md": 4}, 
                            )

markdown_conectado = Checkbox(label="Mantenha-me conectado")

def telaLogin(self):
    return ResponsiveRow(
        [

            Column(
                [
                    logo,

                    txt_email,

                    txt_password,
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),

            Column(
                [
                    markdown_conectado,
                    txt_fpass
                ],
                horizontal_alignment=CrossAxisAlignment.START
            ),

            Column([
                    btn_signin,

                    btn_signup
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
        btn_signin.on_click = self.btn_signin_clicked
        btn_signup.on_click = self.btn_signup_clicked
        tela = telaLogin(self)
        return tela
    

    def validate_signin(self, email, password):
        valid = True

        if not email:
            txt_email.error_text = "Insira um email"
            valid = False
        elif not get_user(email):
            txt_email.error_text = "Email não cadastrado"
            valid = False
        else:
            txt_email.error_text = "" 

        if not password:
            txt_password.error_text = "Insira uma senha"
            valid = False
        else:
            txt_password.error_text = ""

        if(valid):
            if(not verify_password(email, password)):
                txt_password.error_text = "Senha incorreta"
                valid = False

        self.update()
        return valid
    
    def signin_user(self, email):
        id = get_token(email)
        self.page.session.set('user_id', id)
        self.page.session.set('veic_id', 0)
        self.page.go('/home')

    def btn_signin_clicked(self, e):
        # obter campos de texto
        email = txt_email.value
        password = txt_password.value

        # verificar validade dos dados
        valid = self.validate_signin(email, password)
        if(valid):
            # entrar com usuário
            self.signin_user(email)
      
      
    def btn_signup_clicked(self, e): 
        self.page.go('/cadastro')     
    