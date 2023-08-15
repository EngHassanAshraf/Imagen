# Convert between RGB system and Gray system

import cv2 as cv
import os

def set_img_path(img_path):
    set_img_path.org_path = img_path
    set_img_path.org_img = cv.imread(img_path)
    try:
        os.mkdir('/'.join(img_path.split('/')[:-1])+'/Modified/')
    except FileExistsError:
        pass

def path_splitter(org_Path):
    path_splitter.path = '/'.join(org_Path.split('/')[:-1])   
    path_splitter.org_img_name =  org_Path.split('/')[-1]
    
def org_im():
    cv.imshow('Original Image', cv.imread(set_img_path.org_path))


def convert_2_gry():
    path_splitter(set_img_path.org_path )
    gry_img = cv.cvtColor(cv.imread(set_img_path.org_path), cv.COLOR_BGR2GRAY)
    new_path = path_splitter.path + '/Modified/gray_' + path_splitter.org_img_name
    cv.imwrite(new_path,gry_img)
    cv.imshow('Gray Image', gry_img)

def container_folder_path():
    path_splitter(set_img_path.org_path)
    new_path = path_splitter.path + '/Modified'
    return new_path
