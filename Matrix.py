
import random
import os

class Matrix(object):
  
   
   
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.score = 0 
        self.matrix = self.generateMatrix()

    
    def generateMatrix(self):
        tmp = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D']
        random.shuffle(tmp)
        idx = 0
        matrix = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(tmp[idx])
                idx += 1
            matrix.append(row)

        return matrix

    
    def printMatrix(self,pos1 =(-1,-1),pos2 =(-1,-1),color = 0):

        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

        for i in range(self.height):
            for j in range(self.width):
                if (i,j) == pos1 or (i,j) == pos2:
                    if color == 0:
                        print('\033[42m{}'.format(self.matrix[i][j]), end='')
                    else:
                        print('\033[41m{}'.format(self.matrix[i][j]), end='')
                    print('\033[0m', end='')
                else:
                    print('{}'.format(self.matrix[i][j]), end='')

            print('\r\n', end='')
        print('\r\nscore: {}\r\n'.format(self.score))

    def checkValid(self,pos1,pos2):

        if pos1 == (-1,-1) or pos2 == (-1,-1):
            return False

        i_1,j_1 = pos1
        i_2,j_2 = pos2

        if self.matrix[i_1][j_1] != self.matrix[i_2][j_2]:
            return False
        else:
            if(self.matrix[i_1][j_1] == ' '):
                return False
            else:
                return True

    def setNone(self,pos1,pos2):

        i_1,j_1 = pos1
        i_2,j_2 = pos2

        self.matrix[i_1][j_1] = ' '
        self.matrix[i_2][j_2] = ' '

    def checkNone(self):

        for i in range(self.width):
            for j in range(self.height):
                if self.matrix[i][j] != " ":
                    return False
        return True

