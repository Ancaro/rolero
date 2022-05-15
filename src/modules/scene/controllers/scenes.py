### Scenes Controller ###

# Main
import pygame

# Interfaces
from src.modules.scene.models import IScene

# Content
from src.content.scenes import (
    InitialScreenScene, 
    SelectPlayerScreenScene,
)



class ScenesController:

    def __init__(
        self,
        # config: dict,
    ):
        # self.__config = config
        self.__current_scene: IScene = None

    # def set_up(self):
    #     """Initializes the Scenes Controller."""
    #     self.setup_current_scene(InitialScreenScene())

    def setup_current_scene(self, scene: IScene):
        """Setup the current scene."""
        self.__current_scene = scene

    def render(self, screen):
        """Renders current scene into passed screen."""
        self.__current_scene.render(screen)
