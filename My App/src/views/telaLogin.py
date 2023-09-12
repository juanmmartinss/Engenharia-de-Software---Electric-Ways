from flet import *
import cv2 as cv


def main(page: Page):

    colorBackground = '#020c2b'

    background = Container(
        bgcolor = colorBackground,
        width = 500,
        height = 900
        )
    
    page.add(background)


    logo = Image(
        src = f"assets/elecLogo.png",
        height=100,
        fit = ImageFit.CONTAIN,
    )

    body = Container(
        Column([
            Container(
                Image(src = 'assets/elecLogo.png')
            )
        ])
    )

    image = cv.imread('assets/elecLogo.png')
    cv.imshow("imagem", image)

    page.add(body)

app(target=main)