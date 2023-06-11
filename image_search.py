import os
import cv2

def image_search(dir_path, ext):
    image_paths=[]
    path = dir_path
    file_ext = ext
    for root, dirs, files in os.walk(path): 
        for file_name in files:
            for extension in file_ext:
                if extension in file_name:
                    file_path = os.path.join(root, file_name)
                    print(file_path)
                    image_paths.append(file_path)
    return image_paths


if __name__ == "__main__":
    image_search(r"C:\Users\Asus\Desktop\test", ['.jpg', '.png'])
