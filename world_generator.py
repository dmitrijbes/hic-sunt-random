from random import choice
from math import floor

import world_entities
import world_growth


def generate_ocean(world):
    world_x, world_y = world.size
    for cell_x in range(world_x):
        for cell_y in range(world_y):
            world.set_cell(world_entities.Ocean, cell_x, cell_y)


def generate_land(world, land_settings):
    world_growth.plant_seeds(
        world, world_entities.Field, land_settings.seeds_amount, world_entities.Ocean
    )

    characters = world_growth.create_characters(5, 2)

    world_growth.grow_seeds(
        world,
        characters,
        world_entities.Field,
        world_entities.Ocean,
        land_settings.growth_rate,
    )


def generate_mountains(world, mountain_settings):
    world_growth.plant_seeds(
        world,
        world_entities.Mountain,
        mountain_settings.seeds_amount,
        world_entities.Field,
    )

    characters = world_growth.create_characters(
        5, 2, directions=[(-1, 0), (0, 1), (-1, 1), (1, -1)]
    )

    world_growth.grow_seeds(
        world,
        characters,
        world_entities.Mountain,
        world_entities.Field,
        mountain_settings.growth_rate,
    )


def is_good_river_direction(world, parent_cell, direction):
    cell_x = parent_cell[0] + direction[0]
    cell_y = parent_cell[1] + direction[1]

    if not world_growth.is_inside_world(world, cell_x, cell_y):
        return False

    is_good_neighbour_count = (
        world_growth.get_neighbors_count(world, world_entities.River, cell_x, cell_y)
        < 2
    )
    is_ocean = isinstance(world.world_objects[cell_x][cell_y], world_entities.Ocean)

    return is_good_neighbour_count and not is_ocean


def generate_river(world, river_settings):
    directions = [(1, -1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (-1, 1)]

    for _ in range(river_settings.river_seeds_count):
        fields = world.get_world_objects(world_entities.Field)
        if not fields:
            return
        field = choice(fields)
        cell_x = field[0]
        cell_y = field[1]

        world.set_cell(world_entities.River, cell_x, cell_y)

        for _ in range(river_settings.river_length):
            rand_direction = choice(directions)
            max_tries = 20
            tries_count = 0
            while not is_good_river_direction(world, (cell_x, cell_y), rand_direction):
                rand_direction = choice(directions)
                tries_count = tries_count + 1
                if tries_count > max_tries:
                    break
            if tries_count > max_tries:
                break
            cell_x = cell_x + rand_direction[0]
            cell_y = cell_y + rand_direction[1]

            world.set_cell(world_entities.River, cell_x, cell_y)


def generate_forests(world, forest_settings):
    world_growth.plant_seeds_where(
        world,
        world_entities.Forest,
        floor(forest_settings.seeds_amount / 3 * 2),
        world_entities.Field,
        adjacent_types=[world_entities.Mountain],
    )
    world_growth.plant_seeds_among(
        world,
        world_entities.Forest,
        floor(forest_settings.seeds_amount / 3 * 1),
        world_entities.Field,
        world_entities.Field,
    )

    characters = world_growth.create_characters(5, 4)

    world_growth.grow_seeds(
        world,
        characters,
        world_entities.Forest,
        world_entities.Field,
        forest_settings.growth_rate,
    )


def generate_cities(world, city_settings):
    world_growth.plant_seeds_where(
        world,
        world_entities.City,
        floor(city_settings.seeds_amount / 5 * 3),
        world_entities.Field,
        adjacent_types=[world_entities.River],
    )
    world_growth.plant_seeds_where(
        world,
        world_entities.City,
        floor(city_settings.seeds_amount / 5 * 1),
        world_entities.Field,
        adjacent_types=[world_entities.Forest],
    )
    world_growth.plant_seeds_among(
        world,
        world_entities.City,
        floor(city_settings.seeds_amount / 5 * 1),
        world_entities.Field,
        world_entities.Field,
    )

    characters = world_growth.create_characters(5, 6)

    world_growth.grow_seeds_random(
        world,
        characters,
        world_entities.City,
        world_entities.Field,
        city_settings.growth_rate,
    )


def generate_world(world_settings):
    world = world_entities.World(
        world_settings.name, world_settings.size[0], world_settings.size[1]
    )

    generate_ocean(world)
    generate_land(world, world_settings.land_settings)
    generate_mountains(world, world_settings.mountain_settings)
    generate_forests(world, world_settings.forest_settings)
    generate_river(world, world_settings.river_settings)
    generate_cities(world, world_settings.city_settings)

    return world
