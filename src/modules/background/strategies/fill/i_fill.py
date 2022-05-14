### Fill Strategy Interface ###

# Main
import abc



class IFillStrategy(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def fill_background(self, screen, surface):
        pass
