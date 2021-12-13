import cv2
import numpy as np
import torch

img = cv2.imread('./demo/03.jpg')
mask = img<=225
mask = img*mask
cv2.imwrite('03_mask.png',mask)