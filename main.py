import pygame
import random
from cps_functions import in_rect, simple_cps

pygame.init()

def main_menu():

    # Screen 

    HEIGH, WIDTH = 600, 800
    screen = pygame.display.set_mode((WIDTH, HEIGH))
    pygame.display.set_caption("Mouse Trainer - Main Menu")


    # objects
    r_width, r_height = 100, 60
    x, y = WIDTH // 2 - 60 // 2, HEIGH // 2

    

    # text show
    font = pygame.font.SysFont(None, 36)


    #var's that change while loops
    running = True
    clock = pygame.time.Clock()

    while running:
        m_x, m_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # check the click
            if in_rect(m_x, m_y, x, r_width, y, r_height) and (event.type == pygame.MOUSEBUTTONDOWN):
                if event.button == 1:
                    simple_cps()
                    running = False


        # draw objects
        pygame.draw.rect(screen, "red", (x, y, r_width, r_height))


        # show text
        start_text = font.render("Start!", True, "white")
        screen.blit(start_text, (x + 20, y + 20))

        title_text = font.render("Welcome! to Mouse Trainer!!", True, "white")
        screen.blit(title_text, (200, 100))

        # ipdate screen and frames
        clock.tick(60)
        pygame.display.flip()



if __name__ == "__main__":
    main_menu()