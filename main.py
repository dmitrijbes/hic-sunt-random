import world_generator as world_generator
import world_renderer as world_renderer

def main():
    print("Welcome to hic sunt random!")

    print("Starting to generate world..")
    world = world_generator.generate_world()

    print("Starting to render world..")
    world_renderer.render_world(world)

    print("Hic sunt random work finished! Enjoy.")

if __name__ == '__main__':
    main()
