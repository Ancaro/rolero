### Scenes Controller ###

# Interfaces
from src.modules.scene.models import IScene, TransitionStates
from src.modules.scene.strategies import (
    ITransitionStrategy,
    FadingTransitionStrategy,
)



class ScenesController:

    def __init__(
        self,
    ):
        self.__current_scene: IScene = None
        self.__next_scene: IScene = None
        self.__transition_state = TransitionStates.OFF
        self.__transition_strategy: ITransitionStrategy = FadingTransitionStrategy()

    # def set_up(self):
    #     """Initializes the Scenes Controller."""
    #     self.setup_current_scene(InitialScreenScene())

    def setup_current_scene(self, scene: IScene):
        """Setup the current scene."""
        if not self.__current_scene:
            self.__current_scene = scene
            self.__next_scene = None
            self.__transition_state = TransitionStates.IN
        else:
            self.__next_scene = scene
            self.__transition_state = TransitionStates.OUT

    def render(self, screen):
        """Renders current scene into passed screen."""
        if self.__transition_state != TransitionStates.OFF:
            self.__current_scene, self.__next_scene, self.__transition_state = self.__transition_strategy.transition(
                self.__current_scene,
                self.__next_scene,
                self.__transition_state,
                screen,
            )
        else:
            self.__current_scene.render(screen)
