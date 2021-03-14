class World:
    def __init__(self, name, size_x, size_y):
        self.name = name
        self.size = (size_x, size_y)

    def __str__(self):
        return f"World; name:{self.name} size_x:{self.size[0]} size_y:{self.size[1]}"

<<<<<<< HEAD
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
=======
    def __iter__(self):
        # yield from self.world_entities
        pass
>>>>>>> c8cd64e2764bd6d7b13226b003f5fe6fc007d14a
