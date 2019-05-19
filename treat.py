from matplotlib import pyplot as plt
import numpy as np
import cv2
from scipy import stats
import translate
from skimage import transform

imgData = cv2.imread('van.jpg',0)

imgData = np.array(imgData)

shape = imgData.shape


def twoWayTreat():
    global imgData
    imgData = stats.zscore(imgData)

    for raw in range(shape[0]):
        for col in range(shape[1]):
            if imgData[raw][col] < 0:
                imgData[raw][col] = 0
            else:
                imgData[raw][col] = 255


def debugImg():
    global imgData
    plt.imshow(imgData)
    plt.show()


def getCode():
    code = ''
    for this_line_index in range(len(imgData)-1):
        lineLib = []
        this_line = imgData[this_line_index]
        newTurn = False
        for this_line_data_index in range(len(this_line)-1):
            if this_line[this_line_data_index] == 255:
                begin_draw = this_line_data_index
                newTurn = True

            if this_line[this_line_data_index] == 0 and newTurn:
                end_draw = this_line_data_index
                lineLib.append([begin_draw,end_draw])
                newTurn = False

        for i in lineLib:
            code = code + translate.getCode([i[0],this_line_index,i[1],this_line_index]) + '\n'

    return code

def compressImg():
    global imgData
    imgData = transform.rescale(imgData, [0.2,0.2])



twoWayTreat()

compressImg()

debugImg()

p = getCode()

translate.setSize(imgData.shape)

with open('draw.java','w') as f:
    f.write(translate.upper_code)
    f.write(p)
    f.write(translate.lower_code)

f.close()
