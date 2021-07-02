import pygame


# TODO: make a XOR (A, B, -> A XOR B)
# TODO: make a XNOR (A, B -> NOT A XOR B)
class Gate(pygame.sprite.Sprite):
    def __init__(self, img_url="heart.png", x=0, y=0, gate_input1=0, gate_input2=0):
        super().__init__()
        self.img_url = img_url 
        self.image = pygame.image.load(self.img_url)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 

        self.gate_input1 = gate_input1
        self.gate_input2 = gate_input2

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

    def set_input(self, new_gate_input, gate_input_to_set):
        # gate input 1 or 2
        if gate_input_to_set == 1:
            self.gate_input1 = new_gate_input
        if gate_input_to_set == 2:
            self.gate_input2 = new_gate_input

    def flip_input(self, gate_input):
        return not gate_input


class Buffer_Gate(Gate):
    def __init__(self, img_url, x, y, gate_input1):
        super().__init__(img_url, x, y, gate_input1)
        # self.gate_input1 = gate_input1

    def get_output(self):
        return self.gate_input1


class Inverted_Buffer(Gate):
    def __init__(self, img_url, x, y, gate_input1):
        super().__init__(img_url, x, y, gate_input1)
        # self.gate_input1 = gate_input1

    def get_output(self):
        return self.flip_input(self.gate_input1)


class AND_Gate(Gate):
    def __init__(self, img_url, x, y, gate_input1, gate_input2):
        super().__init__(img_url, x, y, gate_input1, gate_input2)
        # self.gate_input1 = gate_input1
        # self.gate_input2 = gate_input2
    
    def get_output(self):
        if not self.gate_input1:
            return False
        if not self.gate_input2:
            return False

        return True
        # alternatively
        # return self.gate_input1 and self.gate_input2


class NAND_Gate(Gate):
    def __init__(self, img_url, x, y, gate_input1, gate_input2):
        super().__init__(img_url, x, y, gate_input1, gate_input2)
        # self.gate_input1 = gate_input1
        # self.gate_input2 = gate_input2

    def get_output(self):
        # temp_AND_Gate = AND_Gate(self.gate_input1, self.gate_input2, self.img_url, self.rect.x, self.rect.y)
        temp_AND_Gate = AND_Gate(self.img_url, self.rect.x, self.rect.y, self.gate_input1, self.gate_input2)
        AND_output = temp_AND_Gate.get_output()
        # temp_Inv_Buff = Inverted_Buffer(AND_output, self.img_url, self.rect.x, self.rect.y)
        temp_Inv_Buff = Inverted_Buffer(self.img_url, self.rect.x, self.rect.y, AND_output)
        temp_Inv_Buff_output = temp_Inv_Buff.get_output()

        return temp_Inv_Buff_output
        # alternatively
        # return not (self.gate_input1 and self.gate_input2)


class OR_Gate(Gate):
    def __init__(self, img_url, x, y, gate_input1, gate_input2):
        super().__init__(img_url, x, y, gate_input1, gate_input2)
        # self.gate_input1 = gate_input1
        # self.gate_input2 = gate_input2

    def get_output(self):
        if self.gate_input1 == False and self.gate_input2 == False:
            return False

        return True
        # alternatively
        # return self.gate_input1 or self.gate_input2


class NOR_Gate(Gate):
    def __init__(self, img_url, x, y, gate_input1, gate_input2):
        super().__init__(img_url, x, y, gate_input1, gate_input2)
        # self.gate_input1 = gate_input1
        # self.gate_input2 = gate_input2
    
    def get_output(self):
        # temp_OR_Gate = OR_Gate(self.gate_input1, self.gate_input2, self.img_url, self.rect.x, self.rect.y)
        temp_OR_Gate = OR_Gate(self.img_url, self.rect.x, self.rect.y, self.gate_input1, self.gate_input2)
        temp_OR_Gate_output = temp_OR_Gate.get_output()
        # temp_Inv_Buff = Inverted_Buffer(self.gate_input1, self.img_url, self.rect.x, self.rect.y)
        temp_Inv_Buff = Inverted_Buffer(self.img_url, self.rect.x, self.rect.y, temp_OR_Gate_output)
        temp_Inv_Buff_output = temp_Inv_Buff.get_output()

        return temp_Inv_Buff_output
        # alternatively
        # return not (self.gate_input 1 or self.gate_input2)