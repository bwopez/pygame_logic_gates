import pygame


# TODO: make a "snap" connecting box
    # so when something comes in contact with it then it will "snap" 
    # and be connected to it
    # when something is connected to it then that will be
    # the input for that gate, whether it be input1 or input2
# TODO: create art for each gate
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

        # TODO: change this to only one input_connector
        # TODO: make a two pronged input gate for all the other gates
        input_connector_width = 10
        input_connector_height = 10
        self.list_of_inputs = []
        self.input_connector1 = pygame.Rect(self.rect.left - input_connector_width, self.rect.top - input_connector_height, input_connector_width, input_connector_height)
        self.input_connector2 = pygame.Rect(self.rect.left - input_connector_width, self.rect.bottom + input_connector_height, input_connector_width, input_connector_height)
        self.list_of_inputs.append(self.input_connector1)
        self.list_of_inputs.append(self.input_connector2)

    def draw(self, win, scroll_values):
        self.rect.x -= scroll_values[0]
        self.rect.y -= scroll_values[1]

        win.blit(self.image, (self.rect.x, self.rect.y))
        self.input_connector1.right = self.rect.left
        self.input_connector1.bottom = self.rect.top
        pygame.draw.rect(win, "Green", self.input_connector1)

        self.input_connector2.right = self.rect.left
        self.input_connector2.top = self.rect.bottom
        pygame.draw.rect(win, "Green", self.input_connector2)

    def set_input(self, new_gate_input, gate_input_to_set):
        # gate input 1 or 2
        if gate_input_to_set == 1:
            self.gate_input1 = new_gate_input
            # self.gate_input1.value = new_gate_input 
        if gate_input_to_set == 2:
            self.gate_input2 = new_gate_input
            # self.gate_input2.value = new_gate_input

    def flip_input(self, gate_input):
        return not gate_input
        # return not gate_input.value

    def flip_input1(self):
        self.set_input(self.flip_input(self.gate_input1), 1)
        # self.set_input(self.flip_input(self.gate_input1.value), 1)

    def flip_input2(self):
        self.set_input(self.flip_input(self.gate_input2), 2)
        # self.set_input(self.flip_input(self.gate_input2.value), 2)


class Buffer_Gate(Gate):
    def __init__(self, img_url, x, y, gate_input1):
        super().__init__(img_url, x, y, gate_input1)

    def get_output(self):
        return self.gate_input1


class Inverted_Buffer_Gate(Gate):
    def __init__(self, img_url, x, y, gate_input1=0):
        super().__init__(img_url, x, y, gate_input1)

    def get_output(self):
        # TODO: fix this for all gates
        if self.gate_input1:
            return self.flip_input(self.gate_input1.value)
        return self.flip_input(self.gate_input1)


class AND_Gate(Gate):
    def __init__(self, img_url, x, y, gate_input1, gate_input2):
        super().__init__(img_url, x, y, gate_input1, gate_input2)
    
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

    def get_output(self):
        temp_AND_Gate = AND_Gate(self.img_url, self.rect.x, self.rect.y, self.gate_input1, self.gate_input2)
        AND_output = temp_AND_Gate.get_output()
        temp_Inv_Buff = Inverted_Buffer_Gate(self.img_url, self.rect.x, self.rect.y, AND_output)
        temp_Inv_Buff_output = temp_Inv_Buff.get_output()

        return temp_Inv_Buff_output
        # alternatively
        # return not (self.gate_input1 and self.gate_input2)


class OR_Gate(Gate):
    def __init__(self, img_url, x, y, gate_input1, gate_input2):
        super().__init__(img_url, x, y, gate_input1, gate_input2)

    def get_output(self):
        if self.gate_input1 == False and self.gate_input2 == False:
            return False

        return True
        # alternatively
        # return self.gate_input1 or self.gate_input2


class NOR_Gate(Gate):
    def __init__(self, img_url, x, y, gate_input1, gate_input2):
        super().__init__(img_url, x, y, gate_input1, gate_input2)
    
    def get_output(self):
        temp_OR_Gate = OR_Gate(self.img_url, self.rect.x, self.rect.y, self.gate_input1, self.gate_input2)
        temp_OR_Gate_output = temp_OR_Gate.get_output()
        temp_Inv_Buff = Inverted_Buffer_Gate(self.img_url, self.rect.x, self.rect.y, temp_OR_Gate_output)
        temp_Inv_Buff_output = temp_Inv_Buff.get_output()

        return temp_Inv_Buff_output
        # alternatively
        # return not (self.gate_input 1 or self.gate_input2)


# XOR Gate
# if both are the same = False
class XOR_Gate(Gate):
    def __init__(self, img_url, x, y, gate_input1, gate_input2):
        super().__init__(img_url, x, y, gate_input1, gate_input2)

    def get_output(self):
        if self.gate_input1 == self.gate_input2:
            return False
        return True


class XNOR_Gate(Gate):
    def __init__(self, img_url, x, y, gate_input1=0, gate_input2=0):
        super().__init__(img_url, x, y, gate_input1, gate_input2)

    def get_output(self):
        temp_XOR_Gate = XOR_Gate(self.img_url, self.rect.x, self.rect.y, self.gate_input1, self.gate_input2)
        temp_XOR_Gate_output = temp_XOR_Gate.get_output()
        temp_Inv_Buff = Inverted_Buffer_Gate(self.img_url, self.rect.x, self.rect.y, temp_XOR_Gate_output)
        temp_Inv_Buff_output = temp_Inv_Buff.get_output()

        return temp_Inv_Buff_output