import pygame


class Static_image(pygame.sprite.Sprite):
    def __init__(self, img_url, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(img_url)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))


# TODO: make a Buffer (True -> True)
# TODO: make an Inverted Buffer (True -> False)
# TODO: make an AND (A, B -> AB)
# TODO: make a NAND (A, B -> NOT AB)
# TODO: make an OR (A, B -> A + B)
# TODO: make a NOR (A, B -> NOT A + B)
# TODO: make a XOR (A, B, -> A XOR B)
# TODO: make a XNOR (A, B -> NOT A XOR B)
class Gate(pygame.sprite.Sprite):
    def __init__(self, img_url, x, y):
        super().__init__()
        self.image = pygame.image.load(img_url)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Buffer_Gate(Gate):
    def __init__(self, gate_input, img_url, x, y):
        super().__init__(img_url, x, y)
        self.gate_input = gate_input

    def get_output(self):
        return self.gate_input