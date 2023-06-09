# Auteur : Jephte Pierre
# Date : 13 Mars 2023
#
# Ce programme dessine un labyinte de taille n et prend plusiueurs
# paramètres. Tous les parametres sont des entiers >=1.


# Cette fonction prend un entier non-négatif n en paramètre et retourne un 
# tableau de longueur n contenant en ordre les valeurs entières de 0 à n-1 

def iota(n) : 
    tab = [0]*n
    for i in range(n) :
        tab[i] = i 
    return tab

# Cette fonction prend en paramètre un tableau de nombres (tab) et un
# nombre x et retourne un booléen indiquant si x est contenu dans le tableau.

def contient(tab, x):
    return x in tab 

# Cette fonction prend en paramètre un tableau de nombres (tab) et un 
# nombre x et retourne un nouveau tableau avec le même contenu que tab
# sauf que x est ajouté à la fin s'il n'est pas déjà contenu dans tab.

def ajouter(tab, x):
    if x not in tab:
        tab.append(x)
    return tab

# Cette fonction prend en paramètre un tableau de nombres (tab) et un nombre
# x et retourne un nouveau tableau avec le même contenu que tab sauf que x
# est retiré du tableau.

def retirer (tab, x):
    if x in tab :
        tab.remove(x)
    return tab

# Cette fonction prend la coordonnée (x,y) d'une cellule et la taille
# d'une grille (largeur=nX et hauteur=nY) et retourne un tableau contenant
# le numéro des cellules voisines et qui ajoute les cellules

def voisins(x, y, nX, nY):
    tab = []
    tempX = x-1
    tempY = y
    if tempX>=0:                   
        ajouter(tab,tempX+tempY*nX)
    tempX = x+1
    tempY= y
    if tempX<nX:
        ajouter(tab,tempX+tempY*nX) 
    tempY = y-1
    tempX = x
    if tempY>=0:
        ajouter(tab,tempX+tempY*nX) 
    tempY= y+1
    if tempY<nY:
        ajouter(tab,tempX+tempY*nX) 
    return tab


def randomCellNumber(n) : 
    return math.floor(n*random())

#fonction qui retourne un tableau contenant les éléments
#en commun des tableaux entrés en paramètres  

def common(tab1, tab2):
    tab3 = []
    for i in tab1:
        if contient(tab2, i):
            ajouter(tab3, i)
    return tab3

# dessine la grille en blanc

def createGrid(nX,nY,largeurCase, mursH, mursV) : 
    row = nY*(largeurCase+1)
    column = nX*(largeurCase+1)
    setScreenMode(column+1,row+1)
    
    for i in range(0, row+1):
        for j in range(0, column+1):
            setPixel(j,i, struct(r=15, g=15, b=15))
          
    pixelX=0
    pixelY=0
    
    for mur in range(nX*(nY+1)):
        if(mur in mursH):
            for x in range(largeurCase+1):
                setPixel(pixelX,pixelY, struct(r=0, g=0, b=0))
                pixelX+=+1
            
        else:
            pixelX+=largeurCase+1
        if ((mur+1)%nX==0):
            pixelX = 0
            pixelY += largeurCase+1
        
    pixelX=0
    pixelY=0
    x_final = nX*(largeurCase+1)
    
    for mur in range((nX+1)*nY):
        if pixelX>x_final:
            pixelX = 0
        if mur in mursV:
            pixelY = (mur//(nX+1)) * (largeurCase+1)
            for i in range(largeurCase+1):
                setPixel(pixelX,pixelY,struct(r=0, g=0, b=0))
                pixelY += 1
            setPixel(pixelX,pixelY, struct(r=0, g=0, b=0)) 
        pixelX += largeurCase + 1

# Cette procédure crée un labyrinthe aléatoire (largeur=nX et hauteur=nY)
# et dessine ce labyrinthe dans la fenêtre de pixels en utilisant une grille


def laby(nX, nY, largeurCase) :
    mursH =  []
    n_final = (nX-1)+(nY-1)*nX               # taille du labyrinthe
    s_final = (nX-1)+ (nY-1+1)*nX            # dernier mur horizontal
    
    for i in range (1, s_final):             # création de l'ensemble des
                                             # murs horizontaux tout
                                             # en fixant l'entrée et la
                                             # sortie
        mursH.append(i)          
        
    mursV = iota((nX+1)*nY)                  # création de l'ensemble des
                                             # murs verticaux
    front = []
    cave = []
    randomNumber = randomCellNumber(n_final) # On trouve ses coordonnées
    x = randomNumber%nX                   
    y = randomNumber//nX        
    
    ajouter (cave,randomNumber)              #création de la cavité initiale
    front = voisins(x, y, nX, nY) 
    
    for i in range(n_final):                 # tant que toutes les cellulesne
                                             # sont pas encore dans la cavité
            
        i = randomCellNumber(len(front))     # choisir une indice
                                             # aléatoirement de 
                                             # l'ensemble cellules voisines
                                             # initiales
                    
        randomNumber = front[i]  
            
        x = randomNumber%nX                  # Determiner les coordonnées
                                             # de chaque cellule
        y = randomNumber//nX     
        
        e = 1+x+y*(nX+1)         
        s = x + (y+1)*nX        
        o = x+y*(nX+1)           
        n = x + y * nX           
        
        near = voisins(x, y, nX, nY)         # cellules voisines
                                   
            
        commonCells = common(cave, near)     # cellules en communs entre
                                             # voisines et cavité
                                      
                    
        i  = randomCellNumber(len(commonCells)) 
                                        
        randomCommonCell = commonCells[i]       
        
        if abs(randomNumber - randomCommonCell) == 1: 
            if randomNumber > randomCommonCell:
                retirer(mursV, o)           
                
            else:
                retirer(mursV, e)             
                
        elif abs(randomNumber - randomCommonCell) == nX:
            if randomNumber > randomCommonCell:
                retirer(mursH, n)        
                
            else:
                retirer(mursH, s)            
        ajouter(cave, randomNumber) 
                
        for j in near:              
            ajouter(front, j)       
            
        for j in cave :                     # retirer de l'ensemble vosines
                                            # les cellules qui sont dèja 
                                            # dans la cavité
            retirer(front, j)       
            
    createGrid(nX, nY, largeurCase, mursH, mursV) 
    
laby (16, 9, 20)

def testIota() : # tests unitaires 
    assert iota(0) == []
    assert iota(5) == [0,1,2,3,4]
testIota()  

def testContient() : # tests unitaires 
    assert contient([],0) == False
    assert  contient([9,2,5], 2) == True
    assert  contient([9,2,5], 4) == False
    assert contient([2.0],2) == True
testContient()

def testAjouter() :# tests unitaires 
    assert ajouter([9,2,5], 2) == [9,2,5]
    assert ajouter([9,2,5], 4) == [9,2,5,4]
    assert ajouter([9,2,5.0],5) == [9,2,5]
    assert ajouter([],2) == [2]
testAjouter   

def testRetirer() : # tests unitaires 
    assert retirer([9,2,5], 2) == [9,5]
    assert retirer([9,2,5], 4) == [9,2,5]
    assert retirer([9,2,5.0],5) == [9,2]
    assert retirer([],2) == []
testRetirer()   

def testVoisins() : # tests unitaires 
    assert voisins(7, 2, 8, 4) == [22,15,31]
    assert voisins(0, 0, 8, 4) == [1,8]
    assert voisins(0, 0, 1, 1) == []
testVoisins()

def testRandomCellNumber() : #tests unitaires
    assert randomCellNumber(0) == 0
    assert (randomCellNumber(10) >= 0) == True
    assert (randomCellNumber(10) <= 10) == True
testRandomCellNumber()

def testCommon() : #tests unitaires
    assert common([],[]) == []
    assert common([],[2]) == []
    assert common([2,3],[3]) == [3]
testCommon()
