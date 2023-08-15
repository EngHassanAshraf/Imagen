#   Local Transform Filters
'''
Low pass  (gaussian )
High pass  ()
Median
Averaging
'''
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

def low_pass():
    path_splitter(set_img_path.org_path)
    gaussian = cv.GaussianBlur(set_img_path.org_img, (37, 37), 0)
    new_path = path_splitter.path + '/Modified/gaussian_blured_' + path_splitter.org_img_name
    cv.imwrite(new_path,gaussian)
    cv.imshow("Gaussian Low-Pass filter", gaussian)


def high_pass():
    path_splitter(set_img_path.org_path)
    edgesx = cv.Scharr(set_img_path.org_img, -1, dx=1, dy=0, scale=1,
                       delta=0, borderType=cv.BORDER_DEFAULT)
    
    edgesy = cv.Scharr(set_img_path.org_img, -1, dx=0, dy=1, scale=1,
                       delta=0, borderType=cv.BORDER_DEFAULT)
    
    new_path1 = path_splitter.path + '/Modified/hori_scharr_' + path_splitter.org_img_name
    new_path2 = path_splitter.path + '/Modified/verti_scharr_' + path_splitter.org_img_name
    
    cv.imwrite(new_path1,edgesx)    
    cv.imwrite(new_path2,edgesy)

    cv.imshow("H-Scharr High-Pass filter", edgesx)
    cv.imshow("V-Scharr High-Pass filter", edgesy)
    
def median():
    '''Its input need to has a Salt and Pepper noise
        to the median filter effect
        Median works efficiently with this noise and it used in smoothing images
    '''
    path_splitter(set_img_path.org_path)
    median_filtered = cv.medianBlur(set_img_path.org_img, 5)
    new_path = path_splitter.path + '/Modified/median_filtered_' + path_splitter.org_img_name
    cv.imwrite(new_path,median_filtered)
    cv.imshow('Medain Filtered Image', median_filtered)
    
def averaging():
    pass
    # averaging_filtered = None
    # new_path = path_splitter.path + '/Modified/averaging_filtered_' + path_splitter.org_img_name
    # cv.imwrite(new_path,averaging_filtered)
    # cv.imshow('Averaging Filtered Image', averaging_filtered)
    