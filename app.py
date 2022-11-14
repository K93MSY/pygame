import pygame
from pygame.locals import *
import sys


def main():
    # Var

    pygame.init()                                   # Reset Pygame
    screen = pygame.display.set_mode((800, 800))    # make window 800*800
    pygame.display.set_caption("FantasyTrain")      # text in title bar
    font = pygame.font.Font("./src/assets/JosefinSans-Bold.ttf", 80)

    clock = pygame.time.Clock()

    while (1):
        clock.tick(60)

        screen.fill((0, 0, 0))        # bg-black
        logo = font.render("Fantasy Train", True,
                           (255, 255, 255))   # 描画する文字列の設定
        logo.set_alpha(256)
        screen.blit(logo, [140, 120])  # position logo

        # don't touch↓
        pygame.display.update()     # update display
        for event in pygame.event.get():
            if event.type == QUIT:  # window fin
                pygame.quit()       # Python fin
                sys.exit()
            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main()
