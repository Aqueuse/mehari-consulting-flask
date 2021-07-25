import os


def list_img_in_folder(path, index):
    img_list = []
    limit = 6
    for element in os.listdir(path):
        if element.endswith('.jpg'):
            img_list.append(element)
    img_list.sort()
    return img_list[int(index):int(index)+limit]


def list_all_img_in_folder(path):
    img_list = []
    for element in os.listdir(path):
        if element.endswith('.jpg'):
            img_list.append(element)
    return img_list


def get_img_count(path):
    img_list = []
    for element in os.listdir(path):
        if element.endswith('.jpg'):
            img_list.append(element)
    return len(img_list)


def month_exist(month):
    files_list = os.listdir('logs/')
    for element in files_list:
        if month == element[0:2]:
            return True
    return False
