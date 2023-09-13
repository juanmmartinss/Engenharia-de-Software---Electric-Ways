from flet import *

def main(page: Page):

    colorBackground = '#00001E'
    
    botaoPadrao = ButtonStyle(
        color = {MaterialState.DEFAULT: colors.WHITE}, #Estado(clicando, default, selecionando, etc),
        bgcolor = colorBackground, 
        padding = {MaterialState.DEFAULT: 20}, #Tamanho
        overlay_color = colors.BLUE_200, #Cor quando seleciona
        side = {MaterialState.DEFAULT: BorderSide(2, colors.WHITE)}, #Borda do botao
        shape = {MaterialState.DEFAULT: RoundedRectangleBorder(radius=1)}
        
    )


    botaoEntrar = ElevatedButton("Entrar", 
                                style = botaoPadrao,
                                )
    

    botaoCadastrar = ElevatedButton(text = 'Cadastrar',
                                    style = botaoPadrao,
                                    )


    logo = Image(
        src = "logomudado.png",
        height = 200,
        width = 200,
        fit = ImageFit.CONTAIN,
    )



    page.add(logo) 
    
    page.add(botaoEntrar, botaoCadastrar)
    
    page.bgcolor = colorBackground

    page.update()

        
app(target=main, assets_dir="assets")