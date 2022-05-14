### Game Module ###

# Main
import pygame

# Models
from src.modules.background.models.background import Background



class Game:

    def __init__(
        self,
        config: dict,
    ):
        self._config = config
        self._screen = None
        self._clk = None
        self.set_up()

    def set_up(self):
        """Initializes everything the game needs to work, like the screen and CLK, 
        just to mention a few examples."""
        pygame.init()
        self.setup_screen()
        self.set_title()
        self.setup_clk()
        self.setup_bg()
        
    def run(self):
        """Runs the Game and keeps in a infinite loop, waiting for events and 
        running the game logic."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()

            # screen.blit(ground_surface, (position_bichito[p], 200))
            # screen.blit(text_surface, (400, 10))

            pygame.display.update()

            # p += 3
            # if p >= max_p:
            #     p = 0

            self._clk.tick(self._config.get('FRAMERATE'))
    
    def exit_game(self):
        """Closes the Game."""
        pygame.quit()
        exit()

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
        self._bg.fill_background(self._screen)
