### Terrain Model ###

# Main
import pygame



class Terrain:

    def __init__(
        self, 
        terrain_image: str,
    ):
        self.__terrain_image = terrain_image
        self.__surface = pygame.image.load(self.__terrain_image).convert_alpha()
        self.__rect = self.__surface.get_rect(midbottom=(200,400))
    
    def get_surface(self):
        """Return the surface object of the terrain."""
        return self.__surface
    
    def get_rect(self):
        """Return the rect object of the terrain."""
        return self.__rect
    
    def fill_terrain(self, screen):
        """Fills the terrain of the passed screen with the configured terrain."""
        screen.blit(self.__surface, self.__rect)
