import world_entities
import random

def generate_ocean(world):
    for x, world_objects_row in enumerate(world.world_objects):
        for y, world_object in enumerate(world_objects_row):
            world.world_objects[x][y] = world_entities.Ocean(x, y)

def generate_land(world):
    land_seeds = 3
    for i in range(land_seeds):
        world_size_x, world_size_y = world.size
        random_pos_x = random.randint(1, world_size_x - 2)
        random_pos_y = random.randint(1, world_size_y - 2)

        world.world_objects[random_pos_x][random_pos_y] = world_entities.Field(random_pos_x, random_pos_y)

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
