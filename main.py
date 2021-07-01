import pygame
from pygame.locals import *

from gates import Static_image, Buffer_Gate


def main_game():
    # window creation =========================
    pygame.init()
    clock = pygame.time.Clock()

    temp_image = Static_image("../snake/images/heart.png", 69, 69)
    temp_gate = Buffer_Gate(True, "../snake/images/snake_32.png", 200, 200)

    win = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("circuit gates")

    running = True
    while running:

        # Input validation ====================
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        if keys[K_ESCAPE]:
            running = False

        # Update window =======================
        win.fill("White")
        temp_image.draw(win)
        temp_gate.draw(win)
        
        clock.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main_game()