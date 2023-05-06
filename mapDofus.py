import pygame
import random
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
# Définition de la taille des cellules
cellSize =80
cell_width = cellSize * 0.55
cell_height = cellSize * 0.3
#Code link to the map ------------------------------------------------------------------------------------------------------------------------------------------
window_size = (15*cell_width, 22*cell_height)
screen = pygame.display.set_mode(window_size)


# Couleurs des carrés
floorBright = "#978e66"
floorDark = "#8e865d"
colorWall = "#58533a"
colorVoid = "black"

class Map:

    def __init__(self,currentMap):
        self.currentMap = currentMap



class Cell:
    #Init of the cell
    def __init__(self,xInput,yInput,colorInput):
        self.color=colorInput


        self.x = xInput
        self.y = yInput

        self.type = None
        self.occupation = False

        if self.color == floorBright or self.color ==floorDark:
            self.type = "floor"
        elif self.color == colorWall:
            self.type = "wall"
        else:
            self.type = "void"



    # Fonction pour dessiner un carré incliné
    def draw_square(self):
        x=self.x
        y=self.y+cell_height
        color=self.color
        square_points = [
            (x + cell_width // 2, y +2),
            (x + cell_width -2 , y + cell_height // 2 ),
            (x + cell_width // 2 , y + cell_height -2),
            (x +2 , y + cell_height // 2 )
        ]
        
        pygame.draw.polygon(screen, color, square_points)








def createMapWithPhoto():
    cellList = []
    map = np.zeros((40,28))
    # Ouvrir l'image
    img = Image.open("test.png")
    img = img.resize((1200,800))
    # Convertir l'image en tableau Numpy
    np_img = np.array(img)
    print(np_img.shape)
    xsize = int(1200/14)
    ysize = int(800/20)
    #Iterate on the column, i the column
    for i in range(1,29):

        print("---------")
        if i%2 ==0:
            #Iterate on the line, j the line
            for j in range(1,21):
                x = int(i*0.485* xsize)
                y = int(j * 0.98*ysize-0.25*ysize)
                
                map[j-1][i-1]=np_img[y ,x][0]
                
                """np_img[y ,x] = np.array([255,0,0,255])
                np_img[y+1 ,x] = np.array([255,0,0,255])
                np_img[y-1 ,x] = np.array([255,0,0,255])

                np_img[y ,x-1] = np.array([255,0,0,255])
                np_img[y+1 ,x-1] = np.array([255,0,0,255])
                np_img[y-1 ,x-1] = np.array([255,0,0,255])

                np_img[y ,x+1] = np.array([255,0,0,255])
                np_img[y+1 ,x+1] = np.array([255,0,0,255])
                np_img[y-1 ,x+1] = np.array([255,0,0,255])"""


        else:
            #Iterate on the line
            for j in range(20):
                x = int(i*0.485* xsize)
                y = int(j * 0.98*ysize + 0.5 * ysize-0.25*ysize)
                map[j-1][i-1]=np_img[y ,x][0]
                """np_img[y ,x] = np.array([255,0,0,255])
                np_img[y+1 ,x] = np.array([255,0,0,255])
                np_img[y-1 ,x] = np.array([255,0,0,255])

                np_img[y ,x-1] = np.array([255,0,0,255])
                np_img[y+1 ,x-1] = np.array([255,0,0,255])
                np_img[y-1 ,x-1] = np.array([255,0,0,255])

                np_img[y ,x+1] = np.array([255,0,0,255])
                np_img[y+1 ,x+1] = np.array([255,0,0,255])
                np_img[y-1 ,x+1] = np.array([255,0,0,255])"""


    #Read the color and write in in a cell
    for i in range (40):
        for j in range(28):
            x = (j//2 +j%2*0.5 )* cell_width
            y = (i-j%2*0.5) * cell_height
            color = map[i][j]

            if color <=50:
                color = colorVoid
            elif 50<color and color <=95:
                color = colorWall
            elif 95<color and color <=145:
                color = floorBright
            elif 145<color and color <=255:
                color = floorDark

            cellList.append(Cell(x,y,color))

    for cell in cellList:
        cell.draw_square()
    pygame.display.flip()


    plt.imshow(np_img)
    plt.show()    
    return(cellList)


    
    

#Code link to the gameplay ------------------------------------------------------------------------------------------------------------------------------------------
mapToPlay=None
def changeCurrentMap(currentMapInput):
    global mapToPlay
    mapToPlay = currentMapInput


class Personnage(pygame.sprite.Sprite):

    def __init__(self,classe,pv,pa,pm,po):
        super().__init__()
        self.classe
        self.pv
        self.pa
        self.pm
        self.po

        self.x
        self.y

class Eliotrope(Personnage):
    def __init__(self,pv,pa,pm,po,x,y):
        self.classe = "eliotrope"
        self.pv = pv
        self.pa = pa
        self.pm = pm
        self.po = po

        self.x = x
        self.y = y
    
    def deplacer():
        pass




    

# Boucle principale du jeu
running = True
firstTime = True

while running:
    """personnage1 = Eliotrope(pv=100,pa=6,pm=3,po=1,x=5,y=5)"""
    #If window is closed then end the prog
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #If firstime create the map
    if firstTime:
        cellList= createMapWithPhoto()
        currentMap = Map(cellList)
        classes.changeCurrentMap(currentMap)
        firstTime= False
    
    """#If first time then create the map
    if firstTime:
        cellList= createRandomMap()
        firstTime= False
    """


    

    # Actualisation de l'affichage
    """for cell in cellList:
        cell.draw_square()
    pygame.display.flip()"""


# Fermeture de Pygame
pygame.quit()



