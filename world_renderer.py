import copy
import os.path
import random
from os import listdir

import cv2
import numpy as np

import world_entities

TILES_PATH = "./resources/tiles/"
TILES_FORMAT = ".png"


class TilesInfo:
    def __init__(self):
        self.tile_img_count = {}

    def init_info(self):
        self.tile_img_count.clear()

        tile_files = [
            file
            for file in listdir(TILES_PATH)
            if os.path.isfile(os.path.join(TILES_PATH, file))
        ]

        for tile_file in tile_files:
            if "_" not in tile_file:
                continue

            tile_type = tile_file.split("_")[0]
            if tile_type not in self.tile_img_count:
                self.tile_img_count[tile_type] = 1
            else:
                self.tile_img_count[tile_type] += 1


def get_world_object_img(world_object, tiles_info):
    tile_name = type(world_object).name
    if tile_name not in tiles_info.tile_img_count:
        tile_name = "placeholder"

    tile_img_index = random.randint(0, tiles_info.tile_img_count[tile_name] - 1)

    return cv2.imread(
        TILES_PATH + tile_name + "_" + str(tile_img_index) + TILES_FORMAT,
        cv2.IMREAD_COLOR,
    )


def render_world(world):
    print("Rendering world:", world.name)

    tiles_info = TilesInfo()
    tiles_info.init_info()

    world_picture_temp = []
    for row_index, world_objects_row in enumerate(world.world_objects):
        world_picture_row = get_world_object_img(
            world.world_objects[row_index][0], tiles_info
        )

        for world_object in world_objects_row[1:]:
            world_picture_row = np.concatenate(
                (world_picture_row, get_world_object_img(world_object, tiles_info)),
                axis=1,
            )

        world_picture_temp.append(copy.deepcopy(world_picture_row))

    world_picture = world_picture_temp[0]
    for world_picture_row in world_picture_temp[1:]:
        world_picture = np.concatenate((world_picture, world_picture_row), axis=0)

    folder_path = "./output/"
    file_name = "output_"
    file_format = ".png"

    i = 0
    file_path = folder_path + file_name + str(i) + file_format
    while os.path.exists(file_path):
        i += 1
        file_path = folder_path + file_name + str(i) + file_format

    cv2.imwrite(file_path, world_picture)
