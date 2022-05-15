### Game Module ###

# Main
import pygame

# Interfaces
from src.modules.scene.models import IScene

# Content
from src.content.scenes import (
    InitialScreenScene, 
    SelectPlayerScreenScene,
)



class Game:

    def __init__(
        self,
        config: dict,
    ):
        self.__config = config
        self.__screen = None
        self.__clk = None
        self.__current_scene: IScene = None
        self.set_up()

        self.test = False

    def set_up(self):
        """Initializes everything the game needs to work, like the screen and CLK, 
        just to mention a few examples."""
        pygame.init()
        self.setup_screen()
        self.set_title()
        self.setup_clk()
        self.setup_current_scene(InitialScreenScene())

    def set_title(self):
        """This is the title of the window the Game is displayed on."""
        pygame.display.set_caption(self.__config.get('TITLE'))

    def setup_screen(self):
        """Creates the screen of the Game."""
        self.__screen = pygame.display.set_mode(self.__config.get('RESOLUTION'))

    def setup_clk(self):
        """Setup the CLK for the Game."""
        self.__clk = pygame.time.Clock()

    def setup_current_scene(self, scene: IScene):
        """Setup the current scene the Game is displaying."""
        self.__current_scene = scene

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
            self.action()
            self.render_screen()
            self.__clk.tick(self.__config.get('FRAMERATE'))

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
                self.test = not self.test
    
    def action(self):
        if self.test:
            self.setup_current_scene(InitialScreenScene())
        else:
            self.setup_current_scene(SelectPlayerScreenScene())

    def render_screen(self):
        """Renders the screen with the current screen config"""
        self.__current_scene.render(self.__screen)
        # screen.blit(ground_surface, (position_bichito[p], 200))
        # screen.blit(text_surface, (400, 10))

        # self.__terrain.get_rect().x += 1
        # if self.__terrain.get_rect().right > 800: self.__terrain.get_rect().left = 0

        # self.__screen.blit(player, player_rect)

        # if not player_rect.colliderect(self.__terrain.get_rect()):
        #     player_rect.y += 1
        #     if player_rect.y >= 400:
        #         player_rect.y = 0


        pygame.display.update()
