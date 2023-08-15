import cv2 as cv
import numpy as np
import os
from skimage.morphology import erosion, dilation, opening, closing
from skimage.morphology import disk, diamond, octagon, rectangle, square, cube

def set_img_path(img_path):
    set_img_path.org_path = img_path
    set_img_path.org_img = cv.imread(img_path)
    set_img_path.gray_img = cv.cvtColor(set_img_path.org_img, cv.COLOR_BGR2GRAY)
    try:
        os.mkdir('/'.join(img_path.split('/')[:-1])+'/Modified/')
    except FileExistsError:
        pass

def path_splitter(org_Path):
    path_splitter.path = '/'.join(org_Path.split('/')[:-1])   
    path_splitter.org_img_name =  org_Path.split('/')[-1]

def get_kernal(kernal_value):
    if kernal_value == "Disk":
        get_kernal.kernal = disk(6)
    elif kernal_value == "Diamond":
        get_kernal.kernal = diamond(6)
    elif kernal_value == "Octagon":
        get_kernal.kernal = octagon(6,6)
    elif kernal_value == "Rectangle":
        get_kernal.kernal = rectangle(6,6)
    elif kernal_value == "Square":
        get_kernal.kernal = square(6)    
    get_kernal.re_kernal = kernal_value

def mrph_dilation(kernal):
    path_splitter(set_img_path.org_path)
    kernal_value = kernal
    get_kernal(kernal_value)
    dilat = dilation(set_img_path.gray_img, get_kernal.kernal)
    new_path = path_splitter.path + f'/Modified/dilated_{kernal_value}_' + path_splitter.org_img_name
    cv.imwrite(new_path,dilat)
    
    cv.imshow(f'{get_kernal.re_kernal} Dilation', dilat)
    
def mrph_erosion(kernal):
    path_splitter(set_img_path.org_path)    
    kernal_value = kernal
    get_kernal(kernal_value)
    erod = erosion(set_img_path.gray_img, get_kernal.kernal)
    new_path = path_splitter.path + f'/Modified/eroded_{kernal_value}_' + path_splitter.org_img_name
    cv.imwrite(new_path,erod)
    
    cv.imshow(f'{get_kernal.re_kernal} Erosion', erod)
    
def mrph_open(kernal):
    path_splitter(set_img_path.org_path)
    kernal_value = kernal
    get_kernal(kernal_value)
    get_kernal(kernal)
    openm = opening(set_img_path.gray_img, get_kernal.kernal)
    new_path = path_splitter.path + f'/Modified/opened_{kernal_value}_' + path_splitter.org_img_name
    cv.imwrite(new_path,openm)

    cv.imshow(f'{get_kernal.re_kernal} Opening', openm)
    
def mrph_close(kernal):
    path_splitter(set_img_path.org_path)
    kernal_value = kernal
    get_kernal(kernal_value)
    get_kernal(kernal)    
    close = closing(set_img_path.gray_img, get_kernal.kernal)
    new_path = path_splitter.path + f'/Modified/closed_{kernal_value}_' + path_splitter.org_img_name
    cv.imwrite(new_path,close)
    
    cv.imshow(f'{get_kernal.re_kernal} Closing', close)

