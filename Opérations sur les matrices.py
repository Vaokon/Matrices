
class Matrix():
    def __init__(self, inputmatrixlist):
        if type(inputmatrixlist) != list:
            raise TypeError("input matrix must be a 2d list")
        for i in range(1,len(inputmatrixlist)):
            if len(inputmatrixlist[i]) != len(inputmatrixlist[i-1]):
                raise ValueError("all lines must be of the same lenght. all columns must be of the same lenght")
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
            for outputline in range(len(self.matrix)):
                for outputcolumn in range(len(self.matrix[0])):
                    position = 0
                    for i in range(len(inputmatrix.matrix)):
                        position += self.matrix[outputline][i] * inputmatrix.matrix[i][outputcolumn]
                    output[outputline][outputcolumn] = position
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
            for i in range(exponent-1):
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
        output = [[0 for _ in range(len(self.matrix[0]))]for _ in range(len(self.matrix))]
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                output[y][x] = self.matrix[x][y]
        return(output)


    
        #blocks a line and a column, returns leftover matrix
        #line and column : index of list                                                                                       
    def leftover_matrix(self, line : int, column : int):                                                
        tempmatrix = [ row[:] for row in self.matrix]
        for i in range(len(tempmatrix)):
            tempmatrix[i].pop(column)
        tempmatrix.pop(line)
        if tempmatrix == []:
            raise ValueError("leftover matrix is empty/does not exist")
        else:
            return tempmatrix

    def check_square_matrix(self):
        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError("determinant only exist for square matrices")

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
    
        #line and column : index of list
    def minor(self, line, column):
        self.check_square_matrix()
        return Matrix(self.leftover_matrix(line, column)).determinant()
    
    def minors_matrix(self):
        output = [[0 for _ in range(len(self.matrix[0]))]for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                output[i][j] = self.minor(i, j)
        return Matrix(output)

        #line and column : index of list
    def cofactor(self, line, column): 
        self.check_square_matrix()
        return (-1) ** (line+column) * self.minor(line, column)

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
        return Matrix(self.adjoint_matrix() / self.determinant())


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

matrixA = Matrix(A)
matrixB = Matrix(B)
matrixC = Matrix(C)
matrixI = Matrix(I)
matrixD = Matrix(D)
matrixE = Matrix(E)
matrixF = Matrix(F)
matrixG = Matrix(G)
matrixH = Matrix(H)


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


print(timeit.repeat(stmt=loop, setup=setup, repeat=5, number=10000))
"""