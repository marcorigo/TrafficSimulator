from car import Car
from roads import roadBuilder

class Map:
    def __init__(self, renderEngine, road_map, cell_width):
        self.renderEngine = renderEngine
        self.veichles = []
        self.map = road_map
        self.cell_width = cell_width

    def createRoads(self, road_map):
        for x in range(len(road_map)):
            for y in range(len(road_map[0])):
                road_type = road_map[x][y]
                road = roadBuilder(road_type, x, y, self.cell_width, rotation = road_type)
                self.map[x][y] = road

    def addVeichle(self):
        veichle = Car( cell_width = self.cell_width)
        self.veichles.append(veichle)
        return veichle

    def update(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                road = self.map[x][y]
                if road:
                    road.draw(self.renderEngine)
        for veichle in self.veichles:
            self.renderEngine.drawVeichle(veichle.x, veichle.y, veichle.width, veichle.heigth, veichle.angle)
            veichle.move()
            veichle.updatePosition()
            # self.renderEngine.move(veichle.model, veichle.speed, 0)