import numpy as np
import cv2

def render_world(world):
    print("Rendering world:", world.name)
    #for x in range(world.size[0]):
       # for y in range(world.size[1]):
           # print('b')
    img1 = cv2.imread('./resources/tiles/ocean.png',cv2.IMREAD_COLOR)
    img2 = cv2.imread('./resources/tiles/mountain.png',cv2.IMREAD_COLOR)
    img3 = cv2.imread('./resources/tiles/field.png',cv2.IMREAD_COLOR)
    img4 = cv2.imread('./resources/tiles/space.png',cv2.IMREAD_COLOR)

    for world_objects_row in self.world_objects:
            for world_object in world_objects_row:
                if isinstance(world_object, Mountain):
                    cv2.imshow('./resources/tiles/mountain.png', img2)
                elif isinstance(world_object, Field):
                    cv2.imshow('./resources/tiles/field.png', img3)
                elif isinstance(world_object, Ocean):
                    cv2.imshow('./resources/tiles/ocean.png', img1)
                else:
                    cv2.imshow('./resources/tiles/space.png', img4)
            

    # vis = np.concatenate((img1, img2, img3), axis=1)
    # cv2.imwrite('./output/out.png', vis)
    # cv2.imshow('./output/out.png', vis)
            

    k = cv2.waitKey()
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        print('bla')
        cv2.imwrite('out.png', vis)
        
        cv2.destroyAllWindows()

