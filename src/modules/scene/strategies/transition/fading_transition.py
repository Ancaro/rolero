### Fading Transition Strategy ###

# Main
import pygame
from typing import Tuple

# Interfaces
from .i_transition import ITransitionStrategy
from src.modules.scene.models import IScene, TransitionStates



class FadingTransitionStrategy(ITransitionStrategy):

    def __init__(self):
        super().__init__()
        self.fading = None
        self.alpha = 0
        self.alpha_step = 8
        sr = pygame.display.get_surface().get_rect()
        self.veil = pygame.Surface(sr.size)
        self.veil.fill((0, 0, 0))
        self.veil.set_alpha(self.alpha)
    
    def transition(self, cs: IScene, ns: IScene, ts: TransitionStates, screen) -> Tuple[IScene, IScene, TransitionStates]:
        """Transition between current scene and next scene using a fading animation."""
        cs.render(screen)
        next_cs = cs
        next_ns = ns
        next_ts = ts

        if ts == TransitionStates.OUT:
            self.alpha += self.alpha_step
            if self.alpha >= 255:
                next_ts = TransitionStates.IN
                next_cs = ns
                next_ns = None
        
        elif ts == TransitionStates.IN:
            self.alpha -= self.alpha_step
            if self.alpha <= 0:
                next_ts = TransitionStates.OFF
        
        self.veil.set_alpha(self.alpha)
        screen.blit(self.veil, (0,0))
        return next_cs, next_ns, next_ts
