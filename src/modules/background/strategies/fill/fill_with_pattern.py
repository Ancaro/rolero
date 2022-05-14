### Fill Background Strategy ###

# Interface
from .i_fill import IFillStrategy



class FillWithPatternStrategy(IFillStrategy):

    def __init__(self):
        super().__init__()
    
    def fill_background(self, screen, surface):
        """Fills the background of the passed screen repeating the surface
        pattern passed."""
        screen_w, screen_h = screen.get_size()
        bg_w, bg_h = surface.get_size()
        for x in range(0, screen_w, bg_w):
            for y in range(0, screen_h, bg_h):
                screen.blit(surface, (x, y))
