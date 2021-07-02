import pygame
from pygame.locals import *

from gates import (
    Buffer_Gate, Inverted_Buffer_Gate, 
    AND_Gate, NAND_Gate, OR_Gate, NOR_Gate,
    XOR_Gate, XNOR_Gate
)
from gate_inputs import Gate_Input


# TODO: make some graphics for the gates
# TODO: make some graphics for the inputs
# TODO: create small boxes at the ends of the gate's 
    # and the ends of the inputs so that they can "snap" to 
    # each other when they come in contact with each other
def main_game():
    # window creation =========================
    pygame.init()
    clock = pygame.time.Clock()

    gates = []
    current_element = 0
    buffer_gate = Buffer_Gate("heart.png", 0, 0, True)
    gates.append(buffer_gate)
    inverted_buffer_gate = Inverted_Buffer_Gate("heart.png", 0, 0, True)
    gates.append(inverted_buffer_gate)
    and_gate = AND_Gate("heart.png", 0, 0, True, True)
    gates.append(and_gate)
    nand_gate = NAND_Gate("heart.png", 0, 0, True, True)
    gates.append(nand_gate)
    or_gate = OR_Gate("heart.png", 0, 0, True, True)
    gates.append(or_gate)
    nor_gate = NOR_Gate("heart.png", 0, 0, True, True)
    gates.append(nor_gate)
    xor_gate = XOR_Gate("heart.png", 0, 0, True, True)
    gates.append(xor_gate)
    xnor_gate = XNOR_Gate("heart.png", 0, 0, True, True)
    gates.append(xnor_gate)

    new_input = Gate_Input("true.png", 0, 0, True)
    new_input2 = Gate_Input("false.png", 0, 32, False)

    win = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("circuit gates")

    running = True
    while running:
        current_gate = gates[current_element]

        # Input validation ====================
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # Changing inputs =================
            if event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    # temp_NOR_Gate.set_input(temp_NOR_Gate.flip_input(temp_NOR_Gate.gate_input1), 1)
                    # current_gate.set_input(current_gate.flip_input(current_gate.gate_input1), 1)
                    current_gate.flip_input1()
                if event.key == K_RIGHT:
                    # temp_NOR_Gate.set_input(temp_NOR_Gate.flip_input(temp_NOR_Gate.gate_input2), 2)
                    # current_gate.set_input(current_gate.flip_input(current_gate.gate_input2), 2)
                    current_gate.flip_input2()
                if event.key == K_SPACE:
                    current_element += 1
                    if current_element > len(gates) - 1:
                        current_element = 0
                print(current_element, current_gate.gate_input1, current_gate.gate_input2, current_gate.get_output())

        if keys[K_ESCAPE]:
            running = False

        # Update window =======================
        win.fill("White")
        new_input.draw(win)
        new_input2.draw(win)
        
        clock.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main_game()