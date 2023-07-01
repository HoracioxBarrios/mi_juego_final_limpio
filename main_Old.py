import pygame
from utilidades import *
from configuracion import *
from class_world import *
from clase_personaje import Personaje
from clase_enemigo import Enemigo
from stage import Stage
from clase_proyectil import Proyectil
from clase_vida import BarraVida
from importlib import import_module
from modo.modo_dev import *

pygame.init()

ancho_pantalla = ANCHO_PANTALLA
alto_pantalla = ALTO_PANTALLA
fps = FPS
relog = pygame.time.Clock()
screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

running = True

bg_fondo = pygame.image.load("asset\game_background_1.png")
bg_fondo = pygame.transform.scale(bg_fondo, (ancho_pantalla, alto_pantalla))


world_data = leerJson('stages.json')
stage = world_data["stages"][0]["stage_1"]

# print(stage)

tile_size = 50
margen = 0
path_music_world = world_data["stages"][0]["musica_path"] 
world = StagePadre(stage, tile_size, 'asset\StoneBlock.png', screen, path_music_world)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)
flag = True

#Instancias
char_list = []
enemigo = Enemigo(screen, 800, 50, world.tile_list)
personaje = Personaje(500, 50, world.tile_list, screen, enemigo)
poder = Proyectil(1, personaje.rect.x, personaje.rect.y)
poder_list:list[Proyectil] = []
poder_list.append(poder)
stage = Stage()
sprites_personajes = pygame.sprite.Group()
sprites_personajes.add(personaje, enemigo)



while running:

    screen.blit(bg_fondo, (0, 0))
    lista_pisos =  world.draw()

    
    

    
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    #orden de verificación
        #gravedad
        #colision
        #incremento o decrementos de los rect en y, x
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_SPACE:
                personaje.acciones("saltar")
            elif evento.key == pygame.K_w:
                personaje.acciones("shot")
            elif evento.key == pygame.K_TAB:
               
                cambiar_modo()
                

    if get_modo():
        pygame.draw.rect(screen, (255, 255, 255), personaje.get_rect, 2)
        pygame.draw.rect(screen, (255, 255, 255), enemigo.get_rect, 2)
        pygame.draw.rect(screen, (255, 255, 255), personaje.poder.rect, 2)
        dibujar_grid(screen, BLANCO, tile_size, ancho_pantalla, alto_pantalla, 0)
    

    sprites_personajes.update(screen)
    sprites_personajes.draw(screen)

   

    pygame.display.update()

    delta_ms = relog.tick(FPS)
    
    
    personaje.delta_ms = delta_ms
    enemigo.delta_ms = delta_ms
    poder.delta_ms = delta_ms

pygame.quit()