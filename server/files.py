import os


# List all files in a directory using os.listdir (sorted by filename)
def list_img_in_folder(path):
    img_list = []
    for element in os.listdir(path):
        if element.endswith('.jpg'):
            img_list.append(element)
    img_list.sort()
    return img_list
