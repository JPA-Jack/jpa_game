import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
pygame.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    x =0
    while x == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill ("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
