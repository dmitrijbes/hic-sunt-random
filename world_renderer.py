import copy
import os.path

import numpy as np
import cv2

import world_entities


def get_world_object_img(world_object):
    if isinstance(world_object, world_entities.Mountain):
        return cv2.imread('./resources/tiles/mountain.png', cv2.IMREAD_COLOR)
    elif isinstance(world_object, world_entities.Field):
        return cv2.imread('./resources/tiles/field.png', cv2.IMREAD_COLOR)
    elif isinstance(world_object, world_entities.Ocean):
        return cv2.imread('./resources/tiles/ocean.png', cv2.IMREAD_COLOR)
    elif isinstance(world_object, world_entities.River):
        return cv2.imread('./resources/tiles/river.png', cv2.IMREAD_COLOR)
    else:
        return cv2.imread('./resources/tiles/placeholder.png', cv2.IMREAD_COLOR)


def render_world(world):
    print("Rendering world:", world.name)

    world_picture_temp = []
    for row_index, world_objects_row in enumerate(world.world_objects):
        world_picture_row = get_world_object_img(
            world.world_objects[row_index][0])

        for world_object in world_objects_row[1:]:
            world_picture_row = np.concatenate(
                (world_picture_row, get_world_object_img(world_object)), axis=1)

        world_picture_temp.append(copy.deepcopy(world_picture_row))

    world_picture = world_picture_temp[0]
    for world_picture_row in world_picture_temp[1:]:
        world_picture = np.concatenate(
            (world_picture, world_picture_row), axis=0)

    folder_path = "./output/"
    file_name = "output_"
    file_format = ".png"

    i = 0
    file_path = folder_path + file_name + str(i) + file_format
    while os.path.exists(file_path):
        i += 1
        file_path = folder_path + file_name + str(i) + file_format

    cv2.imwrite(file_path, world_picture)
