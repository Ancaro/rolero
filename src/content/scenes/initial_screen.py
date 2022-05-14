### Scene: Initial Screen ###

# Interfaces
from src.modules.scene.models.i_scene import IScene

# Models
from src.modules.background.models.background import Background
from src.modules.terrain.models.terrain import Terrain


class InitialScreenScene(IScene):

    def __init__(self, config):
        IScene.__init__(self)
        self.__config = config
        self.__bg = Background(self.__config.get('DEFAULT_BG'))

    @property
    def screen_id(self):
        return "Rolero HP!!!"

    def render(self, screen):
        self.__fill_background(screen)

    def __fill_background(self, screen):
        self.__bg.fill_background(screen)

    # def setup_bg(self):
    #     """Setup the background for this Scene."""
    #     self.__bg = 

    # def setup_terrain(self):
    #     """Setup the terrain for the Game."""
    #     self.__terrain = Terrain(self.__config.get('DEFAULT_TERRAIN'))
