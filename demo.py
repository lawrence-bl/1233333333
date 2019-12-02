import os, sys
import time
from Matrix import Matrix

if os.name == 'posix':
    import sys, tty, termios
else:
    import msvcrt

def getCoordinate(key,Dict):

    return Dict[key]


def getch():
    if os.name == 'posix':
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    else:
        return msvcrt.getch()

if __name__ == '__main__':
    # """python lixiang/demo.py"""

    
    posDict = {'a': (0,0), 'b': (0,1), 'c': (0,2), 'd': (0,3),
               'e': (1,0), 'f': (1,1), 'g': (1,2), 'h': (1,3),
               'i': (2,0), 'j': (2,1), 'k': (2,2), 'l': (2,3),
               'm': (3,0), 'n': (3,1), 'o': (3,2), 'p': (3,3),
               'q': 'over'}

  
    matrix = Matrix(4,4)

   
    pos1 = (-1,-1)
    pos2 = (-1,-1)
    inputPosition = (-1,-1)

    totalTime = 60 
    startTime = time.time()

    while(True):
        if(matrix.checkNone()):
            break
        if(time.time()- startTime) > totalTime:
            break
        matrix.printMatrix(pos1=pos1,pos2=pos2,color=0)

        if(matrix.checkValid(pos1=pos1,pos2=pos2)):
            # print("score +2")
            matrix.score += 2
            matrix.printMatrix(pos1=pos1, pos2=pos2, color=1)
            time.sleep(0.5)
            matrix.setNone(pos1,pos2)
            if (matrix.checkNone()):
                break
            pos1 = (-1, -1)
            pos2 = (-1, -1)
            matrix.printMatrix(pos1=pos1,pos2=pos2, color=0)

        inputKey = getch()
        if(inputKey == "q"):
            break
        if(not inputKey in posDict):
            print("Error")
            break
        inputPosition = getCoordinate(inputKey,posDict)

        if pos1 == (-1,-1) and pos2 == (-1,-1):
            pos1 = inputPosition
        elif pos1 != (-1,-1) and pos2 == (-1,-1):
            pos2 = inputPosition
            if pos1 == pos2:
                pos1 = (-1,-1)
                pos2 = (-1,-1)
        else:
            pos1 = inputPosition
            pos2 = (-1,-1)

    print("Game over! Score: ",matrix.score)
    sys.exit(0)



