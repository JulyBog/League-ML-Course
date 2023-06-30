import os
import cv2
import math

from image_search import image_search

current_dir = os.getcwd()
img_dir = os.path.join(current_dir, "test_data_chess")
image_paths = image_search(img_dir, [".jpg", ".png"])

for image_path in image_paths:
    img = cv2.imread(image_path)

    h, w, c = img.shape
    image_name = os.path.basename(image_path)

    h_cell = h / 10
    w_cell = w / 10
    h_cell = math.ceil(h_cell)
    w_cell = math.ceil(w_cell)

    for i in range(5):
        for j in range(5):
            start_w = w_cell * i * 2
            start_h = h_cell * j * 2
            img[
                start_h:start_h + h_cell,
                start_w:start_w + w_cell
            ] *= 0

    for i in range(5):
        for j in range(5):
            start_w = w_cell + w_cell * i * 2
            start_h = h_cell + h_cell * j * 2
            img[
                start_h:start_h + h_cell,
                start_w:start_w + w_cell
            ] *= 0

    # Ya ebal QT
    cv2.imwrite(os.path.join(os.getcwd(), "out_img", image_name), img)
    # cv2.imshow(image_name, img)
    # cv2.waitKey(-1)
