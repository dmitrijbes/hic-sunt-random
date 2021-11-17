import random
import argparse

import world_generator
import world_renderer
from world_entities import WorldSettings


def parse_user_arguments():
    parser = argparse.ArgumentParser(
        description='User parameters for the world generation.')
    parser.add_argument('--mountain_seeds_amount', type=int, default=6,
                        help='Provides amount of mountain seeds (default: 6).')
    args = parser.parse_args()


def main():

    print("Welcome to hic sunt random!")

    world_settings = WorldSettings()
    init_world_settings(world_settings)

    print("Starting to generate world..")
    world = world_generator.generate_world(world_settings)

    print("Starting to render world..")
    world_renderer.render_world(world)

    # generate_many_worlds()

    print("Hic sunt random work finshed! Enjoy.")


def init_world_settings(world_settings):
    world_settings.mountain_settings.seeds_amount = 6
    world_settings.mountain_settings.growth_rate = 5
    world_settings.land_settings.seeds_amount = 6
    world_settings.land_settings.growth_rate = 20
    world_settings.forest_settings.seeds_amount = 10
    world_settings.forest_settings.growth_rate = 4
    world_settings.city_settings.seeds_amount = 8
    world_settings.city_settings.growth_rate = 3
    world_settings.river_settings.river_seeds_count = 5
    world_settings.river_settings.river_length = 30


def randomize_world_settings(world_settings):
    world_settings.mountain_settings.seeds_amount = random.randint(0, 20)
    world_settings.mountain_settings.growth_rate = random.randint(0, 20)
    world_settings.land_settings.seeds_amount = random.randint(0, 20)
    world_settings.land_settings.growth_rate = random.randint(0, 20)
    world_settings.forest_settings.seeds_amount = random.randint(0, 10)
    world_settings.forest_settings.growth_rate = random.randint(0, 5)
    world_settings.city_settings.seeds_amount = random.randint(0, 15)
    world_settings.city_settings.growth_rate = random.randint(0, 3)


def generate_many_worlds():
    for _ in range(30):
        world_settings = WorldSettings()
        randomize_world_settings(world_settings)

        world = world_generator.generate_world(world_settings)

        world_renderer.render_world(world)


if __name__ == '__main__':
    main()
