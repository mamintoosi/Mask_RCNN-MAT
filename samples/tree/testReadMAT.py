# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:36:06 2019

@author: Mahmood
"""
#  save('imbw.mat', '-v7.3','bw');
import matplotlib.pyplot as plt
import numpy as np
#import h5py 
import os
import scipy.io as sio
#f = h5py.File('imbw.mat','r') 
#data = f.get('data/bw') 
#f.close()
#mdata = np.array(data)

masks_dir = 'D:/DTemp/DL/Mask_RCNN-master/datasets/tree/train/masks/'
#file_names = next(os.walk(masks_dir))[2]
file_names = ['1_1 (4).mat','1_1 (5).mat']
for mat_file in file_names:                
    mask_path = os.path.join(masks_dir, mat_file)
#    im_file_name = mat_file[:-4]
#    image_path = os.path.join(dataset_dir, im_file_name)
#    image = skimage.io.imread(image_path)
    data = sio.loadmat(mask_path)
    bws = data['bws']
    height, width = bws.shape[:2]
    nObj = 1
    if len(bws.shape) == 3:
        nObj = bws.shape[-1]
    mask = np.zeros([height,width, nObj],dtype=np.uint8)
    
    if len(bws.shape) == 2:
        mask[:, :, 0] = bws
        imgplot = plt.imshow(mask[:, :, i])
        plt.show()
    elif len(bws.shape) == 3:
        for i in range(nObj):
            mask[:, :, i] = bws[:,:,i]    
            imgplot = plt.imshow(mask[:, :, i])
            plt.show()
    else:
        print("Error in treeMAT")


#myMat = complex(rand(4), rand(4));
#save('myfile', 'myMat', '-v7')
#In Python, load the .mat file with scipy.io.loadmat. The result is a Python dict:
#
#>>> d = scipy.io.loadmat('myfile.mat')
#>>> m = d['myMat']
#>>> m[0,0]