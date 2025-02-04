import pygame
from load_image import load_image, Field, Inventory, Animal_House, resource, Hero

pygame.init()


def main():
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

    river = [load_image('river/river1.png', 1), load_image('river/river1.png', 1), load_image('river/river1.png', 1)]
    river_count = 0

    main_plant = wheat.copy()

    all_products = ['carrot', 'corn', 'cucumber', 'pumpkin', 'sunflower', 'tomato', 'wheap', 'egg', 'milk']

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
    chiken_house_fon = load_image('fon_chiken.png')

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

    player_group = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    hero = Hero(player_group, (player_x, player_y))

    gameplay = True
    is_inventory = False
    is_chiken_house = False
    is_real_inventory = False
    is_cow_house = False

    while run:
        # переменные, которые нужно изменять во время игры
        chiken_house_rect = pygame.rect.Rect(125 + fon_x, 760 + fon_y, 500, 500)
        cow_house_rect = pygame.rect.Rect(125 + fon_x, 1500 + fon_y, 650, 600)
        field.set_view(60 + fon_x, 50 + fon_y, 65, 67)
        count += 1
        player_speed = 20

        key = pygame.key.get_pressed()

        # ходьба игрока
        if key[pygame.K_LSHIFT] and gameplay:
            player_speed = 7
        if key[pygame.K_w] and gameplay:
            if dis_y // 2 - 100 > hero.rect.y and fon_y <= 0:
                fon_y += player_speed
            elif hero.rect.y > 0:
                hero.update((0, -player_speed), None)
        if key[pygame.K_s] and gameplay:
            if dis_y // 2 + 100 < hero.rect.y and fon_y >= -(2160 - dis_y):
                fon_y -= player_speed
            elif hero.rect.y < 2060 + fon_y:
                hero.update((0, player_speed), None)
        if key[pygame.K_d] and gameplay:
            if dis_x // 2 + 100 < hero.rect.x and fon_x >= -(3840 - dis_x):
                fon_x -= player_speed
            elif hero.rect.x < 3780 + fon_x:
                hero.update((player_speed, 0), None)
        if key[pygame.K_a] and gameplay:
            if dis_x // 2 - 100 > hero.rect.x and fon_x <= 0:
                fon_x += player_speed
            elif hero.rect.x > 0:
                hero.update((-player_speed, 0), None)

        # отловка нажатий на дoма зверей
        if pygame.mouse.get_pressed()[0] and gameplay:
            if chiken_house_rect.collidepoint(pygame.mouse.get_pos()):
                # print('yes')
                gameplay = False
                is_inventory = False
                is_cow_house = False
                is_chiken_house = True
            if cow_house_rect.collidepoint(pygame.mouse.get_pos()):
                # print('yes')
                gameplay = False
                is_inventory = False
                is_chiken_house = False
                is_cow_house = True

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

        player_group.draw(dis)
        dis.blit(load_image(main_plant[4]), (dis_x - 270, -50))

        # отображение реки
        # if river_count / 20 == 2:
        #     river_count = 0
        # river_count += 1
        # dis.blit(river[river_count // 20], (fon_x, fon_y))

        pygame.draw.rect(dis, pygame.Color("white"), cow_house_rect, 1)

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
            for x in range(inventory.width):
                for y in range(inventory.height):
                    try:
                        dis.blit(load_image(plants_images[x + y * inventory.width]), (
                            x * inventory.cell_size_x + inventory.left, y * inventory.cell_size_y + inventory.top))
                    except IndexError:
                        pass
            # инициализация нажатий в инвенторе
            if pygame.mouse.get_pressed()[0]:
                if inventory.get_click(pygame.mouse.get_pos()):
                    main_plant = inventory.get_click(pygame.mouse.get_pos())

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
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and gameplay and main_plant:
                pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                pl = field.get_click(pos, dis, plants, main_plant)
                if pl and pl[0] and pl[1]:
                    plants[pl[1]] = pl[0]
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e and is_inventory:
                gameplay = True
                is_inventory = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and not is_inventory and gameplay:
                gameplay = False
                is_inventory = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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
    pygame.quit()


if __name__ == '__main__':
    main()