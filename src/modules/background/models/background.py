# Background Model

# Main
import pygame



class Background:

    def __init__(
        self, 
        bg_image: str,
    ):
        self._bg_image = bg_image
        self._surface = pygame.image.load(self._bg_image)
    
    def getSurface(self):
        return self._surface

    def fillBackground(self, screen):
        screen_w, screen_h = screen.get_size()
        bg_w, bg_h = self._surface.get_size()
        for x in range(0, screen_w, bg_w):
            for y in range(0, screen_h, bg_h):
                screen.blit(self._surface, (x, y))
