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

def get_neighbours_count(world, world_object, x, y):
    neighbours_count = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
    for direction_x, direction_y in directions:
        neighbour_x = x + direction_x
        neighbour_y = y + direction_y
        if is_inside_world(world, neighbour_x, neighbour_y) and isinstance(world.world_objects[neighbour_x][neighbour_y], world_object):
            neighbours_count += 1

    return neighbours_count

def throw_coin():
    if random.randint(0, 1) == 1:
        return True
    return False

def generate_land(world, land_seeds, land_grow_rate):
    for i in range(land_seeds):
        world_size_x, world_size_y = world.size
        random_pos_x = random.randint(1, world_size_x - 2)
        random_pos_y = random.randint(1, world_size_y - 2)

        world.world_objects[random_pos_x][random_pos_y] = world_entities.Field(random_pos_x, random_pos_y)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
    characters = []
    max_characters = 6
    character_force = 2
    for j in range(max_characters):
        character_directions = []
        for i in range(character_force):
            random_direction = random.randint(0, len(directions) - 1)
            character_directions.append(directions[random_direction])
        characters.append(character_directions)

    for i in range(land_grow_rate):
        temp_world_objects = copy.deepcopy(world.world_objects)
        for x, world_objects_row in enumerate(temp_world_objects):
            for y, world_object in enumerate(world_objects_row):
                if isinstance(world_object, world_entities.Field):
                    rand_character = random.randint(0, len(characters) - 1)

                    for direction_x, direction_y in characters[rand_character]:
                        land_grow_x = x + direction_x
                        land_grow_y = y + direction_y
                        if is_inside_world(world, land_grow_x, land_grow_y) and throw_coin():
                                world.world_objects[land_grow_x][land_grow_y] = world_entities.Field(land_grow_x, land_grow_y)

def get_mountain_grow_directions(directions, world, x, y):
    grow_directions = []
    for direction_x, direction_y in directions:
        mountain_grow_x = x + direction_x
        mountain_grow_y = y + direction_y
        if is_inside_world(world, mountain_grow_x, mountain_grow_y) and isinstance(world.world_objects[mountain_grow_x][mountain_grow_y], world_entities.Field):
            grow_directions.append((direction_x, direction_y))

    return grow_directions

def generate_mountains(world, mountain_seeds, mountain_grow_rate, mountain_grow_size):
    for i in range(mountain_seeds):
        world_size_x, world_size_y = world.size
        random_pos_x = random.randint(1, world_size_x - 2)
        random_pos_y = random.randint(1, world_size_y - 2)
        while not isinstance(world.world_objects[random_pos_x][random_pos_y], world_entities.Field):
            random_pos_x = random.randint(1, world_size_x - 2)
            random_pos_y = random.randint(1, world_size_y - 2)
        world.world_objects[random_pos_x][random_pos_y] = world_entities.Mountain(random_pos_x, random_pos_y)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
    characters = []
    max_characters = 3
    character_force = 2
    for j in range(max_characters):
        character_directions = []
        for i in range(character_force):
            random_direction = random.randint(0, len(directions) - 1)
            character_directions.append(directions[random_direction])
        characters.append(character_directions)

    for i in range(mountain_grow_rate):
        temp_world_objects = copy.deepcopy(world.world_objects)
        for x, world_objects_row in enumerate(temp_world_objects):
            for y, world_object in enumerate(world_objects_row):
                if isinstance(world_object, world_entities.Mountain):
                    rand_character = random.randint(0, len(characters) - 1)
                    grow_directions = get_mountain_grow_directions(characters[rand_character], world, x, y)

                    if not grow_directions:
                        continue

                    direction_index = random.randint(0, len(grow_directions) - 1)
                    direction_x, direction_y = grow_directions[direction_index]
                    mountain_grow_x = x + direction_x
                    mountain_grow_y = y + direction_y
                    world.world_objects[mountain_grow_x][mountain_grow_y] = world_entities.Mountain(mountain_grow_x, mountain_grow_y)

# # def 555get_mountain_grow_directions(directions, world, x, y):
#     grow_directions = []
#     for direction_x, direction_y in directions:
#         mountain_grow_x = x + direction_x
#         mountain_grow_y = y + direction_y
#         if is_inside_world(world, mountain_grow_x, mountain_grow_y) and isinstance(world.world_objects[mountain_grow_x][mountain_grow_y], world_entities.Field):
#             grow_directions.append((direction_x, direction_y))

#     return grow_directions

# def 555generate_mountains(world, mountain_seeds, mountain_grow_rate, mountain_grow_size):
#     for i in range(mountain_seeds):
#         world_size_x, world_size_y = world.size
#         random_pos_x = random.randint(1, world_size_x - 2)
#         random_pos_y = random.randint(1, world_size_y - 2)
#         while not isinstance(world.world_objects[random_pos_x][random_pos_y], world_entities.Field):
#             random_pos_x = random.randint(1, world_size_x - 2)
#             random_pos_y = random.randint(1, world_size_y - 2)
#         world.world_objects[random_pos_x][random_pos_y] = world_entities.Mountain(random_pos_x, random_pos_y)

#     directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
#     characters = []
#     max_characters = 3
#     character_force = 2
#     for j in range(max_characters):
#         character_directions = []
#         for i in range(character_force):
#             random_direction = random.randint(0, len(directions) - 1)
#             character_directions.append(directions[random_direction])
#         characters.append(character_directions)

#     for i in range(mountain_grow_rate):
#         temp_world_objects = copy.deepcopy(world.world_objects)
#         for x, world_objects_row in enumerate(temp_world_objects):
#             for y, world_object in enumerate(world_objects_row):
#                 if isinstance(world_object, world_entities.Mountain):
#                     rand_character = random.randint(0, len(characters) - 1)
#                     grow_directions = get_mountain_grow_directions(characters[rand_character], world, x, y)

#                     if not grow_directions:
#                         continue

#                     direction_index = random.randint(0, len(grow_directions) - 1)
#                     direction_x, direction_y = grow_directions[direction_index]
#                     mountain_grow_x = x + direction_x
#                     mountain_grow_y = y + direction_y
#                     world.world_objects[mountain_grow_x][mountain_grow_y] = world_entities.Mountain(mountain_grow_x, mountain_grow_y)
def generate_lake():
    pass

def get_river_grow_directions(river_grow_size, world, x, y):
    river_directions = [(1, -1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (-1, 1)]
    # river_directions = [(0, 1), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
    river_grow_directions = []
    for direction_x, direction_y in river_directions:
        river_grow_x = x + direction_x
        river_grow_y = y + direction_y
        if not river_grow_directions:
            if is_inside_world(world, river_grow_x, river_grow_y) and (isinstance(world.world_objects[river_grow_x][river_grow_y], world_entities.Field) or isinstance(world.world_objects[river_grow_x][river_grow_y], world_entities.Mountain)) and get_neighbours_count(world, world_entities.River, river_grow_x, river_grow_y) < river_grow_size:
               river_grow_directions.append((direction_x, direction_y))
        else:
            if is_inside_world(world, river_grow_x, river_grow_y) and (isinstance(world.world_objects[river_grow_x][river_grow_y], world_entities.Field) or isinstance(world.world_objects[river_grow_x][river_grow_y], world_entities.Mountain)) and get_neighbours_count(world, world_entities.River, river_grow_x, river_grow_y) < river_grow_size and (direction_x, direction_y) != river_grow_directions[-1]:
                river_grow_directions.append((direction_x, direction_y))

    return river_grow_directions


def generate_river(world, river_seeds, river_grow_rate, river_grow_size):
    for i in range(river_seeds):
        world_size_x, world_size_y = world.size
        riv_random_pos_x = random.randint(1, world_size_x - 2)
        riv_random_pos_y = random.randint(1, world_size_y - 2)
        while isinstance(world.world_objects[riv_random_pos_x][riv_random_pos_y], world_entities.Ocean):
            riv_random_pos_x = random.randint(1, world_size_x - 2)
            riv_random_pos_y = random.randint(1, world_size_y - 2)
        world.world_objects[riv_random_pos_x][riv_random_pos_y] = world_entities.River(riv_random_pos_x, riv_random_pos_y)

    for i in range(river_grow_rate):
        temp_world_objects = copy.deepcopy(world.world_objects)
        for x, world_objects_row in enumerate(temp_world_objects):
            for y, world_object in enumerate(world_objects_row):
                if isinstance(world_object, world_entities.River):
                    river_grow_directions = get_river_grow_directions(river_grow_size, world, x, y)
                    if not river_grow_directions:
                        continue

                    #random_values=[]
                    riv_direction_index = random.randint(0, len(river_grow_directions) - 1)
                    #random_values.append(riv_direction_index)
                    direction_x, direction_y = river_grow_directions[riv_direction_index]
                    river_grow_x = x + direction_x
                    river_grow_y = y + direction_y
                    world.world_objects[river_grow_x][river_grow_y] = world_entities.River(river_grow_x, river_grow_y)

def generate_forest():
    pass

def generate_world(name, size_x, size_y):
    world = world_entities.World(name, size_x, size_y)

    generate_ocean(world)

    land_seeds = 10
    land_grow_rate = 30
    generate_land(world, land_seeds, land_grow_rate)

    mountain_seeds = 3
    mountain_grow_rate = 6
    mountain_grow_size = 3
    generate_mountains(world, mountain_seeds, mountain_grow_rate, mountain_grow_size)

    river_seeds = 5
    river_grow_rate = 10
    river_grow_size = 2
    generate_river(world, river_seeds, river_grow_rate, river_grow_size)



    generate_forest()
    generate_lake()
    # print(world)

    return world
