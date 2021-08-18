import world_entities
import world_growth
import random
import copy

def generate_ocean(world):
    for x, world_objects_row in enumerate(world.world_objects):
        for y, world_object in enumerate(world_objects_row):
            world.world_objects[x][y] = world_entities.Ocean(x, y)

def generate_land(world, land_seeds, land_grow_rate):
    world_growth.plant_seeds(world, world_entities.Field, land_seeds, world_entities.Ocean)

    characters = world_growth.create_characters(3, 2, directions=[(0, 1), (1,0), (1,1)])

    world_growth.grow_seeds(world, characters, world_entities.Field, world_entities.Ocean, land_grow_rate)

def generate_mountains(world, mountain_seeds_amount, mountain_grow_rate):
    world_growth.plant_seeds(world, world_entities.Mountain, mountain_seeds_amount, world_entities.Field)

    characters = world_growth.create_characters(3, 2)

    world_growth.grow_seeds(world, characters, world_entities.Mountain, world_entities.Field, mountain_grow_rate)

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


def generate_river_by_elia(world, river_seeds):
    elias_planted_seeds = []
    for i in range(river_seeds):
        world_size_x, world_size_y = world.size
        riv_random_pos_x = random.randint(1, world_size_x - 2)
        riv_random_pos_y = random.randint(1, world_size_y - 2)
        while isinstance(world.world_objects[riv_random_pos_x][riv_random_pos_y], world_entities.Ocean):
            riv_random_pos_x = random.randint(1, world_size_x - 2)
            riv_random_pos_y = random.randint(1, world_size_y - 2)
        world.world_objects[riv_random_pos_x][riv_random_pos_y] = world_entities.River(riv_random_pos_x, riv_random_pos_y)
        elias_planted_seeds.append((riv_random_pos_x, riv_random_pos_y))

    for river_seed in elias_planted_seeds:
        riv_seed_x, riv_seed_y = river_seed
        river_directions = [(1, -1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (-1, 1)]
        riv_random_direction = random.choice(river_directions)
        world.world_objects[riv_seed_x + riv_random_direction[0]][riv_seed_y + riv_random_direction[1]] = world_entities.River(riv_seed_x + riv_random_direction[0], riv_seed_y + riv_random_direction[1])


def generate_forest():
    pass

def generate_world(name, size_x, size_y):
    world = world_entities.World(name, size_x, size_y)

    generate_ocean(world)

    land_seeds = 6
    land_grow_rate = 20
    generate_land(world, land_seeds, land_grow_rate)

    mountain_seeds = 3
    mountain_grow_rate = 10
    generate_mountains(world, mountain_seeds, mountain_grow_rate)

    river_seeds = 5
    generate_river_by_elia(world, river_seeds)

    generate_forest()
    generate_lake()
    # print(world)

    return world
