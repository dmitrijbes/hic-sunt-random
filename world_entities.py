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
        for y in range(size_y):
            world_objects_row = []
            for x in range(size_x):
                world_objects_row.append(WorldObject(x,y))

            self.world_objects.append(world_objects_row)

    def __str__(self):
        for world_objects_row in self.world_objects:
            for world_object in world_objects_row:
                if isinstance(world_object, Mountain):
                    print("^", end="")
                elif isinstance(world_object, Field):
                    print("#", end="")
                elif isinstance(world_object, Ocean):
                    print("~", end="")
                else:
                    print("_", end="")
            print("")

        return f"World; name:{self.name} size_x:{self.size[0]} size_y:{self.size[1]}"
