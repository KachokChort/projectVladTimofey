import pygame
import random
from load_image import load_image, Field, Board, Inventory, Settings, Information, Market, Offer, resource

pygame.init()


def main():
    pygame.mixer.music.load('music_fon.mp3')
    pygame.mixer.music.play(-1)
    volume0 = 0.3

    wheat = ['wheap', 'wheap/wheat_2.png', 'wheap/wheat_1.png', 3, 'wheap/wheap_grains.png']
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

    all_products = ['carrot', 'corn', 'cucumber', 'pumpkin', 'sunflower', 'tomato', 'wheap', 'egg']

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
    font = pygame.font.SysFont('Arial', 20)
    font2 = pygame.font.SysFont('Arial', 80)
    font3 = pygame.font.SysFont('Arial', 40)

    field = Field(10, 8)
    field.set_view(60, 50, 65, 67)
    plants = {}
    count = 0
    inventory = Inventory(5, 3, plants_for_inventory)
    inventory.set_view(275, 100, 270, 300)
    settings = Settings(1, 1)
    settings.set_view(700, 700, 559, 215)
    volume1 = Settings(1, 1)
    volume1.set_view(20, 170, 225, 225)
    volume2 = Settings(1, 1)
    volume2.set_view(300, 170, 225, 225)
    info = Information(1, 1)
    info.set_view(1500, 750, 148, 148)
    offer1 = Offer(1, 1)
    offer1.set_view(528, 416, 720, 60)
    offer2 = Offer(1, 1)
    offer2.set_view(528, 516, 720, 60)
    offer3 = Offer(1, 1)
    offer3.set_view(528, 616, 720, 60)

    real_inventory = Inventory(8, 4, plants_for_inventory)
    real_inventory.set_view(10, 10, 238, 265)

    gameplay = True
    is_inventory = False
    is_settings = False
    is_info = False
    is_market = False
    is_real_inventory = False
    is_buy1 = False
    is_buy2 = False
    is_buy3 = False
    up = True
    down = True
    right = True
    left = True
    level1 = True
    level2 = False
    level3 = False
    level4 = False
    level5 = False
    bar = '5_8bar.png'
    bar1 = 5

    with open('offers.txt', 'r', encoding='utf-8') as f_in:
        ofer = f_in.readlines()
    ofer = "".join(ofer)
    ofer = ofer.split()

    print(ofer)
    with open('inventory_.txt', 'r', encoding='utf-8') as f_in:
        inventory1 = f_in.readlines()
    inventory1 = "".join(inventory1)
    inventory1 = inventory1.split('&')
    products1 = []
    numproducts = []
    for i in inventory1:
        products1.append(i.split('=')[0])
        numproducts.append(int(i.split('=')[1]))

    while run:
        pygame.mixer.music.set_volume(volume0)
        with open('balance.txt', 'r', encoding='utf-8') as f_in:
            balance = f_in.readlines()
        balance = "".join(balance)
        balance = int(balance)
        with open('stats.txt', 'r', encoding='utf-8') as f_in:
            stats = f_in.readlines()
        stats = "".join(stats)
        stats = int(stats)


        count += 1
        player_speed = 20

        dis.fill('black')
        dis.blit(fon, (fon_x, fon_y))

        key = pygame.key.get_pressed()

        if key[pygame.K_LSHIFT] and gameplay:
            player_speed = 7
        if (key[pygame.K_w] or key[pygame.K_UP]) and gameplay:
            if dis_y // 2 - 100 > player_y and fon_y <= 0:
                fon_y += player_speed
            elif player_y > 0:
                player_y -= player_speed
        if (key[pygame.K_s] or key[pygame.K_DOWN]) and gameplay:
            if dis_y // 2 + 100 < player_y and fon_y >= -(2160 - dis_y):
                fon_y -= player_speed
            elif player_y < 2060 + fon_y:
                player_y += player_speed
        if (key[pygame.K_d] or key[pygame.K_RIGHT]) and gameplay:
            if dis_x // 2 + 100 < player_x and fon_x >= -(3840 - dis_x):
                fon_x -= player_speed
            elif player_x < 3780 + fon_x:
                player_x += player_speed
        if (key[pygame.K_a] or key[pygame.K_LEFT]) and gameplay:
            if dis_x // 2 - 100 > player_x and fon_x <= 0:
                fon_x += player_speed
            elif player_x > 0:
                player_x -= player_speed


        for plant in plants:
            plant = plants[plant]
            if plant:
                if plant.time - plant.count // FPS > 0:
                    dis.blit(font.render(f'{plant.time - plant.count // FPS}', False, 'white'),
                             (plant.rect[0] + 30 + fon_x, plant.rect[1] + 37 + fon_y))
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
                        dis.blit(load_image(plants_images[x + y * inventory.width]), (
                        x * inventory.cell_size_x + inventory.left, y * inventory.cell_size_y + inventory.top))
                    except IndexError:
                        pass
        if is_settings:
            dis.blit(load_image('settings.png'), (60, 30))
            dis.blit(load_image('sound.png'), (150, 30))
            dis.blit(load_image(bar), (150, 170))
            dis.blit(load_image('+.png'), (300, 170))
            dis.blit(load_image('-.png'), (20, 170))
            dis.blit(load_image('exit.png'), (700, 700))

        if is_market:
            with open('ofersss.txt', 'r', encoding='utf-8') as f_in:
                ofers = f_in.readlines()
            ofers = "".join(ofers)
            ofers = ofers.split()
            offers1 = ofers[0]
            offers2 = ofers[1]
            offers3 = ofers[2]
            dis.blit(load_image('market.png'), (0, 0))
            dis.blit(load_image(offers1), (dis_x - 1550, -200))
            dis.blit(load_image(offers2), (dis_x - 1550, -100))
            dis.blit(load_image(offers3), (dis_x - 1550, 0))

        if is_info:
            dis.blit(load_image('info.png'), (60, 30))
            dis.blit(load_image('coin.png'), (dis_x - 630, 50))
            dis.blit(load_image('button_stats_market.png'), (dis_x - 1800, 50))
            print(balance)
            dis.blit(font1.render(str(balance), 1, (0, 0, 0)), (dis_x - 400, 100))
            dis.blit(font1.render(str(stats), 1, (0, 0, 0)), (dis_x - 1250, 125))

        if pygame.mouse.get_pressed()[0] and is_inventory:
            if inventory.get_click(pygame.mouse.get_pos()):
                main_plant = inventory.get_click(pygame.mouse.get_pos())

        if pygame.mouse.get_pressed()[0] and is_settings:
            if settings.get_click(pygame.mouse.get_pos()):
                run = False



        # отображение реал инвенторя
        if is_real_inventory:
            dis.blit(load_image('fon_inventory.png'), (0, 0))
            real_inventory.render(dis)
            for x in range(real_inventory.width):
                for y in range(real_inventory.height):
                    try:
                        print(resource.resourses[all_products[x + y * real_inventory.width]])
                        dis.blit(
                            font3.render(
                                f'{all_products[x + y * real_inventory.width]}',
                                False, 'black'), (
                                x * real_inventory.cell_size_x + real_inventory.left,
                                y * real_inventory.cell_size_y + real_inventory.top))
                        dis.blit(
                            font3.render(
                                f'{resource.resourses[all_products[x + y * real_inventory.width]]}',
                                False, 'black'), (
                                x * real_inventory.cell_size_x + real_inventory.left,
                                y * real_inventory.cell_size_y + real_inventory.top + 40))
                    except TypeError:
                        pass
                    except IndexError:
                        pass

        if is_buy1 or is_buy2 or is_buy3:
            f1 = open("stats.txt", 'w')
            if is_buy1:
                kords = (dis_x - 1550, -200)
                offers = offers1
            elif is_buy2:
                kords = (dis_x - 1550, -100)
                offers = offers2
            elif is_buy3:
                kords = (dis_x - 1550, 0)
                offers = offers3
            if offers == 'place1.png':
                if numproducts[0] >= 20:
                    numproducts[0] -= 20
                    f = open("balance.txt", 'w')
                    f.write(str(balance + 10))
                    f1.write(str(stats + 1))
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place2.png':
                if numproducts[1] >= 20:
                    numproducts[1] -= 20
                    f = open("balance.txt", 'w')
                    f.write(str(balance + 10))
                    f1.write(str(stats + 1))
                    f.close()
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place3.png':
                if numproducts[2] >= 20:
                    numproducts[2] -= 20
                    f = open("balance.txt", 'w')
                    f.write(str(balance + 10))
                    f1.write(str(stats + 1))
                    f.close()
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place4.png':
                if numproducts[3] >= 20:
                    numproducts[3] -= 20
                    f = open("balance.txt", 'w')
                    f.write(str(balance + 20))
                    f1.write(str(stats + 1))
                    f.close()
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place5.png':
                if numproducts[4] >= 20:
                    numproducts[4] -= 20
                    f = open("balance.txt", 'w')
                    f.write(str(balance + 20))
                    f1.write(str(stats + 1))
                    f.close()
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place6.png':
                if numproducts[5] >= 20:
                    numproducts[5] -= 20
                    f = open("balance.txt", 'w')
                    f.write(str(balance + 20))
                    f1.write(str(stats + 1))
                    f.close()
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place7.png':
                if numproducts[6] >= 20:
                    numproducts[6] -= 20
                    f = open("balance.txt", 'w')
                    f.write(str(balance + 20))
                    f1.write(str(stats + 1))
                    f.close()
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place8.png':
                if numproducts[6] >= 20 and numproducts[3] >= 5:
                    numproducts[6] -= 20
                    numproducts[3] -= 5
                    f = open("balance.txt", 'w')
                    f.write(str(balance + 50))
                    f1.write(str(stats + 1))
                    f.close()
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place9.png':
                if numproducts[4] >= 20 and numproducts[5] >= 30:
                    numproducts[4] -= 20
                    numproducts[5] -= 30
                    f = open("balance.txt", 'w')
                    f.write(str(balance + 120))
                    f1.write(str(stats + 1))
                    f.close()
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if is_buy1:
                f = open("ofersss.txt", 'w')
                f.write(f'{offers}\n')
                f.write(f'{offers2}\n')
                f.write(offers3)
                f.close()
            elif is_buy2:
                f = open("ofersss.txt", 'w')
                f.write(f'{offers1}\n')
                f.write(f'{offers}\n')
                f.write(offers3)
                f.close()
            elif is_buy3:
                f = open("ofersss.txt", 'w')
                f.write(f'{offers1}\n')
                f.write(f'{offers2}\n')
                f.write(offers)
                f.close()
            f1.close()
            f = open("inventory_.txt", 'w')
            f.write(
                f'{products1[0]}={numproducts[0]}&{products1[1]}={numproducts[1]}&{products1[2]}={numproducts[2]}&{products1[3]}={numproducts[3]}&{products1[4]}={numproducts[4]}&{products1[5]}={numproducts[5]}&{products1[6]}={numproducts[6]}')
            f.close()
            is_buy1 = False
            is_buy2 = False
            is_buy3 = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for i in resource.resourses:
                    print(f'{i}: {resource.resourses[i]}')
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

            if event.type == pygame.MOUSEBUTTONDOWN and is_settings:
                if volume1.get_click(pygame.mouse.get_pos()):
                    print(bar1, '-')
                    if bar1 > 0:
                        bar = f'{bar1 - 1}_8bar.png'
                        bar1 -= 1
                        volume0 -= 0.06

            if event.type == pygame.MOUSEBUTTONDOWN and is_settings:
                if volume2.get_click(pygame.mouse.get_pos()):
                    print(bar1, '+')
                    if bar1 < 8:
                        bar = f'{bar1 + 1}_8bar.png'
                        bar1 += 1
                        volume0 += 0.06

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
                    is_buy1 = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and is_market:
                if offer2.f(pygame.mouse.get_pos()):
                    is_buy2 = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and is_market:
                if offer3.f(pygame.mouse.get_pos()):
                    is_buy3 = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_b and is_real_inventory:
                gameplay = True
                is_real_inventory = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b and not is_real_inventory and gameplay:
                gameplay = False
                is_real_inventory = True

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
