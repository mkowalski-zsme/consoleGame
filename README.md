# Gra konsolowa.

##Grafika w konsoli
Przykładowa plansza w konsoli:
```
┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
│   │   │   │   │   │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │   │   │   │   │
└───┴───┴───┴───┴───┴───┴───┴───┴───┘
```

Funkcja rysująca planszę gry składa się z następujących znaków ASCII (tablica ASCII: https://www.asciitable.com/):
- górny lewy narożnik np. znak `┌`, kod ASCII: 218
- środkowy lewy narożnik np. znak `├`, kod ASCII: 195
- itd...

Opis działania kodu:


```
import os
from colorama import Fore, Back
```
Biblioteka `os` zawiera funkcje umożliwiające wywałanie poleceń systemu operacyjnego. W tym przykładzie użyta jest funkcja `system` wywołująca polecenie konsoli `cls` - czyszczenie ekranu. Uwaga: funkcja cls jest stosunkowo wolna!

Biblioteka `colorama` umożliwia "pisanie" w dostępnych kolorach. Zaimportowane zmienne `Fore` - kolor tekstu i `Back` - kolor tła.
Dostępne kolory:
- YELLOW
- WHITE
- RED
- CYAN
- BLUE
- BLACK
- GREEN
- MAGENTA

oraz kolory o wzmocnionej jasności:
- LIGHTYELLO_EX
- LIGHTWHITE_EX
- itd...

np.
```
print(Back.LIGHTYELLOW_EX,Fore.GREEN,"test")
print(Back.YELLOW,Fore.BLUE,"test")
```



