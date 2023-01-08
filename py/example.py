def whatNumIsIt(i1, i2):
    smallest = min([i1,i2])
    biggest = max([i1,i2])
    matrice = [[1,2,3],
        [4,5,6],
        [7,8,9],
        ['*',0,'#']]
    if smallest <= 3 and biggest >= 4:
        return matrice[smallest][biggest-4]
    else:
        return "La combinaison linéaire ne permet pas de déterminer une touche"