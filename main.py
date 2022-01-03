from random import randint
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import world_generator
import world_renderer
from world_entities import WorldSettings


def parse_user_arguments():
    parser = ArgumentParser(
        description="World generation parameters.",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--worlds_amount",
        type=int,
        default=1,
        help="Amount of the worlds to generate.",
    )
    parser.add_argument(
        "--randomize_parameters", dest="randomize_parameters", action="store_true"
    )

    parser.add_argument(
        "--world_width",
        type=int,
        default=100,
        help="Width of the world.",
    )
    parser.add_argument(
        "--world_height",
        type=int,
        default=100,
        help="Height of the world.",
    )

    parser.add_argument(
        "--mountain_seeds_amount",
        type=int,
        default=6,
        help="Mountain seeds.",
    )
    parser.add_argument(
        "--mountain_growth_rate",
        type=int,
        default=5,
        help="Mountain growth rate.",
    )
    parser.add_argument(
        "--land_seeds_amount",
        type=int,
        default=6,
        help="Land seeds.",
    )
    parser.add_argument(
        "--land_growth_rate",
        type=int,
        default=20,
        help="Land growth rate.",
    )
    parser.add_argument(
        "--forest_seeds_amount",
        type=int,
        default=10,
        help="Forest seeds.",
    )
    parser.add_argument(
        "--forest_growth_rate",
        type=int,
        default=4,
        help="Forest growth rate.",
    )
    parser.add_argument(
        "--city_seeds_amount",
        type=int,
        default=8,
        help="City seeds.",
    )
    parser.add_argument(
        "--city_growth_rate",
        type=int,
        default=3,
        help="City growth rate.",
    )
    parser.add_argument(
        "--river_seeds_amount",
        type=int,
        default=5,
        help="River seeds.",
    )
    parser.add_argument(
        "--river_length",
        type=int,
        default=30,
        help="River length.",
    )

    parser.set_defaults(randomize_parameters=False)
    args = parser.parse_args()
    return args


def parameters_to_world_settings(world_settings, args):
    world_settings.size = (args.world_height, args.world_width)
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
    print("Welcome to hic sunt random!")

    args = parse_user_arguments()
    generate_worlds(args)

    print("Hic sunt random work finshed! Enjoy.")


def randomize_world_settings(world_settings):
    world_height = randint(10, 100)
    world_width = randint(10, 100)
    world_settings.size = (world_height, world_width)
    world_settings.mountain_settings.seeds_amount = randint(0, 20)
    world_settings.mountain_settings.growth_rate = randint(0, 20)
    world_settings.land_settings.seeds_amount = randint(0, 20)
    world_settings.land_settings.growth_rate = randint(0, 20)
    world_settings.forest_settings.seeds_amount = randint(0, 10)
    world_settings.forest_settings.growth_rate = randint(0, 5)
    world_settings.city_settings.seeds_amount = randint(0, 15)
    world_settings.city_settings.growth_rate = randint(0, 3)
    world_settings.river_settings.river_seeds_count = randint(0, 10)
    world_settings.river_settings.river_length = randint(0, 50)


def generate_worlds(args):
    if args.worlds_amount < 0 and args.worlds_amount > 200:
        print("Error: Wrong number of worlds to generate!")
        return

    for _ in range(args.worlds_amount):
        world_settings = WorldSettings()

        if args.randomize_parameters:
            randomize_world_settings(world_settings)
        else:
            parameters_to_world_settings(world_settings, args)

        print("Starting to generate world..")
        world = world_generator.generate_world(world_settings)

        print("Starting to render world..")
        world_renderer.render_world(world)


if __name__ == "__main__":
    main()
