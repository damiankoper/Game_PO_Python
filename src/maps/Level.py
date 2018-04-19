from src.interfaces.MapInterface import MapInterface

class Level(MapInterface):
    def __init__(self, name):
        super().__init__()
        self.setName(name)

    def init(self):
        self.ground.clear()
        self.points.clear()

        self.ground = self.loadRects("ground")
        self.points = self.loadRects("points")
        self.finish = self.loadRects("finish")[0]

if __name__ == "__main__":
    level = Level("level1")