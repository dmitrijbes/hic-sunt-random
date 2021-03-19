class WorldObject:
    def __init__(self, coordinate_x, coordinate_y):
        self.position = (coordinate_x, coordinate_y)

class Field(WorldObject):
    pass

class Ocean(WorldObject):
    pass

class Mountain(WorldObject):
    pass

class World:
    def __init__(self, name, size_x, size_y):
        self.name = name
        self.size = (size_x, size_y)
        self.world_objects = []
        for x in range(size_x):
            world_objects_row = []
            for y in range(size_y):
                world_objects_row.append(WorldObject(x,y))

            self.world_objects.append(world_objects_row)

    def __str__(self):
        return f"World; name:{self.name} size_x:{self.size[0]} size_y:{self.size[1]}"
