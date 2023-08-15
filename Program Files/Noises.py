#   Different Noise Types
import os
import random
import cv2 as cv
import skimage
from skimage.io import imsave
import numpy as np

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
    
def add_salt_pepper():
    img = cv.imread(set_img_path.org_path)
    path_splitter(set_img_path.org_path)
    noised = np.zeros(img.shape, np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            r = random.random()
            if r < 0.2/2:
                noised[i][j] = [0, 0, 0]
            elif r < 0.2:
                noised[i][j] = [255, 255, 255]
            else:
                noised[i][j] = img[i][j]
    noised_img_path = path_splitter.path + '/Modified/SP_noisy_' + path_splitter.org_img_name
    cv.imwrite(noised_img_path,noised)
    
    cv.imshow("Salt and Pepper",noised)
    
def add_gaussien():
    path_splitter(set_img_path.org_path)
    org_g_noisy =  skimage.util.random_noise(set_img_path.org_img , mode='gaussian', var=0.01)  
    gaus_img_path = path_splitter.path + '/Modified/Gaus_noisy_' + path_splitter.org_img_name
    imsave(gaus_img_path, org_g_noisy, check_contrast=None)
    
    cv.imshow('Gaussian Noise',org_g_noisy)

def add_poisson():
    path_splitter(set_img_path.org_path)
    gray_img = cv.imread(set_img_path.org_path,cv.IMREAD_GRAYSCALE)
    gray_p_noisy = skimage.util.random_noise(gray_img, mode='poisson')
    poisson_img_path = path_splitter.path + '/Modified/Poisson_noisy_' + path_splitter.org_img_name
    imsave(poisson_img_path, gray_p_noisy)
    
    cv.imshow('Poisson Noise',gray_p_noisy)
