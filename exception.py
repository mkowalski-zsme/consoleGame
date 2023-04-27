x = 0
while True:
    try:
        x = int(input("Podaj liczbę od 1 - 10: "))
        if x >= 1 and x<=10:
            break
    except:
        pass


print(x)