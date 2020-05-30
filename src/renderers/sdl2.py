import sdl2
import sdl2.ext
from sdl2 import blendmode, pixels, rect, surface, rwops, error


class SDLRenderer:
    class NormalLayer:
        def __init__(self, sf):
            self.layer = sf
            matrix = sdl2.ext.PixelView(self.layer)
            color = sdl2.ext.Color(255,0,0)
            for x in range(0,256):
                for y in range(0,240):
                    matrix[y][x] = color
            del matrix


        def clear(self):
            matrix = sdl2.ext.PixelView(self.layer)
            color = sdl2.ext.Color(0,0,0)
            for x in range(0,256):
                for y in range(0,240):
                    matrix[y][x] = color
            del matrix


        def blit(self, element=None, position=(0, 0), color=(0, 0, 0)):
            self.layer.blit(element, position, color)

        def read(self, x, y):
            matrix = sdl2.ext.PixelView(self.layer)
            value = matrix[y][x]
            del matrix
            return value

        def write(self, x, y, value):
            matrix = sdl2.ext.PixelView(self.layer)
            matrix[y][x] = value
            del matrix

    class AlphaLayer:
        def __init__(self,sf):
            factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
            self.layer = factory.from_color(sdl2.ext.Color(0,0,0,0), size=(256,240))
            matrix = sdl2.ext.PixelView(self.layer)
            color = sdl2.ext.Color(255,0,0)
            for x in range(0,256):
                for y in range(0,240):
                    matrix[y][x] = color
            del matrix

        def clear(self):
            pass
            matrix = sdl2.ext.PixelView(self.layer)
            color = sdl2.ext.Color(255,0,0)
            for x in range(0,256):
                for y in range(0,240):
                    matrix[y][x] = color
            del matrix

        def blit(self, element=None, position=(0, 0), color=(0, 0, 0, 0)):
            self.layer.blit(element, position, color)

        def text(self, message=""):
            self.clear()
            #font = pygame.font.Font(pygame.font.get_default_font(), 8)
            #self.layer.blit(
            #    font.render(message, False, (255, 255, 255, 1), (0, 0, 0, 0)),
            #    (4, 220))

        def read(self, x, y):
            matrix = sdl2.ext.PixelView(self.layer)
            value = matrix[y][x]
            del matrix
            return value

        def write(self, x, y, value):
            matrix = sdl2.ext.PixelView(self.layer)
            matrix[y][x] = sdl2.ext.Color(value)
            del matrix

    def __init__(self):
        self.layers = ["LAYER_B", "LAYER_A", "DEBUG_LAYER"]

        #try:
        sdl2.ext.init()
        self.SCREEN = sdl2.ext.Window("PyNES - SDL", size=(256, 240))
        sf = self.SCREEN.get_surface()
        self.LAYER_B = SDLRenderer.NormalLayer(sf)
        self.LAYER_A = SDLRenderer.AlphaLayer(sf)
        self.DEBUG_LAYER = SDLRenderer.AlphaLayer(sf)
        self.SCREEN.show()
        self.reset()
        #except:
        #   print ("Initialize Video Error with Pygame as Renderer")
        super(SDLRenderer, self).__init__()

    def reset(self):
        tl = self.layers.__len__()
        i = 0
        while i < tl:
            l = getattr(self, self.layers[i])
            l.clear()
            del l
            i += 1
        self.clear()
        self.blit()

    def clear(self):
        pass
        # tl = self.layers.__len__()
        # i = 0
        # while i < tl:
        #     l = getattr(self, self.layers[i])
        #     l.clear()
        #     del l
        #     i += 1
        sdl2.ext.Window.refresh(self.SCREEN)

    def blit(self):
        # tl = self.layers.__len__()
        # i = 0
        # while i < tl:
        #     l = getattr(self, self.layers[i])
        #     l.blit()
        #     del l
        #     i += 1
        pass
