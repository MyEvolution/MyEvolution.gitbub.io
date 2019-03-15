import math
import numpy as np
from PIL import Image

img=np.zeros((600,800))
img = img + 255
rows,cols=img.shape

floor = math.floor

k = float(input("k>0:"))
x_0 = y_0 = 50
if k>1:
    y = [i for i in range(51,rows-50)]
    x = []
    delta = 1.0/k
    for i in y:        
        x_1 = x_0+delta
        x.append(floor(x_1))
        x_0 = x_1
        if x_1 >= cols-50:
            break
            
if k<=1:
    x = [i for i in range(51,cols-50)]
    y = []
    delta = k
    for i in x:
        y_1 = y_0+delta
        y.append(floor(y_1))
        y_0 = y_1
        if y_1 >= rows-50:
            break

for i in range(min(len(x),len(y))):
    img[rows - y[i],x[i]] = 0
im = Image.fromarray(img)
im.show()

