### Scene: Initial Screen ###

# Interfaces
from src.modules.scene.models.i_scene import IScene

# Models
from src.modules.background.models.background import Background
from src.modules.terrain.models.terrain import Terrain

from src.modules.background.strategies import FillWithPatternStrategy



class InitialScreenScene(IScene):
    """Initial Screen Scene"""

    def __init__(
        self,
    ):
        super().__init__()
        self.__bg = None
        self.__setup_bg()

    @property
    def screen_id(self):
        return "Rolero HP!!!"

    def render(self, screen):
        self.__fill_background(screen)

    def __setup_bg(self):
        self.__bg = Background(
            'Graphics/Background/Gray.png',
            FillWithPatternStrategy(),
        )

    def __fill_background(self, screen):
        self.__bg.fill_background(screen)

    # def setup_terrain(self):
    #     """Setup the terrain for the Game."""
    #     self.__terrain = Terrain(self.__config.get('DEFAULT_TERRAIN'))
