import pygame

class PygameRenderer:
    class NormalLayer:
        def __init__(self):
            self.layer = pygame.Surface((256,240))
            
        def clear(self):
            self.layer.fill((0, 0, 0))

        def blit(self, element=None, position=(0,0), color=(0,0,0)):
            self.layer.blit(element, position, color)

        def read(self, x, y):
            matrix = pygame.PixelArray(self.layer)
            value = matrix[x,y]
            del matrix
            return value

        def write(self, x, y, value):
            matrix = pygame.PixelArray(self.layer)
            matrix[x,y] = value
            del matrix

    class AlphaLayer:
        def __init__(self):
            self.layer = pygame.Surface((256,240), pygame.SRCALPHA)
            
        def clear(self):
            self.layer.fill((0, 0, 0, 0))

        def blit(self, element=None, position=(0,0), color=(0,0,0,0)):
            self.layer.blit(element, position, color)

        def text(self, message=""):
            self.clear()
            font = pygame.font.Font(pygame.font.get_default_font(), 8)
            self.layer.blit(font.render(message, False, (255, 255, 255, 1), (0,0,0,0)),(4,220))

        def read(self, x, y):
            matrix = pygame.PixelArray(self.layer)
            value = matrix[x,y]
            del matrix
            return value

        def write(self, x, y, value):
            matrix = pygame.PixelArray(self.layer)
            matrix[x,y] = value
            del matrix

    def __init__(self):
        self.layers = ["LAYER_B", "LAYER_A", "DEBUG_LAYER"]

        try:
            pygame.init()   
            self.SCREEN = pygame.display.set_mode((256, 240))
            self.LAYER_B = PygameRenderer.NormalLayer()
            self.LAYER_A = PygameRenderer.AlphaLayer()
            self.DEBUG_LAYER = PygameRenderer.AlphaLayer()
            self.reset()
        except:
           print ("Initialize Video Error with Pygame as Renderer")
        super(PygameRenderer, self).__init__()

    def reset(self):
        self.clear()
        self.blit()
        
    def clear(self):
        tl = self.layers.__len__()
        i=0
        while i < tl:
            l=getattr(self, self.layers[i])
            l.clear()
            del l
            i+=1
        pygame.display.flip()

    def blit(self):
        tl = self.layers.__len__()
        i=0
        while i < tl:
            l=getattr(self, self.layers[i])
            self.SCREEN.blit(l.layer, (0,0))
            del l
            i+=1
        pygame.display.update()
        