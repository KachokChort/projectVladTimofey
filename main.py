import pygame
from load_image import load_image

pygame.init()

def main():
    clock = pygame.time.Clock()
    run = True
    FPS = 60


    infoObject = pygame.display.Info()
    dis_x = infoObject.current_w
    dis_y = infoObject.current_h
    dis = pygame.display.set_mode((dis_x, dis_y))
    pygame.display.set_caption("Wandering")

    fon_x = 0
    fon_y = 0

    player_x = dis_x // 2 - 50
    player_y = dis_y // 2 - 50
    player_speed = 8

    fon = load_image('fon.png')
    player = load_image('player.png')

    while run:
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            if dis_y // 2 - 100 > player_y and fon_y <= 0:
                fon_y += player_speed
            elif player_y > 0:
                player_y -= player_speed
        if key[pygame.K_s]:
            if dis_y // 2 + 100 < player_y and fon_y >= -(2160 - dis_y):
                fon_y -= player_speed
            elif player_y < 2060 + fon_y:
                player_y += player_speed
        if key[pygame.K_d]:
            if dis_x // 2 + 200 < player_x and fon_x >= -(3840 - dis_x):
                fon_x -= player_speed
            elif player_x < 3780 + fon_x:
                player_x += player_speed
        if key[pygame.K_a]:
            if dis_x // 2 - 200 > player_x and fon_x <= 0:
                fon_x += player_speed
            elif player_x > 0:
                player_x -= player_speed


        dis.fill('black')

        dis.blit(fon, (fon_x, fon_y))
        dis.blit(player, (player_x, player_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()