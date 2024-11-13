'''
image operations ,
that i am too lazy to write!
'''
import cv2
import numpy as np


def bgr2_3grey(image: np.ndarray):
    '''
    converts a 3 channel rgb image to one that is grayscale but with 3 channels 
    '''
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_bgr = cv2.merge([gray_image, gray_image, gray_image])
    return gray_bgr

def pad_image(input_image: np.ndarray, pad_size: int = 160):
    '''
    pads image with zeroes to a desginated size
    '''
    h, w ,c = input_image.shape
    pad_width = max(0, pad_size - w)
    pad_height = max(0, pad_size - h)
    top = pad_height // 2
    bottom = pad_height - top
    left = pad_width // 2
    right = pad_width - left
    _pad = np.pad(input_image, ((top, bottom), (left, right), (0, 0)), mode='constant', constant_values=0)
    return _pad
