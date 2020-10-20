def identity_matrix(n):
    output = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        output[i][i] = 1
    return output

class Matrix():
    def __init__(self, inputmatrixlist):
        if type(inputmatrixlist) != list:
            raise TypeError("input matrix must be a 2d list")
        for i in range(1,len(inputmatrixlist)):
            if len(inputmatrixlist[i]) != len(inputmatrixlist[i-1]):
                raise ValueError("all rows must be of the same lenght. all columns must be of the same lenght")
        self.matrix = inputmatrixlist

    def __str__(self):
        return str(self.matrix)
    
        #inputmatrix : Matrix object
    def __add__(self, inputmatrix):
        self.check_same_size(inputmatrix)
        output = [[0 for _ in range(len(self.matrix[0]))]for _ in range(len(self.matrix))]
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                output[x][y] = self.matrix[x][y] + inputmatrix.matrix[x][y]
        return output

    def __neg__(self):
        return (self*-1) 
        
        #inputmatrix : Matrix object
    def __sub__(self, inputmatrix):
        return self + Matrix(-inputmatrix)

    
        #input matrix must be an int or a list
    def __mul__(self, inputmatrix):
            # Multiplication by a constant
        if type(inputmatrix) == int or type(inputmatrix) == float:                                           
            output = [[0 for _ in range(len(self.matrix[0]))]for _ in range(len(self.matrix))]
            for x in range(len(self.matrix)):
                for y in range(len(self.matrix[0])):
                    output[x][y] = self.matrix[x][y] * inputmatrix
            return(output)
            
            #Multiplication by another matrix
        elif isinstance(inputmatrix, Matrix):                                                                
            output = [[0 for _ in range(len(inputmatrix.matrix))]for _ in range(len(self.matrix[0]))]
            for outputrow in range(len(self.matrix)):
                for outputcolumn in range(len(self.matrix[0])):
                    position = 0
                    for i in range(len(inputmatrix.matrix)):
                        position += self.matrix[outputrow][i] * inputmatrix.matrix[i][outputcolumn]
                    output[outputrow][outputcolumn] = position
            return(output)

        else: raise TypeError("Can only multiply a matrix with a number or another matrix")     
    
    def __rmul__(self, other):
        return self*other


    def __truediv__(self, othervalue):
        if type(othervalue) == int or type(othervalue) == float:
            return self * (1/othervalue)
        elif isinstance(othervalue, Matrix):    
            raise TypeError("can't divide a matrix by another matrix")
        else: raise TypeError("can only divide a matrix by a number")
    
    def __pow__(self, exponent):
        if type(exponent) != int:
            raise TypeError("exponent must be an integer")
        else:
            tempmatrix = Matrix([ row[:] for row in self.matrix])
            for _ in range(exponent-1):
                tempmatrix = Matrix(tempmatrix * self)
            return tempmatrix.matrix

    def __eq__(self, othermatrix):
        try: self.check_same_size(othermatrix)
        except: return False
        if isinstance(othermatrix, Matrix):
            if self.matrix == othermatrix.matrix:
                return True
            else: return False
        else: return False

    def __ne__(self, othermatrix):
        if self == othermatrix: return False
        else: return True

    def transpose(self):                                                                           
        output = [[0 for _ in range(len(self.matrix))]for _ in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                output[j][i] = self.matrix[i][j]
        return(output)
    
        #blocks a row and a column, returns leftover matrix
        #row and column : index of list                                                                                       
    def leftover_matrix(self, row : int, column : int):                                                
        tempmatrix = [ row[:] for row in self.matrix]
        for i in range(len(tempmatrix)):
            tempmatrix[i].pop(column)
        tempmatrix.pop(row)
        if tempmatrix == []:
            raise ValueError("leftover matrix is empty/does not exist")
        else:
            return tempmatrix

    def check_square_matrix(self):
        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError("not a square matrix")

    def check_same_size(self, othermatrix):
        if len(self.matrix) != len(othermatrix.matrix):
            raise ValueError("matrices not of same size")
        if len(self.matrix[0]) != len(othermatrix.matrix[0]):
            raise ValueError("matrices not of same size")
    
    def determinant(self):
        self.check_square_matrix()
        if len(self.matrix) == 1:
            return self.matrix[0][0]
        if len(self.matrix) == 2:
            return (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[1][0] * self.matrix[0][1])
        else:
            det = 0
            for j in range(len(self.matrix)):
                sign = (-1) ** j
                smallmatrix = Matrix(self.leftover_matrix(0, j))
                det += (sign * self.matrix[0][j] * smallmatrix.determinant())
            return det
    
        #row and column : index of list
    def minor(self, row, column):
        self.check_square_matrix()
        return Matrix(self.leftover_matrix(row, column)).determinant()
    
    def minors_matrix(self):
        output = [[0 for _ in range(len(self.matrix[0]))]for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                output[i][j] = self.minor(i, j)
        return Matrix(output)

        #row and column : index of list
    def cofactor(self, row, column): 
        self.check_square_matrix()
        return (-1) ** (row+column) * self.minor(row, column)

    def trace(self):
        self.check_square_matrix()
        return sum(self.matrix[i][i] for i in range(len(self.matrix)))

    def cofactors_matrix(self):
        output = [[0 for _ in range(len(self.matrix[0]))]for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                output[i][j] = self.cofactor(i, j)
        return Matrix(output)

        #matrice adjointe       adjugate matrix
    def adjoint_matrix(self):
        return Matrix(self.cofactors_matrix().transpose())
    
    def inverse_matrix(self):
        det = self.determinant
        if det == 0:
            raise ZeroDivisionError("determinant is 0")
        return Matrix(self.adjoint_matrix() / det)

class Augmented_Matrix():
    def __init__(self, leftmatrix, rightmatrix):
        if not (isinstance(leftmatrix, Matrix) and isinstance(rightmatrix, Matrix)):
            raise TypeError("augmented matrix must be created from 2 Matrix objects")
        if len(leftmatrix.matrix) != len(rightmatrix.matrix):
            raise ValueError("both matrices must have same nuber of rows")
        self.leftmatrixwidth = len(leftmatrix.matrix[0])
        self.augmatrix = []
        for i in range(len(leftmatrix.matrix)):
            self.augmatrix.append(leftmatrix.matrix[i] + rightmatrix.matrix[i])
    
    def __str__(self):
        return(str(self.augmatrix))
    
    def return_left_matrix(self):
        tempmatrix = []
        for i in range(len(self.augmatrix)):
            tempmatrix.append(self.augmatrix[i][0 : self.leftmatrixwidth])
        return tempmatrix


    def return_right_matrix(self):
        tempmatrix = []
        for i in range(len(self.augmatrix)):
            tempmatrix.append(self.augmatrix[i][-(len(self.augmatrix[0]) - self.leftmatrixwidth) :])
        return tempmatrix
    
    #rowA and rowB are the list's indexes
    def swap_rows(self, rowA, rowB):
        if type(rowA) != int or type(rowB) != int:
            return TypeError("indexes for rows must be integers")
        self.augmatrix[rowA], self.augmatrix[rowB] = self.augmatrix[rowB] , self.augmatrix[rowA]

    #targetrow and addedrow are the list's indexes
    def add_row_to_row(self, addedrow, targetrow):
        if type(targetrow) != int or type(addedrow) != int:
            return TypeError("indexes for rows must be integers")
        for j in range(len(self.augmatrix[0])):
            self.augmatrix[targetrow][j] = self.augmatrix[targetrow][j] + self.augmatrix[addedrow][j]
        
    #targetrow and sustractedrow are the list's indexes    
    def substract_row_from_row(self, substractedrow, targetrow):
        if type(targetrow) != int or type(substractedrow) != int:
            return TypeError("indexes for rows must be integers")
        for j in range(len(self.augmatrix[0])):
            self.augmatrix[targetrow][j] = self.augmatrix[targetrow][j] - self.augmatrix[substractedrow][j]
    
    #row is the list's index
    def multiply_row_by_constant(self, row, constant):
        if type(row) != int:
            return TypeError("index for row must be integer")
        if type(constant) != int and type(constant) != float:
            return TypeError("constant must be a number")
        for j in range(len(self.augmatrix[0])):
            self.augmatrix[row][j] = self.augmatrix[row][j] * constant
        
    #row is the list's index
    def divide_row_by_constant(self, row, constant):
        if type(constant) != int and type(constant) != float:
            return TypeError("constant must be a number")
        self.multiply_row_by_constant(row, 1/constant)
        


A=[ [1,2,3],
    [4,5,6], 
    [7,8,9] ]
B=[ [1,0,0],
    [0,0,1], 
    [0,1,0] ]
I=[ [1,0,0],
    [0,1,0], 
    [0,0,1] ]    
C=[ [1,0,5],
    [4,0,42], 
    [8,0,1] ]    
D=[ [1,1],
    [4,0] ]
E = [ [1,0,] ]
F = [[25]]
G=[ [6,1,1],
    [4,-2,5], 
    [2,8,7] ]    
H= [ [1,2,1,0],
    [0,3,1,1], 
    [-1,0,3,1],
    [3,1,2,0] ]    
K=[ [1,2,1,0,23,45,-12,6,-1,3],
    [4,5,2,-5,-1,-5,0,6,21,4],
    [4,7,-7,8,-8,9,4,1,6,5],
    [7,2,5,11,2,43,41,13,15,67],
    [-14,15,1,-7,6,-81,1,456,-4,-464],
    [-2,5,144,3,10,17,78,29,65,9],
    [4,46,-561,145,-5,54,613,41,854,6],
    [4,21,-56,41,84,879,12,84,6,45],
    [4,71,54,12051,65,98,7,86951,1,51],
    [-100,-1,-8,4,2,7,4,-42,7,42]]
M=[ [1,2,3,4,5,6,7,8,9,10]]
      

matrixA = Matrix(A)
matrixB = Matrix(B)
matrixC = Matrix(C)
matrixI = Matrix(I)
matrixD = Matrix(D)
matrixE = Matrix(E)
matrixF = Matrix(F)
matrixG = Matrix(G)
matrixH = Matrix(H)
matrixK = Matrix(K)
matrixM = Matrix(M)
#augmatrix = Augmented_Matrix(matrixK, Matrix(matrixM.transpose()))
augmatrix = Augmented_Matrix(matrixA, matrixB)
augmatrix.add_row_to_row(2,0)
augmatrix.substract_row_from_row(1,2)
print(augmatrix.augmatrix)
"""
import timeit
def setup():
    pass

def loop():
   

    A = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    B = Matrix([
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0]
    ])

    temp = A-B
    temp = A*6
    temp = A*B
    temp = B*A
    temp = A.minor(2, 2)
    temp = A.cofactor(2, 2)
    temp = A.transpose()
    temp = A.determinant()
    temp = A.trace()
   
    K = Matrix([ [1,2,1,0,23,45,-12,6,-1,3],
    [4,5,2,-5,-1,-5,0,6,21,4],
    [4,7,-7,8,-8,9,4,1,6,5],
    [7,2,5,11,2,43,41,13,15,67],
    [-14,15,1,-7,6,-81,1,456,-4,-464],
    [-2,5,144,3,10,17,78,29,65,9],
    [4,46,-561,145,-5,54,613,41,854,6],
    [4,21,-56,41,84,879,12,84,6,45],
    [4,71,54,12051,65,98,7,86951,1,51],
    [-100,-1,-8,4,2,7,4,-42,7,42]])
    temp = K.determinant()
   

print(timeit.repeat(stmt=loop, setup=setup, repeat=5, number=1))
"""