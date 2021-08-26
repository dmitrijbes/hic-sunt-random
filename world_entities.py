import copy


class WorldObject:
    def __init__(self, coordinate_x, coordinate_y):
        self.position = (coordinate_x, coordinate_y)


class Field(WorldObject):
    pass


class Ocean(WorldObject):
    pass


class Mountain(WorldObject):
    pass


class River(WorldObject):
    pass


class World:
    def __init__(self, name, size_x, size_y):
        self.name = name
        self.size = (size_x, size_y)
        self.world_objects = []
        self.world_type_objects = {}
        for x in range(size_x):
            world_objects_row = []
            for y in range(size_y):
                world_objects_row.append(WorldObject(x, y))

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

    def set_cell(self, cell_type, x, y):
        if type(self.world_objects[x][y]) in self.world_type_objects:
            self.world_type_objects[type(
                self.world_objects[x][y])].remove((x, y))
        if not cell_type in self.world_type_objects:
            self.world_type_objects[cell_type] = []
        self.world_type_objects[cell_type].append((x, y))

        self.world_objects[x][y] = cell_type(x, y)

    def get_world_objects(self, object_type):
        return copy.copy(self.world_type_objects[object_type])
