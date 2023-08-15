#   Point Tranform Filters
import os
import cv2 as cv
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk, ImageEnhance
from matplotlib import pyplot as plt

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
    
def brightness_adj(brightness_factor):
    path_splitter(set_img_path.org_path)
    org_img = Image.open(set_img_path.org_path)
    enhancer = ImageEnhance.Brightness(org_img)
    enhanced_img = enhancer.enhance(brightness_factor)    
    enhanced_img.save(path_splitter.path + '/Modified/brightness_enhanced_' + path_splitter.org_img_name)
    brightness_enhanced_path = path_splitter.path + '/Modified/brightness_enhanced_' + path_splitter.org_img_name
    return brightness_enhanced_path

def contrast_adj(contrast_factor):
    path_splitter(set_img_path.org_path)
    org_img = Image.open(set_img_path.org_path)
    enhancer = ImageEnhance.Contrast(org_img)
    enhanced_img = enhancer.enhance(contrast_factor)
    enhanced_img.save(path_splitter.path + '/Modified/contrast_enhanced_' + path_splitter.org_img_name)
    contrast_enhanced_path = path_splitter.path + '/Modified/contrast_enhanced_' + path_splitter.org_img_name
    return contrast_enhanced_path

def Histogram():
    img = set_img_path.org_img
    path_splitter(set_img_path.org_path)
        
    plt.hist(img.ravel(), 256, [0,256])       
    plt.title('Image Histogram')
    hist_plot = path_splitter.path + '/Modified/hist_plot_' + path_splitter.org_img_name
    plt.savefig(hist_plot)
    plt.close()

    cv.imshow("Histogram Plot",cv.imread(hist_plot))

def histogram_equalization():
    path_splitter(set_img_path.org_path)
    equ = cv.equalizeHist(cv.imread(set_img_path.org_path, 0))
    new_path_NX = path_splitter.path +'/Modified/Hist_Equalized_' + path_splitter.org_img_name
    cv.imwrite(new_path_NX,equ)
    
    hist_img = cv.imread(new_path_NX)
    cv.imshow("Equalized Image", hist_img) 
    plt.hist(hist_img.ravel(), 256, [0,256])       
    plt.title('Equalized Image Histogram')
    equa_hist_plot = path_splitter.path + '/Modified/equa_hist_plot_' + path_splitter.org_img_name
    plt.savefig(equa_hist_plot)
    plt.close()
    
    cv.imshow("Equalized Histogram Plot",cv.imread(equa_hist_plot))

    
