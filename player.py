import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

        self.move_speed = 5

    def draw(self, win, scroll_values):
        # TODO: move this to an update function
        self.rect.x -= scroll_values[0]
        self.rect.y -= scroll_values[1]

        win.blit(self.image, (self.rect.x, self.rect.y))
        # win.blit(self.image, (self.rect.x - scroll_x, self.rect.y - scroll_y))
    
    def move(self, win, direction):
        if direction == "left":
            self.rect.x -= self.move_speed
            # if self.rect.left <= 0:
            #     self.rect.left = 0
        if direction == "right":
            self.rect.x += self.move_speed
            # if self.rect.right >= win.get_width():
            #     self.rect.right = win.get_width()
        if direction == "up":
            self.rect.y -= self.move_speed
            # if self.rect.top <= 0:
            #     self.rect.top = 0
        if direction == "down":
            self.rect.y += self.move_speed
            # if self.rect.bottom >= win.get_height():
            #     self.rect.bottom = win.get_height()