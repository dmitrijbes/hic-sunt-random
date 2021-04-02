import world_entities

def generate_ocean(world):
    for world_objects_row in world.world_objects:
        for world_object in world_objects_row:
            pos_x, pos_y = world_object.position
            world_object = world_entities.Ocean(pos_x, pos_y)

def generate_land(world):
    pass

def generate_mountains(world):
    pass

def generate_world(name, size_x, size_y):
    world = world_entities.World(name, size_x, size_y)
    print(world)
    generate_ocean(world)
    print("")
    print(world)

    generate_land(world)
    generate_mountains(world)

    return world
