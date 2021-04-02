import world_entities
import random
import copy

def generate_ocean(world):
    for x, world_objects_row in enumerate(world.world_objects):
        for y, world_object in enumerate(world_objects_row):
            world.world_objects[x][y] = world_entities.Ocean(x, y)

def is_inside_world(world, x, y):
    if x < 0 or y < 0:
        return False

    world_size_x, world_size_y = world.size
    if (x > world_size_x - 1) or (y > world_size_y - 1):
        return False

    return True

def throw_coin():
    if random.randint(0, 1) == 1:
        return True
    return False

def generate_land(world):
    land_seeds = 2
    for i in range(land_seeds):
        world_size_x, world_size_y = world.size
        random_pos_x = random.randint(1, world_size_x - 2)
        random_pos_y = random.randint(1, world_size_y - 2)

        world.world_objects[random_pos_x][random_pos_y] = world_entities.Field(random_pos_x, random_pos_y)

    land_grow_rate = 8
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(land_grow_rate):
        temp_world_objects = copy.deepcopy(world.world_objects)
        for x, world_objects_row in enumerate(temp_world_objects):
            for y, world_object in enumerate(world_objects_row):
                if isinstance(world_object, world_entities.Field):
                    for direction_x, direction_y in directions:
                        land_grow_x = x + direction_x
                        land_grow_y = y + direction_y
                        if is_inside_world(world, land_grow_x, land_grow_y) and throw_coin():
                                world.world_objects[land_grow_x][land_grow_y] = world_entities.Field(land_grow_x, land_grow_y)

def generate_mountains(world):
    pass

def generate_world(name, size_x, size_y):
    world = world_entities.World(name, size_x, size_y)

    print(world)
    generate_ocean(world)
    generate_land(world)
    generate_mountains(world)
    print(world)

    return world
