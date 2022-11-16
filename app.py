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

def button( btn_x , btn_y , btn_color_r , btn_color_g , btn_color_b , btn_width , btn_height , btn_text , font_size , screen ,rad):
    
    btn = pygame.draw.rect(screen,(btn_color_r,btn_color_g,btn_color_b),Rect(btn_x-btn_width/2,btn_y-btn_height/2,btn_width,btn_height),0,rad)
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

def description(screen , texts):
    pygame.draw.rect(screen,(255,255,255),Rect(25,500,750,250),2,15)

def game(screen):
    for event in pygame.event.get():
        deletetab(event)
    description(screen , "Hello!")


def main():
    # Var
    screentype = 0

    pygame.init()                                   # Reset Pygame
    screen = pygame.display.set_mode((800, 800))    # make window 800*800
    icon = pygame.image.load("./src/assets/icon.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("PLANETIE")      # text in title bar
    font = pygame.font.Font("./src/assets/JosefinSans-Bold.ttf", 80)

    clock = pygame.time.Clock()

    while (1):
        clock.tick(60)

        screen.fill((0, 0, 0))        # bg-black

        if screentype == 0:
            logo = font.render("PLANETIE", True, (255, 255, 255))   # 描画する文字列の設定
            logo.set_alpha(256)
            text_rect = logo.get_rect(center=(800//2, 400//2))
            screen.blit(logo, text_rect)  # position logo
            if button( 400 , 500  , 255 , 0 , 0 , 140 , 100 , "Start" , 30 , screen , 20) :
                screentype = 1
        
        if screentype == 1:
            game(screen)


        # don't touch↓
        pygame.display.update()     # update display


if __name__ == "__main__":
    main()
