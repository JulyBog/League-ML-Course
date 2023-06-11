print('Salam!')
# cd C:\Users\Asus\Projects\ml_course 
# python ml1_opencv.py

import os
import cv2

current_dir = os.getcwd()
image_paths=[]
for root, dirs, files in os.walk(current_dir):
 
    for file_name in files:
        if '.jpg' in file_name or '.png' in file_name:
            file_path = os.path.join(root, file_name)
            print(file_path)
            image_paths.append(file_path)

is_color_image = 0

for image_path in image_paths:
    img = cv2.imread(image_path, is_color_image)
    if is_color_image: 
        h, w, c = img.shape
    else: 
        h, w = img.shape
    image_name = os.path.basename(image_path)
    print(image_name, img.shape)
    # img[:,:,0] *= 0
    # img[:,:,1] *= 0
    img[
        0:100,
        200:350
    ] *= 0
    # cv2.imshow(image_name, img)
    # cv2.waitKey(-1)
    print(img)
    print(img.max())
    print(img.mean())
    print(type(img))

