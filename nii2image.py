# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 13:06:40 2022

@author: PRANJ
"""
import scipy, numpy, shutil, os, nibabel
import sys, getopt
import numpy as np
import os    # Traverse folders 
import nibabel as nib #nii Format 1 This bag will be used in general 
import imageio   # Convert to an image
def nii_to_image(niifile):
 filenames = os.listdir(filepath) # Read nii Folder 
 slice_trans = []
 
 for f in filenames:
  # Start reading nii Documents 
  img_path = os.path.join(filepath, f)
  img = nib.load(img_path)    # Read nii
  print(img.shape)
  img_fdata = img.get_fdata()
  fname = f.replace('.nii.gz','')   # Remove nii Suffix name of 
  img_f_path = os.path.join(imgfile, fname)
  # Create nii The folder of the corresponding image 
  if not os.path.exists(img_f_path):
   os.mkdir(img_f_path)    # New Folder 
 
  # Start converting to an image 
  nx, ny, nz, nw = img_fdata.shape
  total_volumes = img_fdata.shape[3]
  total_slices = img_fdata.shape[2]  
  # iterate through volumes
  for current_volume in range(0, total_volumes):
      slice_counter = 0
      # iterate through slices
      for current_slice in range(0, total_slices):
          if (slice_counter % 1) == 0:
              data = img_fdata[:, :, current_slice, current_volume]
              #alternate slices and save as png
              print('Saving image...')
              image_name = imgfile[:-4] + "_t" + "{:0>3}".format(str(current_volume+1)) + "_z" + "{:0>3}".format(str(current_slice+1))+ ".png"
              imageio.imwrite(image_name, data)
              print('Saved.')

              #move images to folder
              print('Moving files...')
              src = image_name
              shutil.move(src, img_f_path)
              slice_counter += 1
              print('Moved.')
  '''
    for i in range(z):      #z Is a sequence of images 
   silce = img_fdata[i, :, :]   # You can choose which direction of slice 
   imageio.imwrite(os.path.join(img_f_path,'{}.png'.format(i)), silce)
            # Save an image''' 
 
if __name__ == '__main__':
 filepath = 'C:/Users/PRANJ/ML_fmri_ABIDE/NYU_fMRI/'
 imgfile = 'C:/Users/PRANJ/ML_fmri_ABIDE/NYU_jpg/'
 #filenames=os.listdir(filepath)
 nii_to_image(filepath)
 
