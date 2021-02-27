class World:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

    def __str__(self):
        return f"World: size_x:{self.size_x} size_y:{self.size_y}"
