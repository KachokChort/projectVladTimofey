import pygame
from load_image import load_image, Board, Inventory

pygame.init()

def main():
    clock = pygame.time.Clock()
    run = True
    FPS = 60
    mark_1 = 0

    infoObject = pygame.display.Info()
    dis_x = infoObject.current_w
    dis_y = infoObject.current_h
    dis = pygame.display.set_mode((dis_x, dis_y))
    pygame.display.set_caption("Wandering")

    fon_x = 0
    fon_y = 0

    player_x = dis_x // 2 - 50
    player_y = dis_y // 2 - 50
    player_speed = 4

    fon = load_image('fon.png')
    player = load_image('player.png')

    font = pygame.font.SysFont('Arial', 20)

    field = Board(10, 8)
    field.set_view(60, 50, 65, 67)
    plants = []
    count = 0

    while run:
        count += 1
        player_speed = 4

        dis.fill('black')
        dis.blit(fon, (fon_x, fon_y))

        key = pygame.key.get_pressed()

        if key[pygame.K_LSHIFT]:
            player_speed = 7
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
            if dis_x // 2 + 100 < player_x and fon_x >= -(3840 - dis_x):
                fon_x -= player_speed
            elif player_x < 3780 + fon_x:
                player_x += player_speed
        if key[pygame.K_a]:
            if dis_x // 2 - 100 > player_x and fon_x <= 0:
                fon_x += player_speed
            elif player_x > 0:
                player_x -= player_speed

        if key[pygame.K_e]:
            if mark_1 == 0:
                Inventory()
                mark_1 = 1
            elif mark_1 == 1:
                Inventory()
                mark_1 = 1

        for plant in plants:
            if plant:
                if plant.time - plant.count // FPS > 0:
                    plant.count += 1
                    dis.blit(font.render(f'{plant.time - plant.count // FPS}', False, 'white'), (plant.rect[0] + 30, plant.rect[1] + 37))
                    dis.blit(plant.first_image, plant.rect)
                else:
                    dis.blit(font.render('', False, 'green'), (plant.rect[0] + 30, plant.rect[1] + 37))
                    dis.blit(plant.image, plant.rect)

        if pygame.mouse.get_pressed()[0]:
            plants.append(field.get_click(pygame.mouse.get_pos(), dis))

        dis.blit(player, (player_x, player_y))

        # field.render(dis)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                plants.append(field.get_click(pygame.mouse.get_pos(), dis))

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()