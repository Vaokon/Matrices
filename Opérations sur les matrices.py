import timeit
class Matrix():
    def __init__(self, inputmatrix):
        if type(inputmatrix) != list:
            raise TypeError("input matrix must be a 2d list")
        self.matrix = inputmatrix
    
    
    def addition(self, inputmatrix):
        if type(inputmatrix) != list:
             raise TypeError("matrices must be of the same size for addition")
        output = [[0 for _ in range(len(self.matrix[0]))]for _ in range(len(self.matrix))]
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                output[x][y] = self.matrix[x][y] + inputmatrix[x][y]
        return output
    
    def substract(self, inputmatrix):
        return self.addition(Matrix(inputmatrix).multiplication(-1))
    
        #input matrix must be an int or a list
    def multiplication(self, inputmatrix):
            # Multiplication by a constant
        if type(inputmatrix) == int or type(inputmatrix) == float:                                           
            output = [[0 for _ in range(len(self.matrix[0]))]for _ in range(len(self.matrix))]
            for x in range(len(self.matrix)):
                for y in range(len(self.matrix[0])):
                    output[x][y] = self.matrix[x][y] * inputmatrix
            return(output)
            
            #Multiplication by another matrix
        elif type(inputmatrix) == list:                                                                 
            output = [[0 for _ in range(len(inputmatrix))]for _ in range(len(self.matrix[0]))]
            for outputline in range(len(self.matrix)):
                for outputcolumn in range(len(self.matrix[0])):
                    position = 0
                    for i in range(len(inputmatrix)):
                        position += self.matrix[outputline][i] * inputmatrix[i][outputcolumn]
                    output[outputline][outputcolumn] = position
            return(output)

        
        else: raise TypeError("Can only multiply a matrix with a number or another matrix")     

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

        #line and column : index of list
    def cofactor(self, line, column): 
        self.check_square_matrix()
        return (-1) ** (line+column) * self.minor(line, column)

    def trace(self):
        self.check_square_matrix()
        return sum(self.matrix[i][i] for i in range(len(self.matrix)))


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



print(matrixA.substract(matrixB.matrix))
print(matrixA.trace())
print(matrixH.determinant())
print(matrixG.determinant())   #devrait donner -306
print("A: ", matrixA.leftover_matrix(2,1))


print("B: ", matrixB.leftover_matrix(2,2))
try :
    print("C: ", matrixC.leftover_matrix(3,2))
except: pass
print("D: ", matrixD.leftover_matrix(1,0))
#print("E: ", matrixE.leftover_matrix(0,0))
#print("F: ", matrixF.leftover_matrix(,))
print("I: ", matrixI.leftover_matrix(1,1))
"""

#print("E: ", matrixE.determinant())
#print("F: ", matrixF.determinant())
#print("D: ", matrixD.determinant())
#print("A: ", matrixA.determinant())
"""print("B: ", matrixB.determinant())
print("C: ", matrixC.determinant())
print("I: ", matrixI.determinant())
"""

"""
print(matrixA.minor(0,1))


print(matrixA.addition(matrixB.matrix))

print(matrixB.multiplication(matrixA.matrix))


"""
"""
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

    temp = A.substract(B.matrix)
    temp = A.multiplication(6)
    temp = A.multiplication(B.matrix)
    temp = B.multiplication(A.matrix)
    temp = A.minor(2, 2)
    temp = A.cofactor(2, 2)
    temp = A.transpose()
    temp = A.determinant()
    temp = A.trace()


print(timeit.repeat(stmt=loop, setup=setup, repeat=5, number=10000))
"""