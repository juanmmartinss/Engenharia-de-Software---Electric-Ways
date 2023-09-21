from flet import *


colorBackground = '#00001E'
colorBackground2 = '#1e19a8'


logo = Image(src = "https://i.ibb.co/VtsLycp/logo-without-bg.png", scale=0.8, col={"md": 4})
txt_field_username = TextField(label="username", col={"md": 4})
txt_field_email = TextField(label="email", col={"md": 4})
txt_field_password = TextField(label="password", col={"md": 4}, password=True, can_reveal_password=True,)
txt_field_password_confirm = TextField(label="confirm password", col={"md": 4}, password=True, can_reveal_password=True,)

users = []

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
                            ElevatedButton(text="sign up", col={"md": 4}, on_click=self.btn_sign_up_clicked),
                            TextButton(text="sign in", col={"md": 4}, on_click=self.btn_sign_in_clicked),
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
    return 
  
  
  def find_by_email(email):
        for user in users:
            if user["email"] == email:
                return user
        return None
  

  def find_by_username(username):
        for user in users:
            if user["username"] == username:
                return user
        return None


  def btn_sign_up_clicked(self, e):
        
        if not txt_field_username.value:
            txt_field_username.error_text = "please choose a username"
            self.update()

        elif self.find_by_username(txt_field_username.value):
            txt_field_username.error_text = "username already taken"
            self.update()

        else:
            txt_field_username.error_text = ""
            self.update()
            
        if not txt_field_email.value:
            txt_field_email.error_text = "please enter your email"
            self.update()

        elif self.find_by_email(txt_field_email.value):
            txt_field_email.error_text = "email already taken"
            self.update()

        else:
            txt_field_email.error_text = ""
            self.update() 
            
        if not txt_field_password.value:
            txt_field_password.error_text = "please choose a password"
            self.update()

        else:
            txt_field_password.error_text = ""
            self.update()
            
        if not txt_field_password_confirm.value:
            txt_field_password_confirm.error_text = "please confirm your password"
            self.update()

        elif txt_field_password.value != txt_field_password_confirm.value:
            txt_field_password_confirm.error_text = "passwords do not match"
            self.update()

        else:
            txt_field_password_confirm.error_text = ""
            self.update()
            
        if txt_field_username.value and txt_field_email.value and txt_field_password.value and txt_field_password_confirm.value:
            if not self.find_by_email(txt_field_email.value) and not self.find_by_username(txt_field_username.value):
                if txt_field_password.value == txt_field_password_confirm.value:
                    users.append({
                        "username": txt_field_username.value,
                        "email": txt_field_email.value,
                        "password": txt_field_password.value,
                    })
                    print("sign up")

                    for user in users:
                       print(user)


  def btn_sign_in_clicked(e, self):
        lambda _: self.go('/login')
  