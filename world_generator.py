from world_entities import World

def generate_ocean(world):
    pass

def generate_land(world):
    pass

def generate_mountains(world):
    pass

def generate_world(name, size_x, size_y):
    world = World(name, size_x, size_y)

    generate_ocean(world)
    generate_land(world)
    generate_mountains(world)

    return World("Great Beet", 5, 5)
