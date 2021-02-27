def render_world(world):
    print("Rendering world:", world.name)
    for x in range(world.size[0]):
        for y in range(world.size[1]):
            print("X", end="")
        print("\n", end="")
