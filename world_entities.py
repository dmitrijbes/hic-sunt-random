import copy


class WorldObject:
    name = "world_object"

    def __init__(self, coordinate_x, coordinate_y):
        self.position = (coordinate_x, coordinate_y)


class Field(WorldObject):
    name = "field"


class Ocean(WorldObject):
    name = "ocean"


class Mountain(WorldObject):
    name = "mountain"


class River(WorldObject):
    name = "river"


class Forest(WorldObject):
    name = "forest"


class City(WorldObject):
    name = "city"


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
        if (
            type(self.world_objects[x][y]) in self.world_type_objects
            and (x, y) in self.world_type_objects[type(self.world_objects[x][y])]
        ):
            self.world_type_objects[type(self.world_objects[x][y])].remove((x, y))
        if not cell_type in self.world_type_objects:
            self.world_type_objects[cell_type] = []
        self.world_type_objects[cell_type].append((x, y))

        self.world_objects[x][y] = cell_type(x, y)

    def get_world_objects(self, object_type):
        if not object_type in self.world_type_objects:
            return []

        return copy.copy(self.world_type_objects[object_type])


class MountainSettings:
    seeds_amount = 2
    growth_rate = 2


class RiverSettings:
    river_seeds_count = 5
    river_length = 30


class LandSettings:
    seeds_amount = 2
    growth_rate = 2


class ForestSettings:
    seeds_amount = 2
    growth_rate = 2


class CitySettings:
    seeds_amount = 4
    growth_rate = 3


class WorldSettings:
    name = "Great Beet World"
    size = (100, 100)
    mountain_settings = MountainSettings()
    land_settings = LandSettings()
    forest_settings = ForestSettings()
    city_settings = CitySettings()
    river_settings = RiverSettings()
