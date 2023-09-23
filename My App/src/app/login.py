from flet import *


colorBackground = '#00001E'
colorBackground2 = '#1e19a8'

logo = Image(src="https://i.ibb.co/VtsLycp/logo-without-bg.png", scale=0.8, col={"md": 4})
txt_field_user = TextField(label="Email", col={"md": 4})
txt_field_password = TextField(label="Password", col={"md": 4}, password=True, can_reveal_password=True)

botaoPadrao = ButtonStyle(
        color = {MaterialState.DEFAULT: colors.WHITE}, #Estado(clicando, default, selecionando, etc),
        bgcolor = colorBackground, 
        padding = {MaterialState.DEFAULT: 6}, #Tamanho
        overlay_color = colors.BLUE_200, #Cor quando seleciona
        side = {MaterialState.DEFAULT: BorderSide(2, colors.WHITE)}, #Borda do botao
        shape = {MaterialState.DEFAULT: RoundedRectangleBorder(radius=20)},
        
    )

def telaLogin(self):
    return ResponsiveRow(
        [
            Column(
                [
                    logo,
                    txt_field_user,
                    txt_field_password,
                    ElevatedButton(text="SIGN IN", col={"md": 4}, on_click=self.btn_sign_in_clicked, style=botaoPadrao),
                    TextButton(text="SIGN UP", col={"md": 4}, on_click=lambda _: self.page.go('/cadastro'), style=botaoPadrao),
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
        ],
    )


class Login(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        tela = telaLogin(self)
        return tela

    def btn_sign_in_clicked(self, e):

        if not txt_field_user.value:
            txt_field_user.error_text = "please enter your username or email"
            self.update()

        else:
            txt_field_user.error_text = ""
            self.update()

        if not txt_field_password.value:
            txt_field_password.error_text = "please enter your password"
            self.update()

        else:
            txt_field_password.error_text = ""
            self.update()

        if txt_field_user.value and txt_field_password.value:
            if txt_field_user.value == "admin":
                txt_field_user.error_text = ""
                self.update()
                
                if txt_field_password.value == "admin":
                    print("sign in")

                else:
                    txt_field_password.error_text = "wrong password"
                    self.update()
            else:
                txt_field_user.error_text = "user not found"
                self.update()