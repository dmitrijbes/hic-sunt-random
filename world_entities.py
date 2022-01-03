from copy import copy


class WorldObject:
    name = "world_object"

    def __init__(self, x, y):
        self.position = (x, y)


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


class World:
    def __init__(self, name, size_x, size_y):
        self.name = name
        self.size = (size_x, size_y)
        self.world_objects = []
        self.world_type_objects = {}

        for x_cord in range(size_x):
            world_objects_row = []
            for y_cord in range(size_y):
                world_objects_row.append(WorldObject(x_cord, y_cord))

            self.world_objects.append(world_objects_row)

    def set_cell(self, cell_type, x_cord, y_cord):
        # pylint: disable=unidiomatic-typecheck
        if (
            type(self.world_objects[x_cord][y_cord]) in self.world_type_objects
            and (x_cord, y_cord)
            in self.world_type_objects[type(self.world_objects[x_cord][y_cord])]
        ):
            self.world_type_objects[type(self.world_objects[x_cord][y_cord])].remove(
                (x_cord, y_cord)
            )
        if not cell_type in self.world_type_objects:
            self.world_type_objects[cell_type] = []
        self.world_type_objects[cell_type].append((x_cord, y_cord))

        self.world_objects[x_cord][y_cord] = cell_type(x_cord, y_cord)

    def get_world_objects(self, object_type):
        if not object_type in self.world_type_objects:
            return []

        return copy(self.world_type_objects[object_type])


class WorldSettings:
    name = "Great Beet World"
    size = (100, 100)
    mountain_settings = MountainSettings()
    land_settings = LandSettings()
    forest_settings = ForestSettings()
    city_settings = CitySettings()
    river_settings = RiverSettings()
