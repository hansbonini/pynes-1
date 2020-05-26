from renderers.pygame import PygameRenderer
class RendererManager:
    def __init__(self, renderer="pygame"):
        if renderer == "pygame":
            self.display = PygameRenderer()