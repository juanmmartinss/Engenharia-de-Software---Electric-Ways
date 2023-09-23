import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.pardir, 'database')))
from database.SQLiteDB import *
from flet import *


colorBackground = '#00001E'
colorBackground2 = '#1e19a8'


logo = Image(src = "https://i.ibb.co/VtsLycp/logo-without-bg.png", scale=0.8, col={"md": 4})
txt_field_username = TextField(label="Username", col={"md": 4})
txt_field_email = TextField(label="Email", col={"md": 4})
txt_field_password = TextField(label="Password", col={"md": 4}, password=True, can_reveal_password=True,)
txt_field_password_confirm = TextField(label="Confirm Password", col={"md": 4}, password=True, can_reveal_password=True,)

botaoPadrao = ButtonStyle(
        color = {MaterialState.DEFAULT: colors.WHITE}, #Estado(clicando, default, selecionando, etc),
        bgcolor = colorBackground, 
        padding = {MaterialState.DEFAULT: 6}, #Tamanho
        overlay_color = colors.BLUE_200, #Cor quando seleciona
        side = {MaterialState.DEFAULT: BorderSide(2, colors.WHITE)}, #Borda do botao
        shape = {MaterialState.DEFAULT: RoundedRectangleBorder(radius=20)},   
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
                            ElevatedButton(text="SIGN UP", col={"md": 4}, on_click=self.btn_sign_up_clicked, style=botaoPadrao),
                            TextButton(text="SIGN IN", col={"md": 4}, on_click=lambda _: self.page.go('/login'), style=botaoPadrao),
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
  
  
    def user_exists(email):
        db = SQLiteDB()
        db.connect("src\database\database.db")
        exists = False

        cmd = "SELECT * FROM USUARIO WHERE email = ?"
        results = db.execute_query(cmd, email)
        if(len(results) > 0):
            exists = True

        db.close()
        return exists
  

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
        elif self.user_exists(email):
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
    

    def signup_user(username, email, password):
        db = SQLiteDB()
        db.connect("src\database\database.db")

        cmd = "INSERT INTO USUARIO (nome, email, senha) VALUES (?, ?, ?)"
        db.execute_query(cmd, (username, email, password))

        db.close()


    def btn_sign_up_clicked(self, e):
        # obter campos de texto
        username = txt_field_username.value
        email = txt_field_email.value
        password = txt_field_password.value
        password_confirm = txt_field_password_confirm.value

        # verificar validade dos dados
        valid = self.validate_signup(username, email, password, password_confirm)
        if(not valid):
           return
        
        # cadastrar usuário
        self.signup_user(username, email, password)


    def btn_sign_in_clicked(e, self):
        lambda _: self.page.go('/login')
  