import pygame
from load_image import load_image


pygame.font.init()

def main():
    clock = pygame.time.Clock()
    run = True
    FPS = 60

    pygame.init()
    infoObject = pygame.display.Info()
    dis_x = infoObject.current_w
    dis_y = infoObject.current_h
    dis = pygame.display.set_mode((dis_x, dis_y))
    pygame.display.set_caption("Wandering")

    while run:
        dis.fill('red')

        pygame.display.flip()

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False

        clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    main()