import pygame
from classi import Player

pygame.init()

screen=pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Fighters")

#fighting_ground=600

player1_image=pygame.image.load("image.png").convert_alpha()
player1_image=pygame.transform.scale(player1_image, (25,60))

player1=Player(player1_image, (100,600))
#player2=Player()

tasto = {'su': pygame.K_UP, 'giù': pygame.K_DOWN, 'sinistra': pygame.K_LEFT, 'destra': pygame.K_RIGHT}

game_running=True
clock=pygame.time.Clock()


while game_running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()
    player1.movimento(keys, tasto)

    screen.blit(player1.image, player1.rect)
    pygame.display.flip() 
    clock.tick(60)  # Cap the frame rate to 60 FPS

pygame.quit()
 