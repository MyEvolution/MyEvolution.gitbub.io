# python histogram equalization and specification
import math
import numpy as np
from PIL import Image
from pylab import *

def equalization(im):
    obj = im.flatten()
    sta = [0 for i in range(256)]
    for i in obj:
        sta[i] = sta[i]+1
    sta = [i /len(obj) for i in sta ]

    updated = []
    integral=0.0
    for i in sta:
        integral += i
        updated.append(int(integral * 255))
    nim = np.array(im)
    for i in range(len(im)):
        for j in range(len(im[i])):
            nim[i][j] = updated[im[i][j]]
    return nim,updated

def specification(im,im_s):
    nim,updated1 = equalization(im)

    nim_s,updated2 = equalization(im_s)
    updated = [-1 for i in range(256)]
    for i in range(256):
        if updated[updated2[i]]==-1:
            updated[updated2[i]] = i
    for i in range(256):
        j=1
        while updated[i] == -1:
            updated[i] = updated[(i+j)%256]
            if updated[i] == -1:
                updated[i] = updated[((i-j)+256)%256]
            j+=1
    final = np.array(im)
    for i in range(len(im)):
        for j in range(len(im[i])):
            if updated[im[i][j]]!= -1:
                final[i][j] = updated[im[i][j]]
    return final



im = np.array(Image.open("./image_black.jpg").convert("L"))
nim = equalization(im)[0]
im_s = np.array(Image.open("./object1.jpg").convert("L"))
final = specification(im,im_s)

'''Image.fromarray(im).show()
Image.fromarray(nim).show()
Image.fromarray(im_s).show()'''
Image.fromarray(final).show()
figure()
#hist(im.flatten(),256)
#hist(nim.flatten(),256)
hist(im_s.flatten(),256)
hist(final.flatten(),256)
show()



