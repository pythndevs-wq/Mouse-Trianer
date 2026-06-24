import pygame
import time
import random

for_sec = 1
pygame.init()


def simple_cps():
     #screen setup
 # screen setup
    HEIGHT, WIDTH = 600, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mouse Trainer")

    # clicks
    CPS = 0
    clicks = 0


    # target
    target_radius = 30
    target_x, target_y = WIDTH // 2 , HEIGHT // 2




    # Show CPS nad press enter to start
    displaying = True
    font = pygame.font.SysFont(None, 36)




    # others behind the game loop
    running = True
    clock = pygame.time.Clock()

    # main loop
    while running:


        (x, y) = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # check if the mouse is within the target circle
            if (target_x - x) ** 2 + (target_y - y) ** 2 <= target_radius ** 2:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # [1 means left button]
                    clicks += 1
                    displaying = False
                    CPS = clicks / (pygame.time.get_ticks() / 1000) # it will calculate by dividing the total clicks by the total time in seconds in result giving us the click per second
                    # move the target to a new random position
                    target_x = random.randint(target_radius, WIDTH - target_radius)
                    target_y = random.randint(target_radius, HEIGHT - target_radius)

    

        # fill the background
        screen.fill((255, 255, 255))
        # draw the target circle
        pygame.draw.circle(screen, (255, 0, 0), (target_x, target_y), target_radius)

        # draw the CPS text nad press enter to start text
        cps_text = font.render(f"CPS: {CPS:.2f}", True, (0, 0, 0))
        screen.blit(cps_text, (10, 10))

        if displaying:
            p_enter_text = font.render(f"Click to start...", True, (0, 0, 0))
            screen.blit(p_enter_text, (target_x - p_enter_text.get_width() // 2, target_y - target_radius - 50))

        clock.tick(60)  # limit to 60 frames per second
        # refrest screen after every loop
        pygame.display.flip()




def in_rect(x, y, x_min, x_max, y_min, y_max):
    if (x_min <= x <= x_max) and (y_min <= y <= y <= y_max):
        return True



def menu_window():
    pass
    



if __name__ == "__main__":
    simple_cps()
