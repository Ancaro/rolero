# Background Model

# Main
import pygame



class Background:

    def __init__(
        self, 
        bg_image: str,
    ):
        self._bg_image = bg_image
        self._surface = pygame.image.load(self._bg_image).convert()
    
    def get_surface(self):
        """Return the surface object of the background."""
        return self._surface

    def fill_background(self, screen):
        """Fills the background of the passed screen with the configured background."""
        screen_w, screen_h = screen.get_size()
        bg_w, bg_h = self._surface.get_size()
        for x in range(0, screen_w, bg_w):
            for y in range(0, screen_h, bg_h):
                screen.blit(self._surface, (x, y))
