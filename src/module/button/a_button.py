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