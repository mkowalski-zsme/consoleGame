import os
from colorama import Fore, Back

def printWhite(data):
    print(Fore.WHITE,data,end="",sep="")

def printRed(data):
    print(Fore.RED,data,end="",sep="")

def screenXO(screen):
    os.system('cls')
    corners = {
               "upperLeft":     "┌",    #218 np. chr(218)
               "upperRight":    "┐",    #191
               "mediumLeft":    "├",    #195 
               "mediumRight":   "┤",    #180
               "bottomLeft":    "└",    #192
               "bottomRight":   "┘",    #217
               "upperMid":      "┬",    #194
               "midiumMid":     "┼",    #197
               "bottomMid":     "┴"     #193
              }
    lines =   {
               "vertical": "│",         #179
               "horizontal": "─"        #196
              }
    
    size = len(screen)                  #rozmiar ekranu
    verticalLine = [lines["horizontal"]*3]*size         #lista zawierająca poziome linie
    #print(verticalLine)
    
    verticalUp = corners["upperMid"].join(verticalLine)
    verticalMid = corners["midiumMid"].join(verticalLine)
    verticalDown = corners["bottomMid"].join(verticalLine)

    printWhite(corners["upperLeft"]+verticalUp+corners["upperRight"]+"\n")
 
    for i,row in enumerate(screen):
        printWhite(lines["vertical"])
        for j in row:
            if(j>0): printWhite(" X ")
            elif j<0: printRed(" O ")
            else: printWhite("   ")
            printWhite(lines["vertical"])            
        print()
        if(i < size-1): print(corners["mediumLeft"]+verticalMid+corners["mediumRight"])
    
    print(corners["bottomLeft"]+verticalDown+corners["bottomRight"])


import random


rozmiar = 12
dane = []
for i in range(rozmiar):
    wiersz = [0 for i in range(rozmiar)]
    dane.append(wiersz)

gracz = 1
while True:
    screenXO(dane)

    x = int(input("Podaj 1 wsp: "))-1
    y = int(input("Podaj 2 wsp: "))-1

    dane[y][x] = gracz
    gracz *= -1
    
