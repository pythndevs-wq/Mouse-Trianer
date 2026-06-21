import pygame
import time

for_sec = 1
pygame.init()


def simple_cps():
     #screen setup
    HEIGHT, WIDTH = 600, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mouse Trainer")


    #clicks
    CPS = 0
    clicks = 0

    # box
    circle_width, circle_height = 100, 100
    circle_x, circle_y = WIDTH // 2 - circle_width // 2, HEIGHT // 2 - circle_height // 2


      # state
    waiting = True         # True before the test starts ("Press Enter to Start")
    running_test = False   # True while the 5-second timer is counting down
    start_ticks = 0
    elapsed = 0

    #show text
    font = pygame.font.SysFont(None, 36)
    start_text = font.render("Press Enter to Start", True, (0, 0, 0))
    restart_text = font.render("Press Enter to Restart", True, (0, 0, 0))


    running = True
    clock = pygame.time.Clock()

    while running:
        x , y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # (re)start the test
                clicks = 0
                CPS = 0
                elapsed = 0
                start_ticks = pygame.time.get_ticks()
                waiting = False
                running_test = True
            
            if running_test:
                if (circle_x <= x <= circle_x + circle_width) and (circle_y <= y <= circle_y + circle_height):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        clicks += 1

        if running_test:
            elapsed = (pygame.time.get_ticks() - start_ticks) / 1000
            if elapsed >= for_sec:
                elapsed = for_sec
                running_test = False
                CPS = clicks / for_sec
            else:
                CPS = clicks / elapsed if elapsed > 0 else 0  # avoid division by zero
                

    
        
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (circle_x + circle_width // 2, circle_y + circle_height // 2), 50)

        # show texts
        if waiting:
            screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - start_text.get_height() // 2))
        elif not running_test:
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 - restart_text.get_height() // 2))

        screen.blit(font.render(f"CPS: {CPS:.2f} ==> {clicks}", True, (0, 0, 0)), (10, 10))
        screen.blit(font.render(f"Time: {elapsed:.2f} / {for_sec} sec", True, (0, 0, 0)), (10, 40))

        clock.tick(60)
        pygame.display.flip()










if __name__ == "__main__":
    simple_cps()
