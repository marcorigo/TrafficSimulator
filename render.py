class RenderEngine:
    def __init__(self, canvas, pygame, width, height):
        self.pygame = pygame
        self.canvas = canvas
        self.width = width
        self.height = height
        # self.car = self.pygame.image.load('car.png').convert_alpha()
        self.car = self.pygame.Surface((50, 50), self.pygame.SRCALPHA)

    def drawVeichle(self, position, width, height, angle, fvW, fvH):
        self.car.fill((0, 50, 90))
        self.car = self.pygame.transform.scale(self.car, (width, height))
        # self.car.convert()
        surf = self.pygame.transform.rotate(self.car, angle)
        surf_rect = self.car.get_rect()
        surf_rect.center = position
        self.canvas.blit(surf, surf_rect)

        # self.pygame.draw.rect(self.canvas, (20, 60, 30), (position.x, position.y, 4, 4))

        sqr =  self.pygame.Surface((10, 10), self.pygame.SRCALPHA)
        sqr.fill((150, 50, 20))
        surf = self.pygame.transform.rotate(sqr, angle)
        self.canvas.blit(surf, position + (width / 2, height / 2))

        # # self.car = self.pygame.transform.scale(self.car, (width, height))
        # self.car =  self.pygame.Surface((50, 50))
        # # making a copy of the old center of the rectangle 
        # rect = self.car.get_rect()
        # rect.center = (width / 2, height / 2)
        # old_center = rect.center 
        # # defining angle of the rotation  
        # rot = angle
        # # rotating the orignal image  
        # new_image = self.pygame.transform.rotate(self.car , rot)   
        # # set the rotated rectangle to the old center  
        # rect.center = old_center  
        # # drawing the rotated rectangle to the screen  
        # self.canvas.blit(new_image , rect) 

    def drawRect(self, x, y, width, height, color):
        self.pygame.draw.rect(self.canvas, color, (x, y, width, height))

    def move(self, element, x = 0, y = 0):
        self.canvas.move(element, x, y)
