#   Edge Detection Filters
'''
- Laplacian --
- Gaussian --
- Sobel --
- Prewitt --
- LOG --
- Canny --
- Zero Cross ?
- Thicken  ?
- Skeleton --
- Thining ?
'''


import cv2 as cv
import os
import numpy as np 
from  skimage.morphology import skeletonize
from skimage.io import imsave, imshow
from skimage import data
from skimage.util import invert
import matplotlib.pyplot as plt


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
    
def laplacian():
    path_splitter(set_img_path.org_path)
    gray_img = cv.imread(set_img_path.org_path, 0)
    laplac_img = cv.Laplacian(gray_img, cv.CV_64F)
    laplac_img  = np.uint8(np.absolute(laplac_img ))
    new_path = path_splitter.path + '/Modified/laplacian_' + path_splitter.org_img_name
    cv.imwrite(new_path,laplac_img)

    cv.imshow('Laplacian Filter', laplac_img )
    
def gaussian():
    path_splitter(set_img_path.org_path)
    blured_img = cv.GaussianBlur(set_img_path.org_img,(5,5),cv.BORDER_DEFAULT)
    new_path = path_splitter.path + '/Modified/gauss_blured_' + path_splitter.org_img_name
    cv.imwrite(new_path,blured_img)

    cv.imshow("Gaussian Filter",blured_img)

def sobel(filter_value):
    path_splitter(set_img_path.org_path)
    gaussian_img = cv.GaussianBlur(set_img_path.gray_img,(3,3),0)
    if filter_value == 2:
        sobel_x = cv.Sobel(gaussian_img,cv.CV_8U,1,0,ksize=5)
        new_path = path_splitter.path + '/Modified/hori_sobel_' + path_splitter.org_img_name
        cv.imwrite(new_path,sobel_x)

        cv.imshow('Horizontal  Sobel', sobel_x)
    elif filter_value == 3:
        sobel_y = cv.Sobel(gaussian_img,cv.CV_8U,0,1,ksize=5)
        new_path = path_splitter.path + '/Modified/verti_sobel_' + path_splitter.org_img_name
        cv.imwrite(new_path,sobel_y)

        cv.imshow('Vertical  Sobel', sobel_y)

def prewitt(filter_value):
    path_splitter(set_img_path.org_path)
    gaussian_img = cv.GaussianBlur(set_img_path.gray_img,(3,3),0)
    if filter_value == 4:
        kernel_x = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
        prewitt_x = cv.filter2D(gaussian_img, -1, kernel_x)
        new_path = path_splitter.path + '/Modified/hori_prewitt_' + path_splitter.org_img_name
        cv.imwrite(new_path,prewitt_x)

        cv.imshow('Horizontal Prewitt',prewitt_x)
    elif filter_value == 5:
        kernel_y = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        prewitt_y = cv.filter2D(gaussian_img, -1, kernel_y)
        new_path = path_splitter.path + '/Modified/verti_prewitt_' + path_splitter.org_img_name
        cv.imwrite(new_path,prewitt_y)

        cv.imshow('Vertical Prewitt ',prewitt_y)
        
def LOG():
    path_splitter(set_img_path.org_path)
    blur = cv.GaussianBlur(set_img_path.org_img,(3,3),0)
    laplacian = cv.Laplacian(blur,cv.CV_64F)
    lap_o_g = laplacian/laplacian.max()
    new_path = path_splitter.path + '/Modified/LOG_' + path_splitter.org_img_name
    imsave(new_path,lap_o_g, check_contrast=False)
#    cv.imwrite(new_path,lap_o_g)

    cv.imshow('LOG',lap_o_g)
    
def canny():
    path_splitter(set_img_path.org_path)
    canny_img = cv.Canny(set_img_path.gray_img,100,200)
    new_path = path_splitter.path + '/Modified/canny_' + path_splitter.org_img_name
    cv.imwrite(new_path,canny_img)
    cv.imshow('Canny Filter',canny_img)

# def zero_cross():
#    path_splitter(set_img_path.org_path)
#     zero_cross_img = None
#     new_path = path_splitter.path + '/Modified/zero_cross_' + path_splitter.org_img_name
#     cv.imwrite(new_path,zero_cross_img)
#     cv.imshow("Thicken",zero_cross_img)


# def thicken():
#    path_splitter(set_img_path.org_path)
#     thicken_img = None
#     new_path = path_splitter.path + '/Modified/thicken_' + path_splitter.org_img_name
#     cv.imwrite(new_path,thicken_img)
#     cv.imshow("Thicken",thicken_img)
#     pass

# def skeleton():
#     path_splitter(set_img_path.org_path)
#     image = invert(set_img_path.gray_img)
#     skeleton_img = skeletonize(image)
#     new_path = path_splitter.path + '/Modified/skeleton_' + path_splitter.org_img_name
#     cv.imwrite(new_path,skeleton_img)
    
#     cv.imshow("Skeleton",skeleton_img)
    
#     fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
#                          sharex=True, sharey=True)
#     ax = axes.ravel()

#     ax[0].imshow(image, cmap=plt.cm.gray)
#     ax[0].axis('off')
#     ax[0].set_title('original', fontsize=20)

#     ax[1].imshow(skeleton_img, cmap=plt.cm.gray)
#     ax[1].axis('off')
#     ax[1].set_title('skeleton', fontsize=20)

#     fig.tight_layout()
#     plt.show()
    
    
# def thining():
#     path_splitter(set_img_path.org_path)
#     thining_img = None
#     new_path = path_splitter.path + '/Modified/thining_' + path_splitter.org_img_name
#     cv.imwrite(new_path,thining_img)
#     cv.imshow("Thining",thining_img)
#     pass