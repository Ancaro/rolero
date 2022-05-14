### Background Model ###

# Main
import pygame

# Interfaces
from src.modules.background.strategies import IFillStrategy



class Background:

    def __init__(
        self, 
        bg_image: str,
        fill_strategy: IFillStrategy,
    ):
        self.__bg_image = bg_image
        self.__surface = pygame.image.load(self.__bg_image).convert()
        self.fill_strategy = fill_strategy
    
    def get_surface(self):
        """Return the surface object of the background."""
        return self.__surface

    def fill_background(self, screen):
        """Fills the background using the IFillStrategy configured."""
        self.fill_strategy.fill_background(screen, self.__surface)
