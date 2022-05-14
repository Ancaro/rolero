### Interface Scene model ###

# Main
import abc



class IScene(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def render(self, screen, config):
        pass

    @abc.abstractproperty
    def screen_id(self) -> str:
        return "Rolero!!!"
