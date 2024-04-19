import pygame
from  pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
x = 300
y = 200
#cores
branco = (255,255,255)
Azul =(0,0,255)


titulo = pygame.display.set_caption("Desenho do Quadrado")
tela = pygame.display.set_mode((largura,altura))

while True:
    tela.fill(branco) 
    for  event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.polygon(tela,Azul, [(220,200), (280,200), (280,260), (220,260)])
    pygame.display.flip()