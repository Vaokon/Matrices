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
    
    
    def multiplication(self, inputmatrix):
        if type(inputmatrix) == int or type(inputmatrix) == float:                                           # Multiplication by a constant
            output = [[0 for _ in range(len(self.matrix[0]))]for _ in range(len(self.matrix))]
            for x in range(len(self.matrix)):
                for y in range(len(self.matrix[0])):
                    output[x][y] = self.matrix[x][y] * inputmatrix
            return(output)
            
        elif type(inputmatrix) == list:                                                                 #Multiplication by another matrix
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


    
    
                                                                                            #blocks a line a column, returns leftover matrix
    def leftover_matrix(self, line, column):                                                #line and column : index of list
        if type(line) != int or type(column) != int:
            raise TypeError("line and column index must be int")

        for i in range(len(self.matrix)):
            self.matrix[i].pop(column)
        self.matrix.pop(line)
        if self.matrix == []:
            raise ValueError("leftover matrix is empty/does not exist")
        else:
            return self.matrix

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
                print(j)
                if j%2 == 0:
                    sign = -1
                elif j%2 == 1:
                    sign = 1
                smallmatrix = Matrix(self.leftover_matrix(0, j))
                print(smallmatrix.matrix)


                
            return det

    
        
        
        
    
    
    
    



    def cofactor(self, line, column):                                    #line and column : index of list
        pass


"""A=[ [1,2,3],
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
E = [ [1,0] ]
F = [[25]]"""

matrixA = Matrix(A)
matrixB = Matrix(B)
matrixC = Matrix(C)
matrixI = Matrix(I)
matrixD = Matrix(D)
matrixE = Matrix(E)
matrixF = Matrix(F)


print(matrixA.determinant())

"""
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
