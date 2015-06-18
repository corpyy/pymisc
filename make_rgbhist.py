#!~/usr/bin/env python
# -*- coding: utf-8 -*-

# 画像からGlayscaleヒストグラムとRGBヒストグラムを作るスクリプト

import cv2
import pylab as plt

def show_histogram(im):
    if im.ndim == 2:
        # glayscale
        plt.hist(im.lavel(), 256, range=(0, 255), fc='k')
        plt.show()

    elif im.ndim == 3:
        # color
        fig = plt.figure()
        fig.add_subplot(311)
        plt.hist(im[:,:,0].ravel(), 256, range=(0, 255), fc='b')
        plt.xlim(0,255)
        fig.add_subplot(312)
        plt.hist(im[:,:,1].ravel(), 256, range=(0, 255), fc='g')
        plt.xlim(0,255)
        fig.add_subplot(313)
        plt.hist(im[:,:,2].ravel(), 256, range=(0, 255), fc='r')
        plt.xlim(0,255)
        plt.show()

if __name__ == '__main__':
    im = cv2.imread("pass_to_image")
    if not (im == None):
        show_histogram(im)
