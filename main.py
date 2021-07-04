import pygame, random
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
    inverted_buffer_gate = Inverted_Buffer_Gate("heart.png", 200, 200)
    gates.append(inverted_buffer_gate)

    new_input = Gate_Input("true.png", 0, 0, True)
    connectables.append(new_input)
    new_input2 = Gate_Input("false.png", 0, 400, False)
    connectables.append(new_input2)

    player = Player(50, 50)
    player_connected = False

    # dafluffypotato code
    scroll = [0, 0]

    running = True
    while running:
        current_gate = gates[current_element]

        # collidelist is not letting me get the 0th element of the list
        # SOLVED IT
        # DO NOT USE 
            # if player.rect.collidelist(connectables):
        # USE INSTEAD
            # if player.rect.collidelist(connectables) != -1:
        # if player.rect.collidelist(connectables) != -1:
        #     print(player.rect.collidelist(connectables), connectables[player.rect.collidelist(connectables)])

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
                # TODO: recreate the connecting to gate function for input
                if event.key == K_SPACE:
                    if player_connected:
                        player_connected = False
                        connectables[current_connected_input].connected_to = 0
                    else:
                        current_connected_input = player.rect.collidelist(connectables)
                        if current_connected_input != -1:
                            player_connected = True
                            connectables[current_connected_input].connected_to = player

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

        # for gate in gates:
        #     if gate.gate_input1:
        #         gate.gate_input1.rect.midright = gate.rect.midleft

        # dafluffypotato code
        new_input.draw(win, scroll)
        new_input2.draw(win, scroll)
        inverted_buffer_gate.draw(win, scroll)
        player.draw(win, scroll)
        
        clock.tick(60)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main_game()