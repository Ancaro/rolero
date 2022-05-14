### Main ###


# Config
from src.config import CONFIG

# Game
from src.game import Game



### Begin ###

g = Game(CONFIG)
g.run()

# Surfaces
# ground_surface = pygame.image.load('Graphics/Main Characters/Mask Dude/Fall (32x32).png')
# test_font = pygame.font.Font('Fonts/Koulen-Regular.ttf', 50)
# text_surface = test_font.render("Rolero", False, "Red")
  