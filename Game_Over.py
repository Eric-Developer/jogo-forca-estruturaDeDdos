from Boneco import *
from Cores import *


def game_over(tela, palavra):
    tela.fill(cor_fundo)
    font_grande = pg.font.SysFont('comicsansms', 26, bold=True)
    titulo = font_grande.render('JOGO DA FORCA', 1, cor_texto)
    tela.blit(titulo, (335, 30))

    base = pg.Surface((900, 10))
    haste = pg.Surface((20, 230))
    topo = pg.Surface((80, 15))
    laco = pg.Surface((3, 40))
    tela.blit(base, (0, 450))
    tela.blit(haste, (70, 220))
    tela.blit(topo, (90, 220))
    tela.blit(laco, (167, 235))

    pg.draw.circle(tela, white, (169, 295), 20)
    pg.draw.line(tela, white, (169, 315), (169, 400), 5)
    pg.draw.line(tela, white, (165, 320), (140, 350), 5)
    pg.draw.line(tela, white, (173, 320), (195, 350), 5)
    pg.draw.line(tela, white, (169, 400), (140, 440), 5)
    pg.draw.line(tela, white, (169, 400), (198, 440), 5)

    font_grande = pg.font.SysFont('comicsansms', 26, bold=True)
    font_pequena = pg.font.SysFont('comicsansms', 16)

    msg_final = font_pequena.render('A palavra secreta era ' + palavra.upper(), 1, black)
    tela.blit(msg_final, (250, 420))
    eyes = font_pequena.render('x x', 1, black)
    tela.blit(eyes, (158, 280))
    final = font_grande.render('GAME OVER', 1, black)
    tela.blit(final, (360, 200))

    pg.display.update()


def over(tela, palavra):
    while True:
        game_over(tela, palavra)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()


