import cv2
import os
import numpy as np 
from tqdm import tqdm

src_dir = '/content/data/clear_images'
images = os.listdir(src_dir)
dst_dir = '/content/blur_images'

kernels=[((3,3),0.3),((7,7),1),((11,11),1.6)]
for i, img in tqdm(enumerate(images), total=len(images)):
    for el in os.listdir( '/content/data/clear_images/'+images[i]):
      img = cv2.imread(f"{src_dir}/{images[i]}/{el}")

      temp=np.random.randint(0,3)
      # print(img.shape, kernels[temp][0], kernels[temp][1],sep='==>')
      # add gaussian blurring
      # print(img.shape)
      # print(temp,kernels[temp][0])
      blur = cv2.GaussianBlur(img, kernels[temp][0], kernels[temp][1])
      cv2.imwrite(f"{dst_dir}/{images[i]}.png", blur)

print('DONE')