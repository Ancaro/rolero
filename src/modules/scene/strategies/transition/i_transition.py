### Transition Strategy Interface ###

# Main
import abc
from typing import Tuple

# Interfaces
from src.modules.scene.models import IScene, TransitionStates



class ITransitionStrategy(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def transition(self, cs: IScene, ns: IScene, ts: TransitionStates, screen) -> Tuple[IScene, IScene, TransitionStates]:
        """This method has to return the next scene. Before that, it can
        do whatever it wants, like displaying a message in the screen."""
        pass
