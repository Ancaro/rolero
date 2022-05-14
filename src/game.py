### Game Module ###

# Main
import pygame

# Models
from src.modules.background.models.background import Background
from src.modules.terrain.models.terrain import Terrain



class Game:

    def __init__(
        self,
        config: dict,
    ):
        self._config = config
        self._screen = None
        self._clk = None
        self._bg = None
        self._terrain = None
        self.set_up()

    def set_up(self):
        """Initializes everything the game needs to work, like the screen and CLK, 
        just to mention a few examples."""
        pygame.init()
        self.setup_screen()
        self.set_title()
        self.setup_clk()
        self.setup_bg()
        self.setup_terrain()

    def set_title(self):
        """This is the title of the window the Game is displayed on."""
        pygame.display.set_caption(self._config.get('TITLE'))

    def setup_screen(self):
        """Creates the screen of the Game."""
        self._screen = pygame.display.set_mode(self._config.get('RESOLUTION'))

    def setup_clk(self):
        """Setup the CLK for the Game."""
        self._clk = pygame.time.Clock()

    def setup_bg(self):
        """Setup the background for the Game."""
        self._bg = Background(self._config.get('DEFAULT_BG'))

    def setup_terrain(self):
        """Setup the terrain for the Game."""
        self._terrain = Terrain(self._config.get('DEFAULT_TERRAIN'))

    def exit_game(self):
        """Closes the Game."""
        pygame.quit()
        exit()
        
    def run(self):
        """Runs the Game and keeps in a infinite loop, waiting for events and 
        running the game logic."""
        # player = pygame.image.load('Graphics\Main Characters\Virtual Guy\Jump (32x32).png').convert_alpha()
        # player_rect = player.get_rect(topleft = (100, 100))
        while True:
            self.check_events() 
            self.render_screen()           
            self._clk.tick(self._config.get('FRAMERATE'))

    def check_events(self):
        """Checks for User input or other events that could affect
        the state of the Game"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game()
            
            # if event.type == pygame.MOUSEMOTION:
            #     print(event.pos)
            #     mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(player_rect.collidepoint(event.pos))
                pass
    
    def render_screen(self):
        """Renders the screen with the current screen config"""
        # screen.blit(ground_surface, (position_bichito[p], 200))
        # screen.blit(text_surface, (400, 10))
        self._bg.fill_background(self._screen)
        self._terrain.fill_terrain(self._screen)

        # self._terrain.get_rect().x += 1
        # if self._terrain.get_rect().right > 800: self._terrain.get_rect().left = 0

        # self._screen.blit(player, player_rect)

        # if not player_rect.colliderect(self._terrain.get_rect()):
        #     player_rect.y += 1
        #     if player_rect.y >= 400:
        #         player_rect.y = 0


        pygame.display.update()
