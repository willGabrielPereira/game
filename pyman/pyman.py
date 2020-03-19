# ---- IMPORTA BIBLIOTECAS ----
import os
import time
import pygame


def carrega_imagem(arquivo):
    # ---- ABRE ARQUIVOS DE IMAGEM ----
    arquivo = os.path.join('img', arquivo)
    try:
        superficie = pygame.image.load(arquivo)
    except pygame.error:
        raise SystemExit('Não foi possível carregar as imagens "%s" %s' % (arquivo, pygame.get_error()))
    return superficie.convert()
    # ---- FIM CARREGA_IMAGEM ----


def inicia():
    # ---- INICIA VARIAVEIS GLOBAIS ----
    global relogio, tela, largura, altura, tudo, pacman, gameover, font_padrao, font_ganho

    pygame.font.init()
    tudo = pygame.sprite.RenderPlain()
    pacman = pygame.sprite.RenderPlain()
    font_padrao = pygame.font.get_default_font()

    font_ganho = pygame.font.SysFont(font_padrao, 76)

    largura = 606
    altura = 606
    gameover = False

    # ---- CRIA TELA COM ICONE E CAPTION ----
    pygame.init()
    tela = pygame.display.set_mode([largura, altura])
    ico = carrega_imagem('icon.png')
    pygame.display.set_caption('PyMan')
    pygame.display.set_icon(ico)

    # ---- SETA O CLOCK USADO NOS FRAMES ----
    relogio = pygame.time.Clock()
    return 1
    # ---- FIM INICIA ----


class Parede(pygame.sprite.Sprite):
    # ---- CONSTRUTOR CLASSE PAREDE ----
    # ---- PARAMETROS: COORDENADAS EM TUPLE, TAMANHO EM TUPLE ----
    def __init__(self, coor: tuple, tam: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(tam)
        self.image.fill((100, 200, 255))

        self.rect = self.image.get_rect()
        self.rect.top = coor[1]
        self.rect.left = coor[0]

    # ---- FIM CLASSE PAREDE ----


def faz_parede():
    # ---- SETA TAMANHO E POSIÇÃO DAS PAREDES ----
    paredes = [[0, 0, 6, 600],
               [0, 0, 600, 6],
               [0, 600, 606, 6],
               [600, 0, 6, 606],
               [60, 60, 488, 6],
               [60, 120, 66, 6],
               [60, 120, 6, 126],
               [180, 120, 70, 6],
               [355, 120, 70, 6],
               [300, 120, 6, 66],
               [480, 120, 66, 6],
               [540, 120, 6, 126],
               [120, 180, 126, 6],
               [120, 180, 6, 126],
               [360, 180, 126, 6],
               [480, 240, 6, 60],
               [180, 240, 6, 126],
               [180, 360, 246, 6],
               [420, 240, 6, 126],
               [240, 240, 42, 6],
               [324, 240, 42, 6],
               [240, 240, 6, 66],
               [240, 300, 126, 6],
               [360, 240, 6, 66],
               [0, 300, 66, 6],
               [540, 300, 66, 6],
               [60, 360, 66, 6],
               [60, 420, 6, 130],
               [480, 360, 66, 6],
               [540, 420, 6, 130],
               [120, 420, 366, 6],
               [120, 480, 6, 66],
               [480, 420, 6, 66],
               [180, 480, 246, 6],
               [300, 555, 6, 66],
               [120, 540, 126, 6],
               [360, 540, 126, 6]
               ]

    lista_parede = pygame.sprite.RenderPlain()
    for item in paredes:
        # ---- CRIA UM OBJETO PAREDE COM AS INFORMAÇÕES ANTERIORES ----
        parede = Parede((item[0], item[1]), (item[2], item[3]))
        lista_parede.add(parede)

    return lista_parede


class Pacman(pygame.sprite.Sprite):
    # ---- CONSTRUTOR CLASSE PACMAN ----
    # ---- SEM PARAMETROS ----
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.angulo = 0

        self.imagem = carrega_imagem("pacman.gif")
        self.imagem = pygame.transform.scale(self.imagem, (45, 45))
        self.rect = self.imagem.get_rect()
        self.rect.left = 278
        self.rect.top = 430

        self.vida = True

    # ---- FUNÇÃO DESENHA -----
    # ---- PARAMETROS: SUPERFICIE A SER DESENHADO ----
    def desenha(self, superficie):
        superficie.blit(self.imagem, self.rect)

    # ---- FUNÇÃO VIRA ----
    # ---- PARAMETROS: BOTÃO CLICADO ----
    def vira(self, event):
        if event.key == pygame.K_UP:
            self.angulo = (self.angulo * -1)
            self.imagem = pygame.transform.rotate(self.imagem, self.angulo)
            self.angulo = 90
            self.imagem = pygame.transform.rotate(self.imagem, self.angulo)
            self.x = 0
            self.y = -3
        if event.key == pygame.K_DOWN:
            self.angulo = (self.angulo * -1)
            self.imagem = pygame.transform.rotate(self.imagem, self.angulo)
            self.angulo = -90
            self.imagem = pygame.transform.rotate(self.imagem, self.angulo)
            self.x = 0
            self.y = 3
        if event.key == pygame.K_RIGHT:
            self.angulo = (self.angulo * -1)
            self.imagem = pygame.transform.rotate(self.imagem, self.angulo)
            self.angulo = 0
            self.imagem = pygame.transform.rotate(self.imagem, self.angulo)
            self.x = 3
            self.y = 0
        if event.key == pygame.K_LEFT:
            self.angulo = (self.angulo * -1)
            self.imagem = pygame.transform.rotate(self.imagem, self.angulo)
            self.angulo = 180
            self.imagem = pygame.transform.rotate(self.imagem, self.angulo)
            self.x = -3
            self.y = 0
        if event.key == pygame.K_SPACE:
            self.x = 0
            self.y = 0

    # ---- FUNÇÃO DE COLISAO ----
    # ---- PARAMETROS: OBJETO PARA COLIDIR
    def colide(self, obj):
        '''
        print("\n", self.rect.left)
        print(self.rect.top)
        '''

        old_x = self.rect.left
        xant = old_x + self.x
        self.rect.left = xant

        old_y = self.rect.top
        yant = old_y + self.y

        x_collide = pygame.sprite.spritecollide(self, obj, False)
        if x_collide:
            self.rect.left = old_x
        else:
            self.rect.top = yant
            y_collide = pygame.sprite.spritecollide(self, obj, False)
            if y_collide:
                self.rect.top = old_y

    # ---- FIM CLASSE PACMAN ----


class Bolinha(pygame.sprite.Sprite):
    # ---- CONSTRUTOR CLASSE BOLINHA ----
    # ---- PARAMETROS: COORDENADAS EM TUPLE ----
    def __init__(self, coor: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.imagem = carrega_imagem("bolinha.png")
        self.imagem = pygame.transform.scale(self.imagem, (30, 30))
        self.rect = self.imagem.get_rect()
        self.rect.left = coor[0]
        self.rect.top = coor[1]
        self.desenhar = True

    def desenha(self, superficie):
        if self.desenhar:
            superficie.blit(self.imagem, self.rect)

    def colide(self, obj):
        colide = pygame.sprite.spritecollide(self, obj, False)
        if colide:
            self.desenhar = False
            self.kill()

    # ---- FIM CLASSE BOLINHA ----


class Fantasma(pygame.sprite.Sprite):
    # ---- CONSTRUTOR CLASSE FANTASMA ----
    # ---- PARAMETROS: IMAGEM, COORDENADAS EM TUPLE ----
    def __init__(self, imagem, coor: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.imagem = carrega_imagem(imagem)
        # ---- TRANSFORMA O TAMANHO ----
        self.imagem = pygame.transform.scale(self.imagem, (30, 30))
        self.rect = self.imagem.get_rect()
        # ---- POSICIONA ----
        self.rect.centerx = coor[0]
        self.rect.centery = coor[1]

        # ---- SETA VARIAVEIS ----
        self.modo = True
        self.x = 0
        self.y = 0
        self.passou = False

    # ---- FUNÇÃO DESENHA ----
    # ---- PARAMETROS: SUPERFICIE A SER DESENHADA ----
    def desenha(self, superficie):
        superficie.blit(self.imagem, self.rect)

    # ---- FUNÇÃO SOBE ----
    # ---- SEM PARAMETROS ----
    # ---- UTILIZADA PARA TIRAR O FANTASMA DA GAIOLA ----
    def sobe(self):
        '''
        print("\n", self.rect.left, " ", 285)
        print(self.rect.top, " ", 182)
        '''

        if not self.passou:
            if self.rect.left == 285 and self.rect.top == 190:
                self.passou = True
            else:
                if self.rect.top > 190:
                    self.y = -1
                elif self.rect.top == 190:
                    self.y = 0

                if self.rect.left < 285:
                    self.x = 1

                elif self.rect.left > 285:
                    self.x = -1
                elif self.rect.left == 285:
                    self.x = 0

    # ---- FUNÇÃO ANDAR VERTICAL ----
    # ---- PARAMETROS: COORDENADA Y DO PACMAN ----
    def anda_y(self, coor):
        self.x = 0
        if coor > self.rect.top:
            self.y = 3.5
        else:
            self.y = -3.5

    # ---- FUNÇÃO ANDAR HORIZONTAL----
    # ---- PARAMETROS: COORDENADA X DO PACMAN ----
    def anda_x(self, coor):
        self.y = 0
        if coor > self.rect.left:
            self.x = 3.5
        else:
            self.x = -3.5

    # ---- FUNÇÃO DE COLISÃO ----
    # ---- PARAMETROS: OBJETO A SER COLIDIDO, COORDENADAS X E Y DO PACMAN ----
    def colide(self, obj, x, y):
        old_x = self.rect.left
        xant = old_x + self.x
        self.rect.left = xant

        old_y = self.rect.top
        yant = old_y + self.y

        x_collide = pygame.sprite.spritecollide(self, obj, False)
        # ---- VERIFICA COLISÃO EIXO X ----
        if x_collide:
            self.anda_y(y)
            self.rect.left = old_x
        else:
            self.rect.top = yant
            y_collide = pygame.sprite.spritecollide(self, obj, False)
            # ---- VERIFICA COLISÃO EIXO Y ----
            if y_collide:
                self.anda_x(x)
                self.rect.top = old_y

    def mata(self, obj):
        global gameover
        colide = pygame.sprite.spritecollide(self, obj, False)
        if colide:
            gameover = True
    # ---- FIM CLASSE FANTASMA ----


# ---- FUNÇÃO MAIN ----
# ---- USADA COMO FUNÇÃO PRINCIPAL ----
def main():
    inicia()
    sair = True
    global gameover, font_ganho, comeu
    comeu = 0

    # ---- CHAMA CLASSES ----
    pac = Pacman()
    paredes = faz_parede()
    tudo.add(paredes)
    pacman = [pac]
    bolinhas = [Bolinha((20, 555)), Bolinha((555, 555)), Bolinha((555, 20)), Bolinha((20, 20)), Bolinha((293, 320))]

    fantasmas = [Fantasma("fantasma_verde.png", (largura/2, (altura/2)-25))]

    while sair and not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                Pacman.vira(pac, event)
                if event.key == pygame.K_ESCAPE:
                    sair = False
            # ---- FIM FOR ----

        tela.fill((25, 25, 25))

        pac.colide(paredes)

        paredes.draw(tela)
        pac.desenha(tela)

        for fantasma in fantasmas:
            fantasma.desenha(tela)
            fantasma.sobe()
            fantasma.colide(tudo, pac.rect.left, pac.rect.top)
            fantasma.mata(pacman)

        for bolinha in bolinhas:
            bolinha.desenha(tela)
            bolinha.colide(pacman)
            if not bolinha.desenhar:
                bolinhas.remove(bolinha)
                comeu += 1

        # --- FRAMES ----
        global relogio
        relogio.tick(30)
        pygame.display.update()
        if comeu > 4:
            gameover = True

    # ---- FIM FUNÇÃO MAIN ----


main()

global font_ganho, comeu
print(comeu)

if comeu > 4:
    tela.fill((0,0,0))
    texto = font_ganho.render('Você venceu!', 1, (200, 200, 255))
    tela.blit(texto, (150, 250))
    pygame.display.update()
    time.sleep(3)
    print("YOU WIN")
else:
    tela.fill((0,0,0))
    texto = font_ganho.render('Gameover!', 1, (100, 200, 100))
    tela.blit(texto, (200, 250))
    pygame.display.update()
    time.sleep(3)

pygame.quit()
