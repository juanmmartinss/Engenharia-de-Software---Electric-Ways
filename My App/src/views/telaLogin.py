from flet import *


def main(page: Page):

    colorBackground = '#020c2b'
    
    background = Container(
        bgcolor=colorBackground,
        width=400,
        height=1900
    )
    
    

    def clicouEntrar(e):
        t.value = f"Entrando"
        page.update()

    botaoPadrao = ButtonStyle(
        color = {MaterialState.DEFAULT: colors.WHITE}, #Estado(clicando, default, selecionando, etc),
        bgcolor = colorBackground, 
        padding = {MaterialState.DEFAULT: 20}, #Tamanho
        overlay_color = colors.BLUE_200, #Cor quando seleciona
        side = {MaterialState.DEFAULT: BorderSide(2, colors.WHITE)}, #Borda do botao
        shape = {MaterialState.DEFAULT: RoundedRectangleBorder(radius=1)}
    )


    botaoEntrar = ElevatedButton("Entrar", 
                                 style = botaoPadrao
                                 )
    

    botaoCadastrar = ElevatedButton(text = 'Cadastrar',
                                    style = botaoPadrao
                                    )

    t = Text()
    
    #colorBackground = '#020c2b'

    logo = Image(
        src="assets/elecLogo.png",
        height=400,
        width=300,
        fit=ImageFit.CONTAIN,
    )


    page.add(logo)  # Add the logo image to the page
    
    #page.add(background)


    page.add(botaoEntrar, botaoCadastrar, t)
    #page.add(background)

        

app(target=main)