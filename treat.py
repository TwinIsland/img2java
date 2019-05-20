from matplotlib import pyplot as plt
import numpy as np
import cv2
from scipy import stats
import translate
from skimage import transform

#####################################
imgData = cv2.imread('van.jpg',0)
compressRate = 0.4
#####################################

imgData = np.array(imgData)
shape = imgData.shape
pas = p = 'unknown'

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
    global imgData,compressRate
    imgData = transform.rescale(imgData, [compressRate,compressRate])


def passivate():
    count = 0
    global imgData
    shape = imgData.shape
    lineLenght = shape[1]
    for lineIndex in range(shape[0]-1):
        for numberIndex in range(0,lineLenght-6):
            thisFive = list(imgData[lineIndex,numberIndex:numberIndex+5])
            if thisFive == [0,255,255,255,255]:
                count += 1
                thisFive[0] =255
                imgData[lineIndex,numberIndex:numberIndex+5] = thisFive
    return 'passivate rate: ' + str(count/(shape[0]*shape[1])) + '%'


twoWayTreat()
compressImg()
pas = passivate()
debugImg()
p = getCode()
translate.setSize(imgData.shape)

with open('draw.java','w') as f:
    f.write(translate.upper_code)
    f.write(p)
    f.write(translate.lower_code)

try:
    print('==================')
    print('compressRate: ' + str(compressRate))
    print('passivateRate: ' + str(pas))
    print('size: ' + str(imgData.shape))
    print('==================')
except Exception:
    print('cannot print out the post-info!')

f.close()

