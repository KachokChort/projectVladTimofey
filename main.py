import pygame
from load_image import load_image, Field, Board, Inventory, Settings, Information, Market, Offer

pygame.init()

def main():
    wheat = ['wheat', 'wheap/wheat_2.png', 'wheap/wheat_1.png', 3, 'wheap/wheap_grains.png']
    carrot = ['carrot', 'carrot/carrot_1.png', 'carrot/carrot_2.png', 5, 'carrot/carrot_sprout.png']
    corn = ['corn', 'corn/corn2.png', 'corn/corn1.png', 5, 'corn/corn.png']
    pumpkin = ['pumpkin', 'pumpkin/pumpkin2.png', 'pumpkin/pumpkin1.png', 5, 'pumpkin/pumpkin.png']
    sunflower = ['sunflower', 'sunflower/sunflower2.png', 'sunflower/sunflower1.png', 5, 'sunflower/sunflower.png']
    tomato = ['tomato', 'tomato/tomato2.png', 'tomato/tomato1.png', 5, 'tomato/tomato.png']
    cucumber = ['cucumber', 'cucumber/cucumber2.png', 'cucumber/cucumber1.png', 5, 'cucumber/cucumber.png']

    plants_for_inventory = [wheat.copy(), carrot.copy(), corn.copy(), pumpkin.copy(), sunflower.copy(), tomato.copy(),
                            cucumber.copy()]

    plants_images = ['wheap/wheap_grains.png', 'carrot/carrot_sprout.png', 'corn/corn.png', 'pumpkin/pumpkin.png',
                     'sunflower/sunflower.png', 'tomato/tomato.png', 'cucumber/cucumber.png']

    main_plant = wheat.copy()

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
    player_speed = 20

    fon = load_image('fon.png')
    player = load_image('player.png')

    font = pygame.font.SysFont('Arial', 20)
    font1 = pygame.font.SysFont('Arial', 70)

    field = Field(10, 8)
    field.set_view(60, 50, 65, 67)
    plants = {}
    count = 0
    inventory = Inventory(5, 3, plants_for_inventory)
    inventory.set_view(275, 100, 270, 300)
    settings = Settings(1, 1)
    settings.set_view(1500, 750, 148, 148)
    info = Information(1, 1)
    info.set_view(1500, 750, 148, 148)
    offer1 = Offer(1, 1)
    offer1.set_view(528, 416, 720, 60)
    offer2 = Offer(1, 1)
    offer2.set_view(528, 516, 720, 60)
    offer3 = Offer(1, 1)
    offer3.set_view(528, 616, 720, 60)

    gameplay = True
    is_inventory = False
    is_settings = False
    is_info = False
    is_market = False


    while run:
        with open('balance.txt', 'r', encoding='utf-8') as f_in:
            balance = f_in.readlines()
        balance = "".join(balance)
        balance = int(balance)

        count += 1
        player_speed = 20

        dis.fill('black')
        dis.blit(fon, (fon_x, fon_y))

        key = pygame.key.get_pressed()

        if key[pygame.K_LSHIFT] and gameplay:
            player_speed = 7
        if key[pygame.K_w] and gameplay:
            if dis_y // 2 - 100 > player_y and fon_y <= 0:
                fon_y += player_speed
            elif player_y > 0:
                player_y -= player_speed
        if key[pygame.K_s] and gameplay:
            if dis_y // 2 + 100 < player_y and fon_y >= -(2160 - dis_y):
                fon_y -= player_speed
            elif player_y < 2060 + fon_y:
                player_y += player_speed
        if key[pygame.K_d] and gameplay:
            if dis_x // 2 + 100 < player_x and fon_x >= -(3840 - dis_x):
                fon_x -= player_speed
            elif player_x < 3780 + fon_x:
                player_x += player_speed
        if key[pygame.K_a] and gameplay:
            if dis_x // 2 - 100 > player_x and fon_x <= 0:
                fon_x += player_speed
            elif player_x > 0:
                player_x -= player_speed

        for plant in plants:
            plant = plants[plant]
            if plant:
                if plant.time - plant.count // FPS > 0:
                    dis.blit(font.render(f'{plant.time - plant.count // FPS}', False, 'white'), (plant.rect[0] + 30 + fon_x, plant.rect[1] + 37 + fon_y))
                dis.blit(plant.image, (plant.rect[0] + fon_x, plant.rect[1] + fon_y))
                plant.set_time()
                plant.count += 1

        if pygame.mouse.get_pressed()[0] and gameplay and main_plant:
            print(main_plant)
            pl = field.get_click(pygame.mouse.get_pos(), dis, plants, main_plant)
            if pl and pl[0] and pl[1]:
                plants[pl[1]] = pl[0]

        dis.blit(player, (player_x, player_y))
        dis.blit(load_image(main_plant[4]), (dis_x - 270, -50))


        if is_inventory:
            dis.blit(load_image('inventory.png'), (0, 0))
            inventory.render(dis)
            for x in range(inventory.width):
                for y in range(inventory.height):
                    try:
                        dis.blit(load_image(plants_images[x + y * inventory.width]) ,(x * inventory.cell_size_x + inventory.left, y * inventory.cell_size_y + inventory.top))
                    except IndexError:
                        pass
        if is_settings:
            dis.blit(load_image('settings.png'), (60, 30))
            dis.blit(load_image('exit.png'), (1500, 750))

        if is_market:
            dis.blit(load_image('market.png'), (0, 0))
            dis.blit(load_image('place.png'), (dis_x - 1550, -200))
            dis.blit(load_image('place.png'), (dis_x - 1550, -100))
            dis.blit(load_image('place.png'), (dis_x - 1550, 0))


        if is_info:
            dis.blit(load_image('info.png'), (60, 30))
            dis.blit(load_image('coin.png'), (dis_x - 630, 50))
            print(balance)
            dis.blit(font1.render(str(balance), 1, (0, 0, 0)), (dis_x - 400, 100))

        if pygame.mouse.get_pressed()[0] and is_inventory:
            if inventory.get_click(pygame.mouse.get_pos()):
                main_plant = inventory.get_click(pygame.mouse.get_pos())

        if pygame.mouse.get_pressed()[0] and is_settings:
            if settings.get_click(pygame.mouse.get_pos()):
                run = False



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and is_settings and not is_inventory:
                is_settings = False
                gameplay = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not is_settings:
                is_settings = True
                gameplay = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and gameplay and main_plant:
                pl = field.get_click(pygame.mouse.get_pos(), dis, plants, main_plant)
                if pl and pl[0] and pl[1]:
                    plants[pl[1]] = pl[0]

            if event.type == pygame.KEYDOWN and event.key == pygame.K_e and is_inventory:
                gameplay = True
                is_inventory = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and not is_inventory:
                gameplay = False
                is_inventory = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_t and is_market and not is_inventory:
                gameplay = True
                is_market = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_t and not is_market:
                gameplay = False
                is_market = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB and is_info and not is_inventory:
                gameplay = True
                is_info = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB and not is_info:
                gameplay = False
                is_info = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and is_market:
                if offer1.f(pygame.mouse.get_pos()):
                    f = open("balance.txt", 'w')
                    f.write(str(balance + 1))
                    f.close()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and is_market:
                if offer2.f(pygame.mouse.get_pos()):
                    f = open("balance.txt", 'w')
                    f.write(str(balance + 10))
                    f.close()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and is_market:
                if offer3.f(pygame.mouse.get_pos()):
                    f = open("balance.txt", 'w')
                    f.write(str(balance + 100))
                    f.close()


        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()