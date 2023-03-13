# Author : Jephté Piere
# Date : March 13, 2023
#
# Program that display to the console a tic-tac-toe grid of size n 


n = 3                        # size of the tic-tac-toe grid
hauteur = 3                  # height in number of lines (for example 3) 
largeur = 6                  # width in number of characters (for example 6)
caractereDesLignes = "#"     # character used for solid lines
caractereEspace = " "        # variable used to display the empty lines
posLigneComplete = hauteur   # variable used to display the complete line

for i in range ((n * hauteur) + (n - 1)): # total number of lines
    posColonne = largeur                  # for lines that contain spaces
    ligne_a_afficher = ''
    
    if i % posLigneComplete == 0 and i!= 0 : # for complete line of #
        for j in range ((largeur * n) + (n - 1)):
            ligne_a_afficher += '' + caractereDesLignes             
        posLigneComplete = posLigneComplete + hauteur + 1 
        
    else:                 # lines with spaces at the beginning and "#"
        for j in range ((largeur * n) + (n - 1)): # incomplete line
            if j % posColonne == 0 and j!= 0  :
                ligne_a_afficher += '' + caractereDesLignes
                posColonne = posColonne + largeur + 1  
                
            else:        
                ligne_a_afficher += '' + caractereEspace
                
    print (ligne_a_afficher)
   
