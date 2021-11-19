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
    parser.add_argument('--mountain_growth_rate', type=int, default=5,
                        help='Provides growth rate of mountains (default: 5).')
    parser.add_argument('--land_seeds_amount', type=int, default=6,
                        help='Provides amount of land seeds (default: 6).')
    parser.add_argument('--land_growth_rate', type=int, default=20,
                        help='Provides growth rate of land (default: 20).')
    parser.add_argument('--forest_seeds_amount', type=int, default=10,
                        help='Provides amount of forest seeds (default: 10).')
    parser.add_argument('--forest_growth_rate', type=int, default=4,
                        help='Provides growth rate of forest (default: 4).')
    parser.add_argument('--city_seeds_amount', type=int, default=8,
                        help='Provides amount of city seeds (default: 8).')
    parser.add_argument('--city_growth_rate', type=int, default=3,
                        help='Provides growth rate of cities (default: 3).')
    parser.add_argument('--river_seeds_amount', type=int, default=5,
                        help='Provides amount of river seeds (default: 5).')
    parser.add_argument('--river_length', type=int, default=30,
                        help='Provides river length (default: 30).')

    args = parser.parse_args()

    return args


def parameters_to_world_settings(world_settings, args):
    world_settings.mountain_settings.seeds_amount = args.mountain_seeds_amount
    world_settings.mountain_settings.growth_rate = args.mountain_growth_rate
    world_settings.land_settings.seeds_amount = args.land_seeds_amount
    world_settings.land_settings.growth_rate = args.land_growth_rate
    world_settings.forest_settings.seeds_amount = args.forest_seeds_amount
    world_settings.forest_settings.growth_rate = args.forest_growth_rate
    world_settings.city_settings.seeds_amount = args.city_seeds_amount
    world_settings.city_settings.growth_rate = args.city_growth_rate
    world_settings.river_settings.river_seeds_count = args.river_seeds_amount
    world_settings.river_settings.river_length = args.river_length


def main():

    world_settings = WorldSettings()
    args = parse_user_arguments()
    parameters_to_world_settings(world_settings, args)

    print("Welcome to hic sunt random!")

    print("Starting to generate world..")
    world = world_generator.generate_world(world_settings)

    print("Starting to render world..")
    world_renderer.render_world(world)

    # generate_many_worlds()

    print("Hic sunt random work finshed! Enjoy.")


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
