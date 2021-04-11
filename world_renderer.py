import numpy as np
import cv2
import world_entities
import copy

def render_world(world):
    print("Rendering world:", world.name)

    world_picture = cv2.imread('./resources/tiles/world_begins.png', cv2.IMREAD_COLOR)
    
    img1 = cv2.imread('./resources/tiles/ocean.png', cv2.IMREAD_COLOR)
    img2 = cv2.imread('./resources/tiles/mountain.png', cv2.IMREAD_COLOR)
    img3 = cv2.imread('./resources/tiles/field.png', cv2.IMREAD_COLOR)
    img4 = cv2.imread('./resources/tiles/space.png', cv2.IMREAD_COLOR)
    
    world_map = []
    for world_objects_row in world.world_objects:
        for world_object in world_objects_row:
            if isinstance(world_object, world_entities.Mountain):
                world_picture = np.concatenate((world_picture, img2), axis=1)
            elif isinstance(world_object, world_entities.Field):
                world_picture = np.concatenate((world_picture, img3), axis=1)
            elif isinstance(world_object, world_entities.Ocean):
                world_picture = np.concatenate((world_picture, img1), axis=1)
            else:
                world_picture = np.concatenate((world_picture, img4), axis=1)

        world_picture_row = copy.deepcopy(world_picture)
        world_map.append(world_picture_row)
        world_picture = cv2.imread('./resources/tiles/world_begins.png', cv2.IMREAD_COLOR)
    
    final_world_map = world_map[0]
    
    for picture_row in world_map[1:]:
        final_world_map = np.concatenate((final_world_map, picture_row), axis=0)

    cv2.imwrite('./output/out.png', final_world_map)
    # cv2.imshow('./output/out.png', final_world_map)

    # k = cv2.waitKey()
    # if k == 27:         # wait for ESC key to exit
    #     cv2.destroyAllWindows()
    # elif k == ord('s'):  # wait for 's' key to save and exit
    #     cv2.imwrite('out.png', final_world_map)
    #     cv2.destroyAllWindows()
