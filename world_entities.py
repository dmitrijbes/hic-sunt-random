class World:
    def __init__(self, name, size_x, size_y):
        self.name = name
        self.size = (size_x, size_y)

    def __str__(self):
        return f"World; name:{self.name} size_x:{self.size[0]} size_y:{self.size[1]}"

_new_world_matrix = [
    []
]

object = 


class WorldObject:
    def __init__(self, coordinate_x, coordinate_y)
        self.position = (coordinate_x, coordinate_y)


class Field(WorldObject):
    pass


class Ocean(WorldObject):
    pass


class Mountain(WorldObject):
    pass