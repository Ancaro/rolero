### Scene: Select Player Screen ###

# Interfaces
from src.modules.scene.models import IScene

# Models
from src.modules.background.models import Background
# from src.modules.terrain.models.terrain import Terrain

from src.modules.background.strategies import FillWithPatternStrategy



class SelectPlayerScreenScene(IScene):
    """Select Player Screen Scene"""

    def __init__(
        self,
    ):
        super().__init__()
        self.__bg = None
        self.__setup_bg()

    @property
    def screen_id(self):
        return "select-player"

    def render(self, screen):
        self.__fill_background(screen)

    def __setup_bg(self):
        self.__bg = Background(
            'Graphics/Background/Purple.png',
            FillWithPatternStrategy(),
        )

    def __fill_background(self, screen):
        self.__bg.fill_background(screen)
