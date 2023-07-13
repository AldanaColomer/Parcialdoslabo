import pygame 
from game_logic import Game
from colores import Colores
from creacion_bloques import *
pygame.init() #-->Inicia pygame 

running = True

ventana = pygame.display.set_mode((500 , 620)) #-->Tamaño de la ventana
pygame.display.set_caption("TETRIS PYGAME")


game = Game()

timer = pygame.USEREVENT
pygame.time.set_timer(timer, 300)



while(running): #-->Bucle principal
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            print("El usuario salió del juego")
            running = False
        if(event.type == pygame.KEYDOWN):
            if(game.game_over == True):
                game.game_over = False
            if(event.key == pygame.K_LEFT and game.game_over == False):
                game.mover_izquierda()
            if(event.key == pygame.K_RIGHT and game.game_over == False):
                game.mover_derecha()
            if(event.key == pygame.K_DOWN and game.game_over == False):
                game.mover_abajo()
                game.actualizar_score(0,1)
            if (event.key == pygame.K_UP and game.game_over == False):
                game.rotar()
            if(event.key == pygame.K_SPACE):
                game.reset()
        if(event.type == timer and game.game_over == False):
            game.mover_abajo()
#Diseño de la pantalla:
    ventana.fill(Colores.AZUL_OSCURO)
    game.draw(ventana)
    
    fuente = pygame.font.SysFont("Impact" , 30)
    fuente_dos = pygame.font.SysFont("Impact" , 35)
    texto = fuente.render("SCORE", True, Colores.BLANCO)
    score_rect = pygame.Rect(320,55,170,60)
    score_value = fuente.render(str(game.score), True, Colores.BLANCO)
    pygame.draw.rect(ventana, Colores.AZUL_CLARO, score_rect, 0, 10)
    ventana.blit(score_value, score_value.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    ventana.blit(texto, (365, 20, 50,50))
    
    if(game.game_over == True):
        game_over_text = fuente_dos.render("GAME OVER", True, Colores.NEGRO)
        ventana.blit(game_over_text, (320,450,50,50))

    
    pygame.display.flip() #--> muestra todas las actualizaciones en la pantalla 

pygame.quit() #--> Cierra la ejecución del juego

