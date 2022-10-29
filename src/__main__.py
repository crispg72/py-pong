import pygame
from random import randint

def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode([500, 500])
    
    running = True
    playerx = 250
    playery = 250
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            playery -= 1

        if keys[pygame.K_DOWN]:
            playery += 1

        screen.fill((255, 255, 255))
    
        pygame.draw.circle(screen, (0, 0, 0), (playerx, playery), 5)
    
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":    
    main()