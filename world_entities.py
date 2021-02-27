class World:
    def __init__(self, name, size_x, size_y):
        self.name = name
        self.size = (size_x, size_y)

    def __str__(self):
        return f"World; name:{self.name} size_x:{self.size[0]} size_y:{self.size[1]}"
