import pygame


class Gate_Input(pygame.sprite.Sprite):
    def __init__(self, img_url="true.png", x=0, y=0, value=True):
        super().__init__()
        self.img_url = img_url
        self.image = pygame.image.load(self.img_url)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.value = value

        output_connector_width = 10
        output_connector_height = 10
        self.output_connector = pygame.Rect(self.rect.right, self.rect.centery - output_connector_height / 2, output_connector_width, output_connector_height)
    
    def draw(self, win, scroll_values):
        # editing self.rect
        # TODO: move this to an update function
        self.rect.x -= scroll_values[0]
        self.rect.y -= scroll_values[1]
        win.blit(self.image, (self.rect.x, self.rect.y))
        self.output_connector.left = self.rect.right
        self.output_connector.midleft = self.rect.midright
        pygame.draw.rect(win, "Green", self.output_connector)
        