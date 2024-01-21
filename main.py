from Game_Over import *
from Ganhou import *
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data)
            current = current.next
        return result

pg.init()
screen = pg.display.set_mode((900, 500))
pg.display.set_caption('JOGO DA FORCA')


def palavra_secreta():
    with open('Palavras.txt', 'r') as arq:
        lista_palavras = arq.readlines()
        palavra = random.choice(lista_palavras).strip()
    return palavra.upper()

def tela_fixa(background):
    font_grande = pg.font.SysFont('comicsansms', 26, bold=True)
    screen.fill(background)
    titulo = font_grande.render('JOGO DA FORCA', 1, cor_texto)
    screen.blit(titulo, (335, 30))

    base = pg.Surface((900, 10))
    haste = pg.Surface((20, 230))
    topo = pg.Surface((80, 15))
    laco = pg.Surface((3, 40))
    screen.blit(base, (0, 450))
    screen.blit(haste, (70, 220))
    screen.blit(topo, (90, 220))
    screen.blit(laco, (167, 235))


# Insere na tela quando o usuário digita uma letra
def entrada(player_entrada):
    font_pequena = pg.font.SysFont('comicsansms', 16)
    pedido = font_pequena.render('>>', 1, black)
    digitado = font_pequena.render(player_entrada, 1, black)
    screen.blit(pedido, (250, 240))
    screen.blit(digitado, (265, 240))


# Insere as letras chutadas na tela
chutes = LinkedList()
def tentativas(tentativa=''):
    global chutes
    if tentativa not in chutes.display():
        chutes.append(tentativa)
    font_pequena = pg.font.SysFont('comicsansms', 16)
    imprime_tentativa = font_pequena.render('TENTATIVAS: ' + '  '.join(chutes.display()), 1, black)
    screen.blit(imprime_tentativa, (250, 220))

# Seta a qntd de traços de acordo com o tamanho da palavra / troca os traços pelos chutes certos / verifica se ganhou
lines = LinkedList()
def underscore(palavra, letra=''):
    if not lines.head:
        for char in palavra:
            lines.append('_ ')
    current = lines.head
    for cont, char in enumerate(palavra):
        if letra == char:
            current.data = letra + ' '
        current = current.next

    font_pequena = pg.font.SysFont('comicsansms', 16)
    linhas = font_pequena.render(''.join(lines.display()), 1, black)
    screen.blit(linhas, (250, 410))
    if '_ ' not in lines.display():
        return True
    return False

def game():
    palavra = palavra_secreta()
    chute = ''
    letras_digitadas = LinkedList()
    erros = 0
    done = False

    while not done:
        tela_fixa(cor_fundo)
        entrada(chute)
        tentativas()
        ganhou = underscore(palavra)
        if ganhou:
            return 1, palavra
        perdeu = boneco(screen, erros)
        if perdeu:
            return 0, palavra

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    tentativas(chute)
                    if chute and chute not in letras_digitadas.display():
                        if chute in palavra:
                            underscore(palavra, chute)
                        else:
                            erros += 1
                        letras_digitadas.append(chute)
                    chute = ''  # Limpa a variável chute após cada tentativa
                elif event.key == pg.K_BACKSPACE:
                    chute = chute[:-1]
                elif pg.K_a <= event.key <= pg.K_z:
                    chute += pg.key.name(event.key).upper()

        pg.display.update()

resultado, palavra = game()
if resultado == 0:
    print('perdeu')
    over(screen, palavra)
else:
    print('ganhou')
    win(screen, palavra)
