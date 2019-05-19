
upper_code = ''
lower_code = ''
currentBlock = True

f = open('code.slice','r')

p = f.read().splitlines()

for i in p:
    if i == '[upper]':
        currentBlock = True
        continue
    if i == '[end]':
        continue
    if i == '[lower]':
        currentBlock = False
        continue
    if i == '[endFile]':
        break


    if (currentBlock):
        upper_code += i + '\n'
    if(not currentBlock):
        lower_code += i + '\n'


def setSize(size):
    global lower_code
    size = str(size[0]) + ',' + str(size[1])
    lower_code = lower_code.replace('[size]',size)



def getCode(data):
    return '                ' \
           'graphics.drawLine('+str(data[0]) + ','+\
                                str(data[1]) + ','+\
                                str(data[2]) + ','+\
                                str(data[3]) + ');'


if (__name__ == "__main__"):
    print('load function successfully!')
