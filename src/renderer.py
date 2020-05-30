from renderers.sdl2 import SDLRenderer
from renderers.pygame import PygameRenderer
from renderers.ncurse import NcurseRenderer
from renderers.pyglet import PygletRenderer


class RendererManager:
    def __init__(self, renderer="sdl2"):
        if renderer == "sdl2":
            self.display = SDLRenderer()
        elif renderer == "pygame":
            self.display = PygameRenderer()
        elif renderer == "pyglet":
            self.display = PygletRenderer()
        elif renderer == "ncurse":
            self.display = NcurseRenderer()
