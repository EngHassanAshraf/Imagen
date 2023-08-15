# Global Transform Filters
from skimage.transform import hough_line, hough_line_peaks, hough_circle, hough_circle_peaks
import matplotlib.pyplot as plt
from matplotlib import cm

import cv2 as cv
import numpy as np
import os

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

def hough_lines():
    path_splitter(set_img_path.org_path)
    blured_img = cv.GaussianBlur(
        set_img_path.gray_img, (5, 5), cv.BORDER_DEFAULT)
    canny_img = cv.Canny(blured_img, 100, 200)
    tested_angles = np.linspace(-np.pi / 2, np.pi / 2, 360, endpoint=False)
    h, theta, d = hough_line(canny_img, theta=tested_angles)

    # Generating figure 1
    fig, axes = plt.subplots(1, 3, figsize=(15, 6))
    ax = axes.ravel()

    ax[0].imshow(set_img_path.gray_img, cmap=cm.gray)
    ax[0].set_title('Input image')
    ax[0].set_axis_off()

    angle_step = 0.5 * np.diff(theta).mean()
    d_step = 0.5 * np.diff(d).mean()
    bounds = [np.rad2deg(theta[0] - angle_step),
              np.rad2deg(theta[-1] + angle_step),
              d[-1] + d_step, d[0] - d_step]
    ax[1].imshow(np.log(1 + h), extent=bounds, cmap=cm.gray, aspect=1 / 1.5)
    ax[1].set_title('Hough transform')
    ax[1].set_xlabel('Angles (degrees)')
    ax[1].set_ylabel('Distance (pixels)')
    ax[1].axis('image')

    ax[2].imshow(set_img_path.gray_img, cmap=cm.gray)
    ax[2].set_ylim((set_img_path.gray_img.shape[0], 0))
    ax[2].set_axis_off()
    ax[2].set_title('Detected lines')

    for _, angle, dist in zip(*hough_line_peaks(h, theta, d)):
        (x0, y0) = dist * np.array([np.cos(angle), np.sin(angle)])
        ax[2].axline((x0, y0), slope=np.tan(angle + np.pi/2))

    plt.tight_layout()
    plt.show()
    new_path = path_splitter.path + '/Modified/lines_of_' + path_splitter.org_img_name 
    plt.savefig(new_path)

def hough_circles():
    path_splitter(set_img_path.org_path)
    img = set_img_path.org_img
    gray = set_img_path.gray_img
    gray_blurred = cv.blur(gray, (3, 3))
    new_path = path_splitter.path + '/Modified/circles_of_' + path_splitter.org_img_name 
    detected_circles = cv.HoughCircles(
        gray_blurred, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=1, maxRadius=40)
    if detected_circles is not None:
        detected_circles = np.uint16(np.around(detected_circles))
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            cv.circle(img, (a, b), r, (0, 255, 0), 2)
            cv.circle(img, (a, b), 1, (0, 0, 255), 3)
        cv.imshow("Detected Circles", img)
        cv.imwrite(new_path,img)