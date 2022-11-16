def deletetab(event):
    if event.type == QUIT:  # window fin
        pygame.quit()       # Python fin
        sys.exit()
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()