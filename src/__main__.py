import pygame
from random import randint

def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode([500, 500])
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #screen.fill((255, 255, 255))
    
        pygame.draw.circle(screen, (randint(0,255), randint(0,255), randint(0,255)), (randint(0,500), randint(0,500)), 5)
    
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":    
    main()