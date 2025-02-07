import pygame
import random
from load_image import load_image, Field, Inventory, Animal_House, resource, Hero, Lake, safe_resourses, Settings, Information, Market, Offer, AnimatedSprite

pygame.init()


def wr(ba, stats, bal):
    f1 = open("stats.txt", 'w')
    f1.write(str(stats + 1))
    f1.close()
    f = open("balance.txt", 'w')
    f.write(str(ba + bal))
    f.close()


def main():
    pygame.mixer.music.load('music_fon.mp3')
    pygame.mixer.music.play(-1)
    volume0 = 0.3

    wheat = ['wheap', 'wheap/wheat_2.png', 'wheap/wheat_1.png', 3, 'wheap/wheap_grains.png']
    carrot = ['carrot', 'carrot/carrot_1.png', 'carrot/carrot_2.png', 5, 'carrot/carrot_sprout.png']
    corn = ['corn', 'corn/corn2.png', 'corn/corn1.png', 7, 'corn/corn.png']
    pumpkin = ['pumpkin', 'pumpkin/pumpkin2.png', 'pumpkin/pumpkin1.png', 9, 'pumpkin/pumpkin.png']
    sunflower = ['sunflower', 'sunflower/sunflower2.png', 'sunflower/sunflower1.png', 11, 'sunflower/sunflower.png']
    tomato = ['tomato', 'tomato/tomato2.png', 'tomato/tomato1.png', 13, 'tomato/tomato.png']
    cucumber = ['cucumber', 'cucumber/cucumber2.png', 'cucumber/cucumber1.png', 15, 'cucumber/cucumber.png']

    plants_for_inventory = [wheat.copy(), carrot.copy(), corn.copy(), pumpkin.copy(), sunflower.copy(), tomato.copy(),
                            cucumber.copy()]

    plants_images = ['wheap/wheap_grains.png', 'carrot/carrot_sprout.png', 'corn/corn.png', 'pumpkin/pumpkin.png',
                     'sunflower/sunflower.png', 'tomato/tomato.png', 'cucumber/cucumber.png']

    river = [load_image('river/river1.png', 1), load_image('river/river1.png', 1), load_image('river/river1.png', 1)]
    river_count = 0

    main_plant = wheat.copy()

    all_products = ['carrot', 'corn', 'cucumber', 'pumpkin', 'sunflower', 'tomato', 'wheap', 'egg', 'milk']

    clock = pygame.time.Clock()
    run = True
    FPS = 30

    statics = {'carrot': 0, 'corn': 0, 'cucumber': 0, 'pumpkin': 0, 'sunflower': 0, 'tomato': 0, 'wheap': 0, 'egg': 0,
               'milk': 0}

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
    chiken_house_fon = load_image('fon_chiken.png')

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
    chiken_house = Animal_House(4, 2, 'chiken', 'chiken2.png', 'chiken.png')
    chiken_house.set_view(150, 120, 400, 400)
    cow_house = Animal_House(4, 2, 'cow', 'cow2.png', 'cow.png')
    cow_house.set_view(150, 120, 400, 400)
    real_inventory = Inventory(8, 4, plants_for_inventory)
    real_inventory.set_view(10, 10, 238, 265)
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
    start = Settings(1, 1)
    start.set_view(700, 280, 516, 280)

    all_sprites = pygame.sprite.Group()

    hero = Hero(all_sprites, (player_x, player_y))

    is_inventory = False
    stas = False
    is_chiken_house = False
    is_real_inventory = False
    is_cow_house = False
    gameplay = False
    is_settings = False
    is_info = False
    is_market = False
    is_buy1 = False
    is_buy2 = False
    is_buy3 = False
    with open('levels.txt', 'r', encoding='utf-8') as f_in:
        levels = f_in.readlines()
    levels = "".join(levels)
    levels = levels.split()
    print(levels)
    if levels[0] == 'True':
        level1 = True
    else:
        level1 = False
    if levels[1] == 'True':
        level2 = True
    else:
        level2 = False
    if levels[2] == 'True':
        level3 = True
    else:
        level3 = False
    if levels[3] == 'True':
        level4 = True
    else:
        level4 = False
    if levels[4] == 'True':
        level5 = True
    else:
        level5 = False
    if levels[5] == 'True':
        level6 = True
    else:
        level6 = False
    if levels[6] == 'True':
        level7 = True
    else:
        level7 = False
    levels1 = [level1, level2, level3, level4, level5, level6, level7]
    bar = '5_8bar.png'
    bar1 = 5

    if level1:
        with open('offers_level_1.txt', 'r', encoding='utf-8') as f_in:
            ofer = f_in.readlines()
        ofer = "".join(ofer)
        ofer = ofer.split()
    if level2:
        with open('offers_level_2.txt', 'r', encoding='utf-8') as f_in:
            ofer = f_in.readlines()
        ofer = "".join(ofer)
        ofer = ofer.split()
    if level3:
        with open('offers_level_3.txt', 'r', encoding='utf-8') as f_in:
            ofer = f_in.readlines()
        ofer = "".join(ofer)
        ofer = ofer.split()
    if level4:
        with open('offers_level_4.txt', 'r', encoding='utf-8') as f_in:
            ofer = f_in.readlines()
        ofer = "".join(ofer)
        ofer = ofer.split()
    if level5:
        with open('offers_level_5.txt', 'r', encoding='utf-8') as f_in:
            ofer = f_in.readlines()
        ofer = "".join(ofer)
        ofer = ofer.split()

    with open('stats2.txt', 'r', encoding='utf-8') as f_in:
        steps = f_in.readlines()
    steps = "".join(steps)
    steps = int(steps)

    lake_rect = pygame.rect.Rect(2000 + fon_x, 1000 + fon_y, 1000, 1000)
    lake = load_image('river/river1.png')
    lakee = Lake(all_sprites, lake_rect)

    is_locked = {0: level1, 1: level1, 2: level1, 3: level2, 4: level3, 5: level4, 6: level5, 'chik': level6,
                 'cow': level7}
    with open('inventory_.txt', 'r', encoding='utf-8') as f_in:
        inventory1 = f_in.readlines()
    inventory1 = "".join(inventory1)
    inventory1 = inventory1.split('&')
    for i in inventory1:
        resource.resourses[i.split('=')[0]] = int(i.split('=')[1])

    is_go = False
    
    while run:
        is_locked = {0: level1, 1: level1, 2: level1, 3: level2, 4: level3, 5: level4, 6: level5, 'chik': level6,
                     'cow': level7}
        pygame.mixer.music.set_volume(volume0)
        with open('balance.txt', 'r', encoding='utf-8') as f_in:
            balance = f_in.readlines()
        balance = "".join(balance)
        balance = int(balance)
        with open('stats.txt', 'r', encoding='utf-8') as f_in:
            stats = f_in.readlines()
        stats = "".join(stats)
        stats = int(stats)
        # переменные, которые нужно изменять во время игры
        chiken_house_rect = pygame.rect.Rect(125 + fon_x, 760 + fon_y, 500, 500)
        cow_house_rect = pygame.rect.Rect(125 + fon_x, 1500 + fon_y, 650, 600)
        lake_rect = pygame.rect.Rect(2000 + fon_x, 1000 + fon_y, 1000, 1000)
        field.set_view(60 + fon_x, 50 + fon_y, 65, 67)
        lakee.set_rect(lake_rect)

        count += 1
        player_speed = 20

        dis.fill('black')
        dis.blit(fon, (fon_x, fon_y))

        key = pygame.key.get_pressed()

        if key[pygame.K_LSHIFT] and gameplay:
            player_speed = 7
        if (key[pygame.K_w] or key[pygame.K_UP]) and gameplay:
            is_go = True
            if dis_y // 2 - 100 > hero.rect.y and fon_y <= 0:
                fon_y += player_speed
                steps += 1
                if hero.is_col(lakee):
                    fon_y -= player_speed
            elif hero.rect.y > 0:
                hero.update((0, -player_speed), lakee)
        if (key[pygame.K_s] or key[pygame.K_DOWN]) and gameplay:
            is_go = True
            if dis_y // 2 + 100 < hero.rect.y and fon_y >= -(2160 - dis_y):
                fon_y -= player_speed
                steps += 1
                if hero.is_col(lakee):
                    fon_y += player_speed
            elif hero.rect.y < 2060 + fon_y:
                hero.update((0, player_speed), lakee)
        if (key[pygame.K_d] or key[pygame.K_RIGHT]) and gameplay:
            is_go = True
            if dis_x // 2 + 100 < hero.rect.x and fon_x >= -(3840 - dis_x):
                fon_x -= player_speed
                steps += 1
                if hero.is_col(lakee):
                    fon_x += player_speed
            elif hero.rect.x < 3780 + fon_x:
                hero.update((player_speed, 0), lakee)
        if (key[pygame.K_a] or key[pygame.K_LEFT]) and gameplay:
            is_go = True
            if dis_x // 2 - 100 > hero.rect.x and fon_x <= 0:
                fon_x += player_speed
                steps += 1
                if hero.is_col(lakee):
                    fon_x -= player_speed
            elif hero.rect.x > 0:
                hero.update((-player_speed, 0), lakee)

        if is_go:
            if count % 5 == 0:
                hero.set_image()

        is_go = False

        if not gameplay:
            dis.blit(load_image('market.png'), (0, 0))
            dis.blit(load_image('start_game.png'), (700, 280))
        # отловка нажатий на дoма зверей
        if pygame.mouse.get_pressed()[0] and gameplay:
            if chiken_house_rect.collidepoint(pygame.mouse.get_pos()) and is_locked['chik']:
                # print('yes')
                gameplay = False
                is_inventory = False
                is_cow_house = False
                is_chiken_house = True
            elif not is_locked['chik'] and balance >= 120 and chiken_house_rect.collidepoint(pygame.mouse.get_pos()):
                level6 = True
                f = open("balance.txt", 'w')
                f.write(str(balance - 120))
                f.close()
                f = open("levels.txt", 'w')
                f.write(f'{str(level1)}\n')
                f.write(f'{str(level2)}\n')
                f.write(f'{str(level3)}\n')
                f.write(f'{str(level4)}\n')
                f.write(f'{str(level5)}\n')
                f.write(f'{str(level6)}\n')
                f.write(f'{str(level7)}\n')
                f.close()
            if cow_house_rect.collidepoint(pygame.mouse.get_pos()) and is_locked['cow']:
                # print('yes')
                gameplay = False
                is_inventory = False
                is_chiken_house = False
                is_cow_house = True
            elif not is_locked['cow'] and balance >= 170 and cow_house_rect.collidepoint(pygame.mouse.get_pos()):
                level7 = True
                f = open("balance.txt", 'w')
                f.write(str(balance - 170))
                f.close()
                f = open("levels.txt", 'w')
                f.write(f'{str(level1)}\n')
                f.write(f'{str(level2)}\n')
                f.write(f'{str(level3)}\n')
                f.write(f'{str(level4)}\n')
                f.write(f'{str(level5)}\n')
                f.write(f'{str(level6)}\n')
                f.write(f'{str(level7)}\n')
                f.close()

        # отображение всего на карте
        dis.fill('black')
        dis.blit(fon, (fon_x, fon_y))

        # отображение растений на поле
        for plant in plants:
            p = plant
            plant = plants[p]
            if plant:
                if plant.time - plant.count // FPS > 0:
                    dis.blit(font.render(f'{plant.time - plant.count // FPS}', False, 'white'),
                             (p[0] * field.cell_size_x + field.left + 30, p[1] * field.cell_size_y + field.top + 37))
                dis.blit(plant.image, (p[0] * field.cell_size_x + field.left, p[1] * field.cell_size_y + field.top))
                plant.set_time()
                plant.count += 1

        all_sprites.draw(dis)
        dis.blit(load_image(main_plant[4]), (dis_x - 270, -50))
        if not gameplay and not stas:
            dis.blit(load_image('market.png'), (0, 0))
            dis.blit(load_image('start_game.png'), (700, 280))
        else:
            stas = True
        # отображение реки
        # if river_count / 20 == 2:
        #     river_count = 0
        # river_count += 1
        # dis.blit(river[river_count // 20], (fon_x, fon_y))

        if not is_locked['chik'] and gameplay:
            dis.blit(load_image('lock2.png'), chiken_house_rect)
            dis.blit(font1.render(str(120), 1, (0, 0, 0)), chiken_house_rect)

        if not is_locked['cow'] and gameplay:
            dis.blit(load_image('lock2.png'), cow_house_rect)
            dis.blit(font1.render(str(170), 1, (0, 0, 0)), cow_house_rect)

        dis.blit(lake, lake_rect)
        if is_settings:
            dis.blit(load_image('settings.png'), (60, 30))
            dis.blit(load_image('eternal_ranch.png'), (800, -180))
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
            dis.blit(load_image('button_stats_market.png'), (dis_x - 1800, 50))
            dis.blit(load_image('button_steps.png'), (dis_x - 1800, 350))
            dis.blit(load_image('coin.png'), (dis_x - 600, 100))
            dis.blit(font1.render(str(steps), 1, (0, 0, 0)), (dis_x - 1250, 425))
            print(balance)
            dis.blit(font1.render(str(balance), 1, (0, 0, 0)), (dis_x - 400, 100))
            dis.blit(font1.render(str(stats), 1, (0, 0, 0)), (dis_x - 1250, 125))

        if pygame.mouse.get_pressed()[0] and is_settings:
            if settings.get_click(pygame.mouse.get_pos()):
                run = False

        # отображение и инициализация курятника
        if is_chiken_house:
            dis.blit(chiken_house_fon, (0, 0))
            chiken_house.render(dis)
            for i in range(chiken_house.width):
                for j in range(chiken_house.height):
                    chik = chiken_house.board[i][j]
                    chiken_image = load_image(chik.image)
                    chik.count += 1
                    if chik.count < chik.FPS * chik.time:
                        dis.blit(font2.render(f'{chik.time - chik.count // FPS - 1}.{FPS - chik.count % FPS}', False,
                                              'black'), (
                                     i * chiken_house.cell_size_x + chiken_house.left,
                                     j * chiken_house.cell_size_y + chiken_house.top))
                    else:
                        chik.image = chik.first_image
                    if chik.count == chik.FPS * chik.time:
                        resource.resourses['egg'] += 1
                    dis.blit(chiken_image, (
                        i * chiken_house.cell_size_x + chiken_house.left,
                        j * chiken_house.cell_size_y + chiken_house.top))
            if pygame.mouse.get_pressed()[0]:
                chiken_house.get_click(pygame.mouse.get_pos())

        # отображение и инициализация курятника
        if is_cow_house:
            dis.blit(chiken_house_fon, (0, 0))
            cow_house.render(dis)
            for i in range(cow_house.width):
                for j in range(cow_house.height):
                    cow = cow_house.board[i][j]
                    cow_image = load_image(cow.image)
                    cow.count += 1
                    if cow.count < cow.FPS * cow.time:
                        dis.blit(
                            font2.render(f'{cow.time - cow.count // FPS - 1}.{FPS - cow.count % FPS}', False,
                                         'black'), (
                                i * cow_house.cell_size_x + cow_house.left,
                                j * cow_house.cell_size_y + cow_house.top))
                    else:
                        cow.image = cow.first_image
                    if cow.count == cow.FPS * cow.time:
                        resource.resourses['milk'] += 1
                    dis.blit(cow_image, (
                        i * cow_house.cell_size_x + cow_house.left,
                        j * cow_house.cell_size_y + cow_house.top))
            if pygame.mouse.get_pressed()[0]:
                cow_house.get_click(pygame.mouse.get_pos())

        # отображение иинициализация инвенторя
        if is_inventory:
            dis.blit(load_image('inventory.png'), (0, 0))
            inventory.render(dis)
            is_locked = {0: level1, 1: level1, 2: level1, 3: level2, 4: level3, 5: level4, 6: level5, 'chik': level6,
                         'cow': level7}
            for x in range(inventory.width):
                for y in range(inventory.height):
                    try:
                        dis.blit(load_image(plants_images[x + y * inventory.width]), (
                            x * inventory.cell_size_x + inventory.left, y * inventory.cell_size_y + inventory.top))
                        if not is_locked[x + y * inventory.width]:
                            print(is_locked)
                            dis.blit(load_image('lock.png'), (
                                x * inventory.cell_size_x + inventory.left, y * inventory.cell_size_y + inventory.top))
                            dis.blit(font1.render(str(70), 1, (0, 0, 0)), (
                                x * inventory.cell_size_x + inventory.left, y * inventory.cell_size_y + inventory.top))
                    except IndexError:
                        pass

            # инициализация нажатий в инвенторе
            if pygame.mouse.get_pressed()[0]:
                r = inventory.get_cell(pygame.mouse.get_pos())
                r = r[0] + r[1] * inventory.width
                r = is_locked[r]
                if inventory.get_click(pygame.mouse.get_pos()) and r:
                    main_plant = inventory.get_click(pygame.mouse.get_pos())
                elif not r and inventory.get_click(pygame.mouse.get_pos()) and balance >= 70:
                    if inventory.get_cell(pygame.mouse.get_pos())[0] + inventory.get_cell(pygame.mouse.get_pos())[1] * inventory.width == 3:
                        level2 = True
                    elif inventory.get_cell(pygame.mouse.get_pos())[0] + inventory.get_cell(pygame.mouse.get_pos())[1] * inventory.width == 4:
                        level3 = True
                    elif inventory.get_cell(pygame.mouse.get_pos())[0] + inventory.get_cell(pygame.mouse.get_pos())[1] * inventory.width == 5:
                        level4 = True
                    elif inventory.get_cell(pygame.mouse.get_pos())[0] + inventory.get_cell(pygame.mouse.get_pos())[1] * inventory.width == 6:
                        level5 = True
                    f = open("balance.txt", 'w')
                    f.write(str(balance - 70))
                    f.close()
                    f = open("levels.txt", 'w')
                    f.write(f'{str(level1)}\n')
                    f.write(f'{str(level2)}\n')
                    f.write(f'{str(level3)}\n')
                    f.write(f'{str(level4)}\n')
                    f.write(f'{str(level5)}\n')
                    f.write(f'{str(level6)}\n')
                    f.write(f'{str(level7)}\n')
                    f.close()


        if is_buy1 or is_buy2 or is_buy3:
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
                if resource.resourses[all_products[0]] >= 20:
                    wr(balance, stats, 10)
                    resource.resourses[all_products[0]] -= 20
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place2.png':
                if resource.resourses[all_products[1]] >= 20:
                    resource.resourses[all_products[1]] -= 20
                    wr(balance, stats, 10)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place3.png':
                if resource.resourses[all_products[2]] >= 20:
                    resource.resourses[all_products[2]] -= 20
                    wr(balance, stats, 10)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place4.png':
                if resource.resourses[all_products[3]] >= 20:
                    resource.resourses[all_products[3]] -= 20
                    wr(balance, stats, 20)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place5.png':
                if resource.resourses[all_products[4]] >= 20:
                    resource.resourses[all_products[4]] -= 20
                    wr(balance, stats, 20)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place6.png':
                if resource.resourses[all_products[5]] >= 20:
                    resource.resourses[all_products[5]] -= 20
                    wr(balance, stats, 20)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place7.png':
                if resource.resourses[all_products[6]] >= 20:
                    resource.resourses[all_products[6]] -= 20
                    wr(balance, stats, 20)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place8.png':
                if resource.resourses[all_products[6]] >= 20 and resource.resourses[all_products[3]] >= 5:
                    resource.resourses[all_products[6]] -= 20
                    resource.resourses[all_products[3]] -= 5
                    wr(balance, stats, 50)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            elif offers == 'place9.png':
                if resource.resourses[all_products[4]] >= 20 and resource.resourses[all_products[5]] >= 30:
                    resource.resourses[all_products[4]] -= 20
                    resource.resourses[all_products[5]] -= 30
                    wr(balance, stats, 120)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place1cw.png':
                if resource.resourses[all_products[0]] >= 17 and resource.resourses[all_products[6]] >= 17:
                    resource.resourses[all_products[0]] -= 17
                    resource.resourses[all_products[6]] -= 17
                    wr(balance, stats, 40)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place1k.png':
                if resource.resourses[all_products[1]] >= 25:
                    resource.resourses[all_products[1]] -= 25
                    wr(balance, stats, 30)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place1w.png':
                if resource.resourses[all_products[6]] >= 30:
                    resource.resourses[all_products[6]] -= 30
                    wr(balance, stats, 40)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place2c.png':
                if resource.resourses[all_products[0]] >= 15:
                    resource.resourses[all_products[0]] -= 15
                    wr(balance, stats, 15)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place2k.png':
                if resource.resourses[all_products[1]] >= 17:
                    resource.resourses[all_products[1]] -= 17
                    wr(balance, stats, 23)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place2w.png':
                if resource.resourses[all_products[6]] >= 13:
                    resource.resourses[all_products[6]] -= 13
                    wr(balance, stats, 15)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place3c.png':
                if resource.resourses[all_products[0]] >= 30:
                    resource.resourses[all_products[0]] -= 30
                    wr(balance, stats, 35)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place3k.png':
                if resource.resourses[all_products[1]] >= 5:
                    resource.resourses[all_products[1]] -= 5
                    wr(balance, stats, 7)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place3w.png':
                if resource.resourses[all_products[6]] >= 50:
                    resource.resourses[all_products[6]] -= 50
                    wr(balance, stats, 65)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place4c.png':
                if resource.resourses[all_products[0]] >= 5:
                    resource.resourses[all_products[0]] -= 5
                    wr(balance, stats, 7)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place1o.png':
                if resource.resourses[all_products[2]] >= 23:
                    resource.resourses[all_products[2]] -= 23
                    wr(balance, stats, 68)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place1op.png':
                if resource.resourses[all_products[3]] >= 24 and resource.resourses[all_products[2]] >= 13:
                    resource.resourses[all_products[3]] -= 24
                    resource.resourses[all_products[2]] -= 13
                    wr(balance, stats, 90)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place1p.png':
                if resource.resourses[all_products[3]] >= 7:
                    resource.resourses[all_products[3]] -= 7
                    wr(balance, stats, 15)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)

            if offers == 'place1s.png':
                if resource.resourses[all_products[4]] >= 25:
                    resource.resourses[all_products[4]] -= 25
                    wr(balance, stats, 54)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)

            if offers == 'place1t.png':
                if resource.resourses[all_products[5]] >= 15:
                    resource.resourses[all_products[5]] -= 15
                    wr(balance, stats, 45)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)

            if offers == 'place2cp.png':
                if resource.resourses[all_products[0]] >= 20 and resource.resourses[all_products[3]] >= 15:
                    resource.resourses[all_products[0]] -= 20
                    resource.resourses[all_products[3]] -= 15
                    wr(balance, stats, 100)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place2o.png':
                if resource.resourses[all_products[2]] >= 61:
                    resource.resourses[all_products[2]] -= 61
                    wr(balance, stats, 160)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place2p.png':
                if resource.resourses[all_products[3]] >= 10:
                    resource.resourses[all_products[3]] -= 10
                    wr(balance, stats, 26)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
            if offers == 'place2pw.png':
                if resource.resourses[all_products[6]] >= 40 and resource.resourses[all_products[3]] >= 10:
                    resource.resourses[all_products[6]] -= 40
                    resource.resourses[all_products[3]] -= 10
                    wr(balance, stats, 100)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)

            if offers == 'place2s.png':
                if resource.resourses[all_products[4]] >= 14:
                    resource.resourses[all_products[4]] -= 14
                    wr(balance, stats, 27)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)

            if offers == 'place2t.png':
                if resource.resourses[all_products[5]] >= 3:
                    resource.resourses[all_products[5]] -= 3
                    wr(balance, stats, 10)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)

            if offers == 'place3s.png':
                if resource.resourses[all_products[4]] >= 34:
                    resource.resourses[all_products[4]]
                    wr(balance, stats, 70)
                    offers = random.choice(ofer)
                    dis.blit(load_image('place_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)
                else:
                    dis.blit(load_image('place_not_done.png'), kords)
                    pygame.display.update()
                    pygame.time.wait(2000)

            if offers == 'place3t.png':
                if resource.resourses[all_products[5]] >= 16:
                    resource.resourses[all_products[5]] -= 16
                    wr(balance, stats, 34)
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
            is_buy1 = False
            is_buy2 = False
            is_buy3 = False
        f = open("stats2.txt", 'w')
        f.write(str(steps))
        f.close()

        # отловка нажатий на поле
        if pygame.mouse.get_pressed()[0] and gameplay and main_plant:
            # print(main_plant)
            # print(pygame.mouse.get_pos())
            pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            # print(pos)
            pl = field.get_click(pos, dis, plants, main_plant)
            print(pl)
            if pl and pl[0] and pl[1]:
                plants[pl[1]] = pl[0]
                statics[pl[0].name] += 1

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

        # отловка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for i in resource.resourses:
                    print(f'{i}: {resource.resourses[i]}')
                print(statics)
                safe_resourses(resource.resourses)

                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and gameplay and main_plant:
                pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                pl = field.get_click(pos, dis, plants, main_plant)
                if pl and pl[0] and pl[1]:
                    plants[pl[1]] = pl[0]
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e and is_inventory and stas:
                gameplay = True
                is_inventory = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and not is_inventory and gameplay and stas:
                gameplay = False
                is_inventory = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and is_settings and not is_inventory and stas:
                is_settings = False
                gameplay = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not is_settings and stas:
                is_settings = True
                gameplay = False
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_t and is_market and not is_inventory and stas:
                gameplay = True
                is_market = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_t and not is_market and stas:
                gameplay = False
                is_market = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB and is_info and not is_inventory and stas:
                gameplay = True
                is_info = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB and not is_info and stas:
                gameplay = False
                is_info = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and is_market and stas:
                if offer1.f(pygame.mouse.get_pos()):
                    is_buy1 = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and is_market and stas:
                if offer2.f(pygame.mouse.get_pos()):
                    is_buy2 = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and is_market and stas:
                if offer3.f(pygame.mouse.get_pos()):
                    is_buy3 = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not gameplay and not stas:
                gameplay = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB and is_info:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and stas:
                gameplay = True
                is_inventory = False
                is_chiken_house = False
                is_real_inventory = False
                is_cow_house = False
                chiken_house = Animal_House(4, 2, 'chiken', 'chiken2.png', 'chiken.png')
                chiken_house.set_view(150, 120, 400, 400)
                cow_house = Animal_House(4, 2, 'cow', 'cow2.png', 'cow.png')
                cow_house.set_view(150, 120, 400, 400)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b and is_real_inventory:
                gameplay = True
                is_real_inventory = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b and not is_real_inventory and gameplay:
                gameplay = False
                is_real_inventory = True

        pygame.display.flip()
        clock.tick(FPS)
    for i in resource.resourses:
        print(f'{i}: {resource.resourses[i]}')
    print(statics)
    safe_resourses(resource.resourses)
    pygame.quit()


if __name__ == '__main__':
    main()
