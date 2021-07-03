import pygame
from pygame.locals import *

from gates import (
    Buffer_Gate, Inverted_Buffer_Gate, 
    AND_Gate, NAND_Gate, OR_Gate, NOR_Gate,
    XOR_Gate, XNOR_Gate
)
from gate_inputs import Gate_Input
from player import Player

# TODO: make some graphics for the gates
# TODO: make some graphics for the inputs
# TODO: create small boxes at the ends of the gate's 
    # and the ends of the inputs so that they can "snap" to 
    # each other when they come in contact with each other
# TODO: create a camera so that everything can be 
    # blitted onto that and screen shake can be applied to it
    # easier
def main_game():
    # window creation =========================
    pygame.init()
    clock = pygame.time.Clock()

    win = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("circuit gates")

    # list of things that you can drag with your player
    connectables = []

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
    connectables.append(new_input)
    new_input2 = Gate_Input("false.png", 0, 32, False)
    connectables.append(new_input2)

    player = Player(50, 50)
    player_connected = False

    # dafluffypotato code
    scroll = [1, 0]

    running = True
    while running:
        current_gate = gates[current_element]

        # to keep the player in the middle of the screen
        scroll[0] += player.rect.centerx - scroll[0] - ((win.get_width() / 2) + (player.rect.width / 2))
        scroll[1] += player.rect.centery - scroll[1] - ((win.get_height() / 2) + (player.rect.height / 2))

        # Input validation ====================
        keys = pygame.key.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # Changing inputs =================
            if event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    current_gate.flip_input1()
                if event.key == K_RIGHT:
                    current_gate.flip_input2()
                # if event.key == K_SPACE:
                #     current_element += 1
                #     if current_element > len(gates) - 1:
                #         current_element = 0
                # print(current_element, current_gate.gate_input1, current_gate.gate_input2, current_gate.get_output())
                if event.key == K_SPACE:
                    connected_index = player.rect.collidelist(connectables) 
                    if connected_index != -1:
                        print(connected_index)
                        player_connected = True
                        print(player_connected)
                    else:
                        player_connected = False
                        print(player_connected)

            # if new_input.rect.left <= mouse_x <= new_input.rect.right and new_input.rect.top <= mouse_y <= new_input.rect.bottom:
            #     if event.type == pygame.MOUSEBUTTONDOWN:
            #         new_input.rect.center = mouse_x, mouse_y

        if keys[K_ESCAPE]:
            running = False
        if keys[K_a]:
            player.move(win, "left")
        if keys[K_d]:
            player.move(win, "right")
        if keys[K_w]:
            player.move(win, "up")
        if keys[K_s]:
            player.move(win, "down")

        # Update window =======================
        win.fill("White")

        # new_input.draw(win, scroll[0], scroll[1])
        # new_input2.draw(win, scroll[0], scroll[1])
        # player.draw(win, scroll[0], scroll[1])
        # TODO: if the player is connected to something
            # move the thing but with the player's input
        if player_connected:
            connectables[connected_index].rect.midright = player.rect.midleft
        new_input.draw(win, scroll)
        new_input2.draw(win, scroll)
        player.draw(win, scroll)
        
        clock.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main_game()