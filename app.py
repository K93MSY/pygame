import pygame
from pygame.locals import *
import sys

def deletetab(event):
    if event.type == QUIT:  # window fin
        pygame.quit()       # Python fin
        sys.exit()
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

def button( btn_x , btn_y , btn_color_r , btn_color_g , btn_color_b , btn_width , btn_height , btn_text , font_size , screen):
    
    btn = pygame.draw.rect(screen,(btn_color_r,btn_color_g,btn_color_b),Rect(btn_x-btn_width/2,btn_y-btn_height/2,btn_width,btn_height))
    btn_font = pygame.font.Font("./src/assets/JosefinSans-Bold.ttf", font_size)
    drawtxt = btn_font.render(btn_text, True,(255, 255, 255))
    drawtxt.set_alpha(256)
    btntext_rect = drawtxt.get_rect(center=(btn_x, btn_y))
    screen.blit(drawtxt, btntext_rect)

    for event in pygame.event.get():
        deletetab(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn.collidepoint(event.pos):
                print("red button was pressed")
                return True

def main():
    # Var
    screentype = 0

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
        text_rect = logo.get_rect(center=(800//2, 400//2))
        screen.blit(logo, text_rect)  # position logo

        if button( 400 , 200  , 255 , 0 , 0 , 300 , 200 , "Test" , 30 , screen) :
            screentype = 1
            print("Get true!")

        # don't touch↓
        pygame.display.update()     # update display


if __name__ == "__main__":
    main()
