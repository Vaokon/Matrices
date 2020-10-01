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

class Matrice():
    def __init__(self, matrice):
        if type(matrice) != list:
            raise TypeError("La matrice en entrée doit être une liste")
        self.matrice = matrice
    
    
    def addition(self, autre):
        if type(autre) != list:
             raise TypeError("Addition de matrice doit se faire entre deux matrices")
        sortie = [[0 for _ in range(len(self.matrice[0]))]for _ in range(len(self.matrice))]
        for x in range(len(self.matrice)):
            for y in range(len(self.matrice[0])):
                sortie[x][y] = self.matrice[x][y] + autre[x][y]
        return sortie
    
    
    def multiplication(self, autre):
        if type(autre) == int or type(autre) == float:                                           # Multiplication par une constatne
            sortie = [[0 for _ in range(len(self.matrice[0]))]for _ in range(len(self.matrice))]
            for x in range(len(self.matrice)):
                for y in range(len(self.matrice[0])):
                    sortie[x][y] = self.matrice[x][y] * autre
            return(sortie)
            
        elif type(autre) == list:                                                                 #Multiplication par une autre matrice
            sortie = [[0 for _ in range(len(autre))]for _ in range(len(self.matrice[0]))]
            for lignesortie in range(len(self.matrice)):
                for colonnesortie in range(len(self.matrice[0])):
                    case = 0
                    for i in range(len(autre)):
                        case += self.matrice[lignesortie][i] * autre[i][colonnesortie]
                    sortie[lignesortie][colonnesortie] = case
            return(sortie)

        
        else: raise TypeError("Multiplication avec une matrice(liste) ou un nombre")     

    def transposée(self):                                                                           #Transposée
        sortie = [[0 for _ in range(len(self.matrice[0]))]for _ in range(len(self.matrice))]
        for x in range(len(self.matrice)):
            for y in range(len(self.matrice[0])):
                sortie[y][x] = self.matrice[x][y]
        return(sortie)


    
    
                                                                                            #bloque une ligne et une colonne et donne la matrice résultante.
    def matrice_restante(self, ligne, colonne):                                               #ligne et colonne : index dans la liste, pas le i ou le j normal.
        if type(ligne) != int or type(colonne) != int:
            raise TypeError("Cagfmsjngdggdfnhkdfhglkdf")

        for i in range(len(self.matrice)):
            self.matrice[i].pop(colonne)
        self.matrice.pop(ligne)
        if self.matrice == []:
            raise ValueError("la matrice restante est vide/n'existe pas")
        else:
            return self.matrice

    def check_matrice_carrée(self):
        if len(self.matrice) == len(self.matrice[0]):
            return True
        else: return False
    
    def déterminant(self):
        if not self.check_matrice_carrée():
            raise ValueError("le déterminant n'existe que pour les matrices carrées")
        if len(self.matrice) == 1:
            return self.matrice[0][0]
        if len(self.matrice) == 2:
            return (self.matrice[0][0] * self.matrice[1][1]) - (self.matrice[1][0] * self.matrice[0][1])
        else:
            det = 0
            for j in range(len(self.matrice)):
                print(j)
                if j%2 == 0:
                    signe = -1
                elif j%2 == 1:
                    signe = 1
                petitematrice = Matrice(self.matrice_restante(0, j))
                print(petitematrice.matrice)
                #det += signe * petitdet

                
            return det

    
        
        
        
    
    
    
    



    def cofacteur(self, ligne, colonne):                                    #ligne et colonne : index dans la liste
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

matriceA = Matrice(A)
matriceB = Matrice(B)
matriceC = Matrice(C)
matriceI = Matrice(I)
matriceD = Matrice(D)
matriceE = Matrice(E)
matriceF = Matrice(F)


print(matriceA.déterminant())

"""
print("A: ", matriceA.matrice_restante(2,1))
print("B: ", matriceB.matrice_restante(2,2))
try :
    print("C: ", matriceC.matrice_restante(3,2))
except: pass
print("D: ", matriceD.matrice_restante(1,0))
#print("E: ", matriceE.matrice_restante(0,0))
#print("F: ", matriceF.matrice_restante(,))
print("I: ", matriceI.matrice_restante(1,1))
"""

#print("E: ", matriceE.déterminant())
#print("F: ", matriceF.déterminant())
#print("D: ", matriceD.déterminant())
#print("A: ", matriceA.déterminant())
"""print("B: ", matriceB.déterminant())
print("C: ", matriceC.déterminant())
print("I: ", matriceI.déterminant())
"""

"""
print(matriceA.mineur(0,1))


print(matriceA.addition(matriceB.matrice))

print(matriceB.multiplication(matriceA.matrice))


"""
