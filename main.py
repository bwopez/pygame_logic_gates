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

    # we know all the gates work
    gates = []
    current_element = 0
    # xnor_gate = XNOR_Gate("heart.png", 200, 200, True, True)
    # xnor_gate = XNOR_Gate("heart.png", 200, 200)
    # gates.append(xnor_gate)
    inverted_buffer_gate = Inverted_Buffer_Gate("heart.png", 200, 200)
    gates.append(inverted_buffer_gate)

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

        # dafluffypotato code
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

                # TODO: it is still a problem that if you try to put True on the gate first
                    # that it'll just throw both True and False on the gate input
                if event.key == K_SPACE:
                    current_connected_input = player.rect.collidelist(connectables)
                    # TODO: I think its not disconnecting because it is checking here if there
                        # if connectables[current_connected_input].connected_to exists
                        # that means if connectables[current_connected_input].connected_to != 0
                        # I think it is set to 0 somewhere that isn't here
                    if current_connected_input != -1:
                        if connectables[current_connected_input].connected_to:
                            connectables[current_connected_input].connected_to.gate_input1 = 0
                            connectables[current_connected_input].connected_to = 0
                        player_connected = True
                    else:
                        if player_connected:
                            current_connected_gate = player.rect.collidelist(gates)
                            if current_connected_gate != -1:
                                # gates[current_connected_gate].gate_input1 = connectables[current_connected_input]
                                # connectables[current_connected_input].connected_to = gates[current_connected_gate]
                                current_connected_gate_input = player.rect.collidelist(gates[current_connected_gate].list_of_inputs)
                                if current_connected_gate_input != -1:
                                    print("current_connected_gate_input", current_connected_gate_input)
                                    gates[current_connected_gate].list_of_inputs[current_connected_gate_input] = connectables[current_connected_input]
                                    connectables[current_connected_input].connected_to = gates[current_connected_gate]
 
                        player_connected = False

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

        # TODO: fix how gate inputs are being connected to the gates
            # when you connect one it's fine but when you click again
            # the next input will automatically snap to the gate itself
        # if player_connected:
        #     connectables[connected_index].rect.midright = player.rect.midleft
        if player_connected:
            connectables[current_connected_input].rect.midright = player.rect.midleft
        # for gate in gates:
        #     if gate.input1_connected and not player_connected:
        #         connectables[connected_index].rect.midright = gates[curr_conn_gate].rect.midleft
        #     if gate.input2_connected and not player_connected:
        #         connectables[connected_index].rect.bottomright = gates[curr_conn_gate].rect.topleft
        for gate in gates:
            if gate.gate_input1:
                gate.gate_input1.rect.midright = gate.rect.midleft

        # dafluffypotato code
        new_input.draw(win, scroll)
        new_input2.draw(win, scroll)
        # xnor_gate.draw(win, scroll)
        inverted_buffer_gate.draw(win, scroll)
        player.draw(win, scroll)
        
        clock.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main_game()