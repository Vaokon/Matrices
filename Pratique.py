A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [[1, 0, 0],
     [0, 0, 1],
     [0, 1, 0]]


def addition(self, autre):
    if type(autre) != list:
        raise TypeError
    sortie = [[0 for _ in range(len(self[0]))]for _ in range(len(self))]
    for i in range(len(self)):
        for j in range(len(self[i])):
            sortie[i][j] = self[i][j] + autre[i][j]
    return sortie

#print("résultat: ", addition(A, B))


def matrice_restante(matrice, ligne, colonne):                                               #ligne et colonne : index dans la liste, pas le i ou le j normal.
        if type(ligne) != int or type(colonne) != int:
            raise TypeError("Coordonnées d'unt être des entiers")
        matricetemp = matrice.copy()
        for i in range(len(matricetemp)):
            matricetemp[i].pop(colonne)
        matricetemp.pop(ligne)
        if matricetemp == []:
            raise ValueError("la matrice restante est vide/n'existe pas")
        else:
            return matricetemp

def déterminant(matrice):
    if len(matrice) == 1:
        return matrice[0][0]
    if len(matrice) == 2:
        return (matrice[0][0] * matrice[1][1]) - (matrice[1][0] * matrice[0][1])
    else:
        det = 0
        for j in range(len(matrice)):
            print(j)
            if j % 2 == 0:
                signe = -1
            elif j % 2 == 1:
                signe = 1
            petitematrice = matrice_restante(matrice, 0, j)
            print(petitematrice)
            #det += signe * petitdet

        return det


#print(déterminant(A))