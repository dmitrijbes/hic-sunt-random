import random
import copy

class Character():
    def __init__(self, directions):
        self.directions = directions

    def get_directions(self):
        return self.directions


def create_characters(characters_amount, character_directions_amount, directions=[(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]):
    characters = []

    for j in range(characters_amount):
        character_directions = []
        for i in range(character_directions_amount):
            random_direction = random.randint(0, len(directions) - 1)
            character_directions.append(directions[random_direction])
        characters.append(Character(character_directions))

    return characters


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


def get_grow_directions(world, directions, seed_x, seed_y, field_type):
    grow_directions = []
    for direction_x, direction_y in directions:
        grow_x = seed_x + direction_x
        grow_y = seed_y + direction_y
        if is_inside_world(world, grow_x, grow_y) and isinstance(world.world_objects[grow_x][grow_y], field_type):
            grow_directions.append((grow_x, grow_y))

    return grow_directions


def plant_seeds(world, seed_type, seeds_amount, field_type):
    planted_seeds = []

    for i in range(seeds_amount):
        world_size_x, world_size_y = world.size
        random_pos_x = random.randint(1, world_size_x - 2)
        random_pos_y = random.randint(1, world_size_y - 2)
        while not isinstance(world.world_objects[random_pos_x][random_pos_y], field_type) or (random_pos_x, random_pos_y) in planted_seeds:
            random_pos_x = random.randint(1, world_size_x - 2)
            random_pos_y = random.randint(1, world_size_y - 2)
        world.set_cell(seed_type, random_pos_x, random_pos_y)
        planted_seeds.append((random_pos_x, random_pos_y))


def grow_seeds(world, characters, seed_type, field_type, grow_rate):
    for i in range(grow_rate):
        temp_world_objects = copy.deepcopy(world.world_objects)
        for x, y in world.get_world_objects(field_type):
            rand_character = random.randint(0, len(characters) - 1)
            grow_directions = get_grow_directions(world, characters[rand_character].get_directions(), x, y, field_type)
            if not grow_directions:
                continue

            rand_direction_index = random.randint(0, len(grow_directions) - 1)
            grow_x, grow_y = grow_directions[rand_direction_index]
            world.set_cell(seed_type, grow_x, grow_y)
