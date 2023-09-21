from flet import *


colorBackground = '#00001E'
colorBackground2 = '#1e19a8'

logo = Image(src="https://i.ibb.co/VtsLycp/logo-without-bg.png", scale=0.8, col={"md": 4})
txt_field_user = TextField(label="username or email", col={"md": 4})
txt_field_password = TextField(label="password", col={"md": 4}, password=True, can_reveal_password=True)


def telaLogin(self):
    return ResponsiveRow(
        [
            Column(
                [
                    logo,
                    txt_field_user,
                    txt_field_password,
                    ElevatedButton(text="sign in", col={"md": 4}, on_click=self.btn_sign_in_clicked),
                    TextButton(text="sign up", col={"md": 4}, on_click=self.btn_sign_up_clicked),
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


    def btn_sign_up_clicked(self, e):
        lambda _: self.page.go('/cadastro')
        self.update