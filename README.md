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

## Import bibliotek
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
## Definicje funkcji

```
def printWhite(data):
    print(Fore.WHITE,data,end="",sep="")

def printRed(data):
    print(Fore.RED,data,end="",sep="")

def printGreen(data):
    print(Fore.GREEN,data,end="",sep="")

```

Powyższe funkcje służą do wygodnego pisania w kolorze (na biało, czerwono i zielono), bez znaku końca linii

## Funkcja rysująca planszę:

1. Czyszczenie ekranu: `os.system('cls')`
2. Definicja elementów z których składają się ramki planszy w postaci słownika np.:
lewy górny znak -> symbol kodu ASCII o numerze 218: `┌` itd...
3. Definicja elemntów służących do rysowania linii - pionowej: `│` i poziomej: `─`
4. Pobranie rozmiaru ekranu (ilość wierszy w liście): `size = len(screen)`
5. Definicja listy składającej się z trzech znaków poziomych linii o rozmiarze `size`
np. `['───', '───', '───', '───', '───', '───', '───', '───', '───', '───']`
6. Kompozycja listy z poziomymi liniami w linie górną, środkową i dolną. Do tego celu użyta została metoda `join`, która skleja elementy listy `verticalLine` w jedną całość za pomocą odpowiedniego znaku. W ten sposób powstają gotowe do użycia teksty zawierające linie:
- linia górna: `───┬───┬───┬───┬───┬───┬───┬───┬───┬───`
- linia środkowa: `───┼───┼───┼───┼───┼───┼───┼───┼───┼───`
- linia dolna: `───┴───┴───┴───┴───┴───┴───┴───┴───┴───`
7. Kolejny etap to składanie przygotowanych elementów w całą planszę:
- Lewy górny narożnik + górna linia + prawy górny narożnik:
```printWhite(corners["upperLeft"]+verticalUp+corners["upperRight"]+"\n")```
co w efekcie da:
`┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐`
- Następnie w pętli odbywa się rysowanie kolejnych wierszy planszy zaczynając od poziomej linii (lewej krawędzi): `printWhite(lines["vertical"])`, następnie dla każdej kolumny w wierszu: `for j in row:` następuje rysowanie pola:
  - jeżeli wartość listy jest dodatnia, to narysuj krzyżyk ( X )
  - jeżeli wartość listy jest ujemna, to narysuj kółko ( O )
  - a jeżeli wartość rórna jest 0, to narusyj spację (pusty obszar).
Dla różnych gier mogą to być zupełnie inne wartości... 
Po każdym polu (z prawej strony) rysowana jest pionowa linia: `│`
- Rysowanie wierszy powtarza się dla wszystkich wierszy listy. 
Dla ostatniego wiersza ```if(i < size-1): printWhite(corners["mediumLeft"]+verticalMid+corners["mediumRight"]+"\n") ``` nie jest już rysowana środkowa linia, ponieważ poniżej nie znajduje się już nic.
- Na samym końcy rysowana jest linia dolna: 
```printWhite(corners["bottomLeft"]+verticalDown+corners["bottomRight"]+"\n")```
która wygląda następująco: `└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘`

# Funkcja główna

1. Rozpoczęcie skryptu od sprawdzenie czy to ten plik jest uruchamiany:
```if __name__ == "__main__":```
2. Utworzenie listy dwuwymiarowej wypełnionej zerami (pusta plansza):
```
    rozmiar = 10 #rozmiar planszy: 10 x 10
    dane = [] #definicja pustej listy
    for i in range(rozmiar): #dla każdego wiersza
        kolumna = [0 for i in range(rozmiar)] #wygeneruj 10 kolumn wypełnionych zerami
        dane.append(kolumna) #wrzuć gotowy wiersz do listy
```
Po uruchomieniu tego fragmentu utworzy się lista zawierająca w sobie 10 list, każda zawierająca 10 zer. To będzie reprezentacja stanu gry:
```
   [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
```
3. Następnie rozpoczyna się rozgrywka (nieskończona pętla), w któej rysowana jest plansza, a gracze naprzemiennie wprowadzają współrzędne swoich ruchów.

Gra nie kontroluje poprawności ruchów, tak więc możliwe jest wprowadzanie współrzędnych poza planszą, lub współrzędnych zajętego miejsca.





