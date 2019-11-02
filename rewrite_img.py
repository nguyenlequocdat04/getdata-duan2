import cv2
import os

img_path = 'test'
all_file = os.listdir(img_path)
os.chdir(img_path) # very important
for filename in all_file:
# print(filename)
    img=cv2.imread(filename)
    cv2.imwrite(filename,img,[int(cv2.IMWRITE_JPEG_QUALITY), 100])