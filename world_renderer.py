import numpy as np
import cv2

def render_world(world):
    print("Rendering world:", world.name)
    #for x in range(world.size[0]):
       # for y in range(world.size[1]):
           # print('b')
    img1 = cv2.imread('ocean.png',cv2.IMREAD_COLOR)
    img2 = cv2.imread('mountain.png',cv2.IMREAD_COLOR)
    img3 = cv2.imread('field.png',cv2.IMREAD_COLOR)
            
    vis = np.concatenate((img1, img2, img3), axis=1)
    cv2.imwrite('out.png', vis)
    cv2.imshow('out.png', vis)
            

    k = cv2.waitKey()
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        print('bla')
        cv2.imwrite('out.png', vis)
        
        cv2.destroyAllWindows()

